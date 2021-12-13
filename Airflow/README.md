# Airflow
- Apache Airflow에 기능을 추가하는 플러그인을 만듬
- Airflow 및 다양한 실행기와 함께 Docker 사용
- DAG, 운영자, 작업, 워크플로 등과 같은 핵심 기능 마스터
- XCOM, 분기 및 SubDAG와 같은 Apache Airflow의 고급 개념을 이해하고 적용
- Sequential, Local 및 Celery Executor의 차이점, 작동 방식 및 사용 방법
- Hive, PostgreSQL, Elasticsearch 등의 빅 데이터 에코시스템에서 Apache Airflow를 사용
- Apache Airflow 설치 및 구성
- Airflow를 사용하여 실제 데이터 처리 문제에 대한 솔루션을 생각하고, 답변하고, 구현

# Airflow
- 적절한 시간에 작업을 실행할 수 있도록 하는 오케스트레이터, 올바른 방법으로 올바른 순서로
- 장점
  - python에서 인용된 것처럼 실제로 동적, python에서 할 수 있는 모든 것을 데이터 파이프라인에서 할 수 있음
  - 확장성, 병렬로 원하는 만큼의 작업을 실행 
  - UI, 사용자 인터페이스 , 데이터 문제를 모니터링 
  - 확장가능성, 필요한 만큼 사용자 지정 가능 
- 구성요소
  - 웹 서버, 사용자 인터페이스를 제공하는 Unicon이 있는 서버 
  - Scheduler
  - Metastore
  - Executer, 작업이 실행되는 방법을 정의
  - Worker,  실제로 작업이 실행되는 프로세스
- DAG
- Operator
- Task / Task Instance
- Workflow

# code
```shell
- ssh remote 설치
- vscode terminal : ssh -p 2222 airflow@localhost 입력 후 password airflow입력
- F1 >> remote-ssh >> Connect to host and choose localhost >>  ssh -p 2222 airflow@localhost >>  들어가서 Linux 선택 >>  password airflow >> SSH:localhost 연결 
```  
