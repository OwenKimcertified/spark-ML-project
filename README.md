# SPARK - ML 
# FEATURE - TARGET Corelations
![image](https://github.com/OwenKimcertified/spark-ML-toy/assets/99598620/666d697a-8b02-454e-ad5f-50b7cd0e1965)
![image](https://github.com/OwenKimcertified/spark-ML-toy/assets/99598620/be2ef94d-6bb6-491d-ab7f-dd6b36150f46)
![image](https://github.com/OwenKimcertified/spark-ML-toy/assets/99598620/30063ca2-2af4-49f1-8d28-6bb879c23d4b)
![image](https://github.com/OwenKimcertified/spark-ML-toy/assets/99598620/bebcd813-a7b3-4d99-902d-7aae2a8512da)
# setting
- ubuntu 22.04 LTS

- Hadoop 3.3.4

- spark 3.3.3

- docker - zookeeper3.7, kafdrop(obsidian_dynamics), kafka7.0
# spark - ml 을 사용한 이유와 회고

spark -ml 을 사용한 이유는 hdfs 에 저장되는 파일들은 높은 확률로 대용량 데이터이고 

그 대용량 데이터들을 분산 처리 후 저장했기 때문입니다.

hdfs 에 데이터를 저장할 때부터 큰 데이터를 작은 블록에 담아 분할하고 [Batch Processing],

각 노드에 작은 블록들을 분산시켜 데이터를 저장하는 작업들을 병렬적으로 처리하는 방식은 [Distributed Storage] 

가장 spark 와 비슷한 성격이 있었기 때문에 사용하였습니다.

또한 단순한 feature 간 상관 관계의 파악이 목적이였던 저는 

무거운 딥러닝의 라이브러리인 tensorflow, keras 등을 사용할 이유는 없었습니다.

다만 aws ec2 와 같은 클라우드 환경에서 다중 노드들을 사용하는 클러스터를 구성했다면,

훨씬 더 좋은 성능을 기대할 수 있었다는 점이

로컬 환경, 단일 클러스터에서 인스턴스를 조절하는 방식으로 진행하여 그 효과가 두드러지지 않았다는 점은 아쉽습니다. 
