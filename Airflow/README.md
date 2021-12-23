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

# remote ssh
- https://gist.github.com/marclamberti/742efaef5b2d94f44666b0aec020be7c#file-airflow-version
![image](https://user-images.githubusercontent.com/47103479/147244229-61ad9044-fffe-402c-b410-75122c25a2ae.png)

- $ airflow db init 
  - code ex) airflow db upgrade / airflow db reset 
![image](https://user-images.githubusercontent.com/47103479/147244857-cade75be-6496-4aa0-bfea-7aa036bacb6b.png)

- $ airflow webserver
![image](https://user-images.githubusercontent.com/47103479/147245186-57b6a9e9-f9c0-4b6b-9eea-4b5f0b1ece6d.png)
![image](https://user-images.githubusercontent.com/47103479/147245442-ba5d08ee-ff4f-4664-b4d8-a156723f65dc.png)
![image](https://user-images.githubusercontent.com/47103479/147245497-073f14f0-eb45-4b6a-873a-9578b2cf2c07.png)
![image](https://user-images.githubusercontent.com/47103479/147245577-8a4d8ac5-2810-453d-8f9b-7fa6880df52a.png)
![image](https://user-images.githubusercontent.com/47103479/147245669-2eeef081-15f1-4a45-8bb0-1aee01fdf73a.png)
![image](https://user-images.githubusercontent.com/47103479/147245857-f91b57a8-f579-481f-9827-6e3eb7e6314a.png)

## new bash
![image](https://user-images.githubusercontent.com/47103479/147247512-5e9da46b-9c62-412f-ab83-2c94380541d8.png)
![image](https://user-images.githubusercontent.com/47103479/147248748-4cadd3f0-3726-42c7-9b04-5861121c3988.png)
![image](https://user-images.githubusercontent.com/47103479/147248858-0d1cde13-a6b2-461c-8ee8-ba788a51f740.png)
![image](https://user-images.githubusercontent.com/47103479/147249064-716ee5e5-562e-4bd6-9bd6-75d4aa9e3afa.png)

