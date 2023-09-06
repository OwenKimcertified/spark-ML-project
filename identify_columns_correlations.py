from hdfs import InsecureClient
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import IntegerType
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from kafka import KafkaProducer
import datetime

hdfs_client = InsecureClient('http://127.0.0.1:9870', user = 'owen')
hdfs_directory = '/partition_csv'
file_list = hdfs_client.list(hdfs_directory)

# setting for ssh 

import os
local_ip = '127.0.0.1'
os.environ['SPARK_LOCAL_IP'] = local_ip

# setting for out of memory

MAX_MEMORY = '1g' 

ss = SparkSession.builder.appName('spark-ml')\
                          .config('spark.executor.memory', MAX_MEMORY)\
                          .config('spark.driver.memory', MAX_MEMORY)\
                          .getOrCreate()

ADDR = 'hdfs://127.0.0.1:9000/partition_csv/*'

df = ss.read.csv(ADDR, header = True, inferSchema = True)

def convert_to_seconds(time_str):
    parts = time_str.split(":")
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

# make user defined func
convert_to_seconds_udf = udf(convert_to_seconds, IntegerType())

df = df.withColumn("driving_time_seconds", convert_to_seconds_udf(col("driving_time")))

# label (target) = total_amount 

# features = driving_time, trip_distance

df.createOrReplaceTempView('df')

query ="""
select trip_distance, driving_time_seconds, total_amount
from df
"""

for_train = ss.sql(query)

train_df, test_df = for_train.randomSplit([.7, .3], seed = 42)

vecssemble = VectorAssembler(inputCols = ['trip_distance', 'driving_time_seconds'], outputCol = 'vecrized_features')

v_train, v_test = vecssemble.transform(train_df), vecssemble.transform(test_df)

lr = LinearRegression(maxIter = 10,
                      labelCol = 'total_amount',
                      featuresCol = 'vecrized_features')

model = lr.fit(v_train)

brokers = ["localhost:9091", "localhost:9092", "localhost:9093"]
topicname = "sparkml_logs" 

producer = KafkaProducer(bootstrap_servers = brokers)

current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

def logging_kafka():
    text = f"date : {formatted_datetime},\
            r2_score : {model.summary.r2},\
            coefficients = {model.coefficients},\
            intercept = {model.intercept}"

    byte_text = text.encode('utf-8')

    if model.summary.r2 < 0.5:
        producer.send(topicname, b"r2 score is too low to do something please tune again")   
        producer.flush() 
        producer.close()
    else:
        producer.send(topicname, byte_text)
        producer.flush() 
        producer.close()

try: 
    logging_kafka()

except Exception as e:
    log = f"error occur : {e}"
    f_log = log.encode('utf-8')
    producer.send(topicname, f_log)


# terminal status

"""
ConsumerRecord(topic='sparkml_logs', partition=0, offset=0, timestamp=1693250398921, timestamp_type=0, key=None, value=b'date : 2023-08-29 04:19:58,  
               r2_score : 0.742453786141426,      
               coefficients = [3.1801014737444957,2.3611092950901223e-05],       
               intercept = 8.869528838228186', headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=180, serialized_header_size=-1)
"""
