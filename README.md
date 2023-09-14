# SPARK - ML 
# FEATURE - TARGET Corelations
![image](https://github.com/OwenKimcertified/spark-ML-toy/assets/99598620/666d697a-8b02-454e-ad5f-50b7cd0e1965)
![image](https://github.com/OwenKimcertified/spark-ML-toy/assets/99598620/bc26db0f-94d7-4462-8bbf-799babc53e63)
![image](https://github.com/OwenKimcertified/spark-ML-toy/assets/99598620/30063ca2-2af4-49f1-8d28-6bb879c23d4b)
![image](https://github.com/OwenKimcertified/spark-ML-toy/assets/99598620/bebcd813-a7b3-4d99-902d-7aae2a8512da)
# setting
- ubuntu 22.04 LTS

- Hadoop 3.3.4

- spark 3.3.3

- docker - zookeeper3.7, kafdrop(obsidian_dynamics), kafka7.0
# 프로젝트 회고
처음 시작은 TLC TRIP DATA 를 가지고 데이터 분석 공부에 초점을 두고 

sql 쿼리 작성, EDA 등을 공부하려 했는데 분석하면 할 수록 재밌어져

이동 거리에 따라 요금을 예측해보는 Regression 을 구성해보았습니다. 

목표는 r2_score 가 0.7 이상만 나오게 끔 구성하는 것이였고, 성공했습니다.

spark - ml 을 사용한 이유는 hdfs 에 저장되는 파일들은 높은 확률로 

대용량 데이터이고 그 대용량 데이터들을 분산 처리 후 저장했기 때문입니다.

hdfs 에 데이터를 저장할 때부터 큰 데이터를 작은 블록에 담아 분할하고 [Batch Processing],

각 노드에 작은 블록들을 분산시켜 데이터를 저장하는 작업들을 병렬적으로 처리하는 방식은 [Distributed Storage] 

가장 spark 와 비슷한 성격이 있었기 때문에 사용하였습니다.

또한 단순한 feature 간 상관 관계의 파악이 목적이였던 저는 무거운 딥러닝의 라이브러리인

tensorflow, keras 등을 사용할 이유는 없었습니다. 무엇보다 hadoop 과 cluster 의 호환이 좋아서 사용한 것도 있습니다.

아쉬운 점은 aws ec2 와 같은 클라우드 환경에서 다중 노드들을 사용하는 클러스터를 구성했다면,

더 많은 양의 데이터를 저장하고 학습하는 효과를 기대할 수 있었다는 점이 

로컬 환경, 단일 클러스터에서 인스턴스를 조절하는 방식으로 진행하여 그 효과가 두드러지지 않았다는 점은 아쉽습니다. 
