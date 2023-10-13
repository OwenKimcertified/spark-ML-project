# SPARK - ML - PROJECT : FEATURE - TARGET Corelations 

# 정비 중

# 프로젝트 회고
TLC TRIP DATA 로 데이터 분석 공부에 초점을 두고 spark 로 쿼리 작성, EDA 등을 공부하다 보니 



운행 시간, 이동 거리 등을 feature 와 target 으로 설정하여 요금을 예측해보는 Regression 을 구성해보았습니다. 

목표는 r2_score 가 0.7 이상만 나오게 끔 구성하는 것이였고, 성공했습니다.

단순한 feature 간 상관 관계의 파악이 목적이였던 저는 무거운 

딥러닝의 라이브러리인 tensorflow, keras 등을 사용할 이유가 없었고 . 

아쉬운 점은 aws ec2 와 같은 클라우드 환경에서 다중 노드들을 사용하는 클러스터를 구성했다면,

더 많은 양의 데이터를 저장하고 학습하는 효과를 기대할 수 있었다는 점이 

로컬 환경, 단일 클러스터에서 인스턴스를 조절하는 방식으로 진행하여 

그 효과가 두드러지지 않았다는 점은 아쉽습니다. 

# PPT
![슬라이드2](https://github.com/OwenKimcertified/spark-ML-project/assets/99598620/42ceb696-c7e9-4c09-b39f-e95a4203b8ec)
![슬라이드3](https://github.com/OwenKimcertified/spark-ML-project/assets/99598620/4ca8c99c-c35b-418f-9591-f296290b0a95)
![슬라이드4](https://github.com/OwenKimcertified/spark-ML-project/assets/99598620/92952b1d-5c24-4e7b-978d-6d23ae4d68a4)
![슬라이드5](https://github.com/OwenKimcertified/spark-ML-project/assets/99598620/668b5515-d4de-400b-9210-0a54f271d749)

# setting
- ubuntu 22.04 LTS

- openjdk 8

- Hadoop 3.3.4

- spark 3.3.3

- docker - zookeeper3.7, kafdrop(obsidian_dynamics), kafka7.0
