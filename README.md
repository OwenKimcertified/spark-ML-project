TOY PROJECT - SPARK ML

topic
대용량 데이터를 모델에 학습 시 컴퓨터가 멈추는 현상, out of memory + @

Issue - solve 
데이터를 병렬처리 : HDFS 에 데이터를 분산하고 저장.
최적화된 계획 : 지연된 연산과 캐싱을 활용하여 필요한 일을 필요할 시 진행.

Project process         
                 HDFS                                                                                     
                                                                spark ml                                            
                                                                     




   
                                 kafka topic

                      
                                                                  
EDA 가 완료된 파일들을 HDFS 에서 불러오기.
spark 의 dataframe 으로 만들고 쿼리 후 학습을 진행.
학습 완료 시 kafka 의 메시지 큐에 logging (r2_score, coefficient..)


<img src = 'https://drive.google.com/uc?id=1SOplKkXbewpArTwB0YFMMQzI6PfufJ5T' width = 600 height = 800>

