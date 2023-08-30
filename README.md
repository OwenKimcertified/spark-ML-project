# 업데이트 중

<img src = 'https://drive.google.com/uc?id=19lFF-9KWhRBQxNTB2wOHf0U7YK9t8w7f' width = 800 height = 800>
<img src = 'https://drive.google.com/uc?id=1cqgTl-pDVcuAUSRnsMXn-OJvJP3UeZwx' width = 800 height = 200>

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

로컬 환경에서만 진행하여 그 효과가 두드러지지 않았다는 점은 아쉽습니다. 
