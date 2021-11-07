# Spark
# 스파크 
- 빅데이터 애플리케이션 개발에 필요한 통합 플랫폼을 제공
- 간단한 데이터 읽기에서부터 SQL처리, 머신러닝 그리고 스트림 처리에 이르기까지 다양한 데이터 분석 작업을 같은 연산 엔진과 일관성 있는 API로 수행
- 클라우드 기반의 애저 스토리지, 아마존 S3, 분산 파일 시스템인 아파치 하둡, 키/값 저장소인 아파치 카산드라, 메시지 전달 서비스인 아파치 카프카등의 저장소 지원
- 빅데이터 애플리케이션에 필요한 대부분의 기능을 지원 
  - 실시간 데이터 처리 기능(Spark Streaming)
  - 스파크SQL : SQL과 구조화된 데이터를 제공
  - MLlib : 머신러닝 지원
  - GraphX : 스트림 처리 기능을 제공하는 스파크 스트리밍과 새롭게 선보인 구조적 스트리밍 그리고 그래프 분석 엔진
- 인메모리 기반의 대용량 데이터 고속 처리 엔진
- 아파치 스파크는 오픈 소스 범용 분산 클러스터 컴퓨팅 프레임워크
- 아파치 스파크는 범용적이면서도 빠른 속도로 작업을 수행할수 있도록 설계한 클러스터용 플랫폼이자 스트림 처리를 효과적으로 수행하는 인-메모리 방식의 분산 처리 시스템
- 최초 데이터 로드와 최종 결과 저장시에만 디스크 사용 

# 하둡과 비교
- 스파크 메모리 내 데이터 고속 처리 엔젠은 특정 상황, 스테이지 간 다중 스테이지 작업과 비교 시 맵리듀스에 비해 최대 100배 더 빠름
- 아파치 스파크 API는 맵리듀스와 다른 아파치 하둡 구성 요소에 비해 개발자 친화적 API를 제공하여 분산 처리 엔진의 복잡성 대부분을 간단한 메서드를 처리
- 아파치 스파크의 중심은 컴퓨팅 크러스터로 분할 가능한 불변적 객체 컬렉션을 나타내는 프로그래밍 추상화, 즉 탄력적 분산 데이터 집합(RDD) 개념
- 스파크 SQL은 구조적 데이터 처리에 초점을 두며,R과 python에서 차용한 데이터 프레임을 사용
- 스파크 SQL은 표준 SQL 지원 외에 기본적으로 지원되는 JSON, HDFS, 아파치 하이브, JDBC, 아파치 ORC, 아파치 파케이를 포함한 다른 데이터 저장소에서 읽기와 쓰기를 위한 표준 인터페이스도 제공

# 스파크 구조
- Spark Core
  - 메모리 기반의 분산 클러스터 컴퓨팅 환경
  - 스파크 전체의 기초가 되는 기초 분산 작업 처리
  - 장애복구, 네트워킹, 보안, 스케쥴링 및 데이터 셔플링 등 기본 기능을 제공 
- Spark SQL
  - 대규 분산 정형 데이터 처리
  - JSON 파일, Parquet 파일, RDB 테이블, 하이브 테이블 등 다양한 데이터 읽기 및 쓰기 가능
- Spark Streamin
  - 실시간 스트리밍 데이터를 처리하는 프레임워크
  - HDFS, 아파치 카프카, 아파치 플럼, 트위터, ZeroMQ 와 더블어 커스텀 리소스 사용 가능 
 - Spark MLlib
  - 머신러닝 알고리즘 라이브러리
  - RDD 또는 DataFrame의 데이터셋을 변환하는 머신 러닝 모델을 구현
- Spark GraphX
  - 그래프 장점과 두 정점을 잇는 간선으로 구성된 데이터 구조
  - 그래프 RDD(EdgeRDD 및 VertexRDD) 형태의 그래프 구조를 만들 수 있는 기능을 제공
  - 그래프 데이터는 Vertex와 Edge로 구성 
- 동작 구조
  - Driver Program : SparkContext와 RDD 생성, Transformation과 Action을 실행
    - SparkContext : 어떻게 클러스터에 접근할 수 있는지 알려주는 Object, Worker Node내 Executor 간 통신이 발생 
  - Cluster Manager : 클러스터에 1개 존재, 스케쥴링 담당, 여러 대의 서버로 구성된 클러스터 환경에서 다수의 Application이 함께 구동될 수 있게 Application간의 CPU나 메모리, 디스크와 같은 전반적인 컴퓨팅 자원 관리
    - Standalone : 스파크가 독립적으로 작동할 수 있음
    - YARN : 하둡의 리소스 매니저 (하둡과 스파크는 상호 독립적)
    - Mesos : 분산 커널 시스템
    - Kubernetes
  - Worker Node
    - 실제 작업을 수행하는 노드
    - Executor 
      - 주어진 스파크 작업의 개별 테스크들을 실행하는 작업실행 프로세스
      - 애플리케이션을 구성하는 작업을 실행 -> 드라이버에 결과를 전송
      - 사용자 프로그램에서 캐시하는 RDD를 저장하기 위한 메모리 저장소 제공 
    - Task : executor에 할당 되는 작업의 단위 
 - RDD의 연산
  - Transformation : RDD에서 새로운 RDD를 생성하는 함수
  - action : RDD에서 RDD가 아닌 타입의 data로 변환하는 함수들 
  - Partition

- Spark 설치 및 환경설정
  - 대량의 데이터를 고속 병렬분산처리
  - 스토리지 I/O와 네트워크 I/O를 최소화하도록 처리
  - 동일한 데이터에 대한 변환처리가 연속으로 이루어지는 경우와 머신러닝처럼 결과셋을 여러 번 반복해  처리 고속화
  - 한 대의 노드로 처리할 수 있는 용량보다 더 큰 데이터셋에 대해 시행착오가 가능한 환경 제공
  - 배치처리, 스트림처리,  SQL처리와 같은 서로 다른 형태의 애플리케이션을 하나의 환경에 통합하여 사용 가능 

- PySpark
  - 스파크의 메인 추상화는 RDD
  - apache spark를 파이썬에서 실행하기 위한 api
  - SparkContext를 생성하는 것으로 시작 

# Apache spark RDD 프로그래밍 
- RDD Operation
  - 스파크 내부에서 존재하는 분산 데이터에 대한 모델, 기본 데이터 구조
  - 분산된 변경불가 자바 객체 컬렉션
  - RDD는 읽기 전용으로 분할된 레코드의 모음
  - 클러스터의 노드들 간에 파티션된 엘리먼트의 컬렉션들이며 파티션이 분산처리 단위
  - RDD, DataFrame, Dataset 
- transformation
  - filter, map, flatmap, zip, rdeuceByKey, join 
- action : RDD의 요소들을 이용해 어떤 결과값을 얻어내는 연산 
- Partion : 하나의 RDD는 여러 개의 파티션으로 나뉘어짐, 
- Lineage : RDD 연산의 순서를 기록 
- Shared Variables(공유 변수) : 함수가 Spark오퍼레이션에 전달되면(map 혹은 리듀스) 원격자의 클러스터 노드에서 수행 
  - Broadcast Variables : 각 노드에 캐싱된 읽기전용 변수를 보관하게 하기 위해서 사용 
  - Accumulators : 병렬로 효과적으로 제공, 변수들이며 이는 연관된 오퍼레이션들을 통해서 추가 

# SparkSQL
- 스파크의 기본 데이터 모델은 RDD
  - 장점 : 분산환경에서 메모리 기반으로 빠르고 안정적으로 동작하는 프로그램을 작성
  - 단점 : 스키마에 대한 푠현 방법이 없다
- 스파크 SQL 주요 기능
  - DataFrame 추상화 클래스 제공
  - 다양한 구조적 데이터 포맷의 읽기 및 쓰기 가능(JSON, Hive, Parquet 등)
  - 내부 JDBC/ODBC나 외부 Tableau(태블루) 같은 BI 툴 등으로 스파크 SQL을 통해 SQL로 데이터 질의 가능
  - 데이터셋으로부터 조건에 맞는 데이터추출하기
  - JSON의 키와 테이블의 컬럼 등, 특정한 이름으로 데이터 추출하기
  - 복수의 데이터셋 결합
  - 그룹 단위로 집약
  - 다른 형식의 구조화된 데이터셋으로 변환하기
- SchemaRDD
  - Row 객체의 RDD
  - 각 아이템은 Record를 의미
  - RDD에서 제공하지 않는 Operation도 제공 
- DataFrame
- DataSet
  - DataFrame은 Dataset[Row]로 간주, Dataset의 subset이며, Row는 유형이 지정되지 않는 JVM 객체 
  - 필요한 이유: DataFrame과 RDD간의 데이터 타입을 다루는 방식의 차이 
  - 기본 연산 : 데이터 저장 옵션 조정 및 스키마 조회 
    - createOrReplaceTempView(viewName:String)  : Unit-viewName 이름으로 로컬 임시 view
    - explain(): Unit- 디버깅 목적으로 실행계획을 출력
  - 액션 연산
    - show() - DataSet의 정보를 표 형태로 표시
    - head() - 첫 번째 row 로드
    - take(n:Int): Array[T] - DataSet에서 n개의 row를 로드 
  - 트랜스포메이션 연산
    - select() : DataFrame 지정된 컬럼들을 가져옴
    - filter - SQL 표현식 또는 row 조건으로 데이터 필터링
    - agg : 특정 컬럼에 대해 sum(), max()와 같은 집합 연산을 수행
    - intersect : 두 개의 DataSet에 모두 속하는 row로만 구성된 DataSet을 생성 
- Spark SQL JDBC 연동 
  - MySQL(또는 MariaDB)와 스칼라를 연결

# Spark Streamling 
-  실시간으로 들어오는 데이터를 처리하기 위한 모듈
-  다양한 소스로부터 실시간 스트리밍 데이터 처리
-  ![image](https://user-images.githubusercontent.com/47103479/140648845-01175fcd-eca5-4fde-93ff-7b61489c465a.png)

- 배치 처리 : 데이터를 축적하다가 일정 주기마다 일괄적으로 처리하는 방식
  - Spark Streaming의 전체적인 흐름은 리시버가 데이터를 입력 받은 후 마이크로 배치라 불리는 기법으로 데이터를 연산한 뒤 트랜스포메이션을 통해 데이터를 전송
  - ![image](https://user-images.githubusercontent.com/47103479/140648904-ef4543eb-5161-4d83-8324-e7cf903ab175.png)
  - ![image](https://user-images.githubusercontent.com/47103479/140649010-c1801fcf-643c-4c67-8649-335b8ccdcadc.png)

- DStream(Discretized Streams) 
  - 불연속적인 스트림을 의미
  - 끊임없이 생성되는 데이터를 보여주기 위한 추상모델
  - 스파크 스트리밍은 입력받은 데이터를 작은 그룹들로 그룹핑
  - 새로운 배치들은 정해진 간격마다 만들어지며, 작동되는 동안 받은 데이터를 계속 추가 
  - 설정한 배치 주기별로 데이터를 묶어서 하나의 배치 생성(생성된 배치는 하나의 RDD)
  - 데이터는 연속적으로 입력되므로 RDD 역시 연속적으로 생성되며, 이렇게 순차적으로 생성된 RDD의 흐름이 DStream
  - ![image](https://user-images.githubusercontent.com/47103479/140649093-4fb57243-fabe-412e-90c5-1f7075a1b824.png)

- Structured Streaming
  - Spark SQL 엔진 위에 구축된 Stream Processing Framework
  - Sturctured Steraming은 기존에 Spark APIs(DataFrames, Datasets, SQL) 등의 Structured API를 이용하여 End-to-End Streaming Application을 손쉽게 생성
  - SparkSession으로 생성되고 처리할 때 중복 데이터를 관리하기 위하여 time stamp를 도입
  - DStream을 사용하지 않고 새로운 데이터 row 단위로 계속해서 추가
  - DataFrame을 통해 streaming 으로 들어오는 데이터를 질의하거나 집계하거나 변형하는 작업등이 가능 

# Apache Spark MLlib
