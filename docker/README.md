# Docker 개요
- 가상화 : 컴퓨터에서 컴퓨터 리소스(CPU, 메모리, 저장장치, 네트워크 등)의 추상화를 일컫는 광범위한 용어
![image](https://user-images.githubusercontent.com/47103479/145204108-4185f8c9-2283-4d2e-825d-45f67ed182da.png)

  - 서버 가상화
    - 서버는 구체적이고 복잡한 작업을 실행하도록 설계된 강력한 머신
  - 앱 및 데스크톱 가상화
    -  가상 앱 및 데스크톱은 IT 부서가 시뮬레이션된 수백 개의 앱 및 데스크톱을 각 컴퓨터에 설치할 필요 없이 사용자에게 배포할 수 있는 중앙 성버 
  - 네트워크 가상화
  - 클라우드 컴퓨팅 : 인터넷을 통해 공유 컴퓨팅 리소스, 소프트웨어 또는 데이터를 제공하는 방식(가상화는 클라우드 컴퓨팅을 가능하게 하는 주요 기술중 하나) 
- 가상화 응용
  - 서버 통합, 재해 복구, 테스트 및 단력, 휴대 응용, 휴대 작업 공간 , 하드웨어 가상화 기술 
- 클라우드 컴퓨팅
  - 클라우드(인터넷)을 통해 가상화된 컴퓨터의 시스템 리소스(IT 리소스)를 제공
  - 인터넷 기반 컴퓨팅의 일종, 정보를 자신의 컴퓨터가 아닌 인터넷에 연결된 다른 컴퓨터로 처리하는 기술
  - 구성 가능한 컴퓨팅 자원(컴퓨터 네트워크, 서버, 스토리지, 애플리케이션, 서비스)에 대해 어디서나 접근이 가능한, 주문형 접근을 가능케하는 모델 
  ![image](https://user-images.githubusercontent.com/47103479/145204955-9d3b89c7-8718-4234-8b25-874e118b585e.png)

- 컨테이너 기술 
  - 가상화는 단일 하드웨어 시스템에서 여러 운영 체제(윈도우 또는 리눅스)가 동시에 실행
  - 컨테이너는 동일한 운영 체제 커널을 공유하고 시스템의 나머지 부분으로부터 애플리케이션 프로세스 격리 
  ![image](https://user-images.githubusercontent.com/47103479/145205305-08187a56-a23a-43d1-ab5b-c22706221ea1.png)
  
  - 런타임 인스턴스, 애플리케이션과 그 구동환경을 격리한 공간
  - 경량, 포터블 실행가능 이미지, 이미지의 런타임 인스턴스
  - 소프트웨어어와 그에 필요한 의존성 모듈들 포함
  - OS수준에서 제공하는 가상화
  - 애플리케이션 구동환경을 가상화하는 기술
  - OS커널이 격리된 사용자공간을 제공하는 서버 가상화 방법
  - 여러 개의 독립된 사용자 공간 인스턴스를 하나의 호스트에서 사용할 수 있음

# 도커 컨테이너
- 도커 컨테이너
  - 소프트웨어를 제어할 수단을 제공 
    - 도커를 이용해서 어플리케이션을 패키징하면 이의 전개와 런타임 문제를 애플리케이션 외부에서 제어할 수 있음
  - 컨테이너는 기저의 운영 체계로부터, 그리고 다른 컨테이너로부터, 단일 애플리케이션과 이의 의존성, 앱 실행에 필수적인 외부 소프트웨어 라이브러리 전체를 격리
  - 시스템 자원을 좀더 효율적으로 이용 가능 (더 적은 메모리, 더 신속하게 시작 및 중지, 호스트 하드웨어에서 훨씬 더 밀도있게 배치)
  - 소프트웨어 전달 주기를 가속(수요에 맞춘 스케일링, 비즈니스가 요구하는 신기능을 추가하는 업데이트를 간단히 할 수 있음)
  - 애플리케이션 이동을 가능하게 함
    - 애플리케이션이 실행해야 하는 모든 것을 캡슐화 하기 때문에 애플리케이션이 환경들 사이에 손쉽게 이동 가능
  - 컨테이너에 의해 좀더 용이해지는 소프트웨어 패턴의 하나는 마이크로서비스
    - 마이크로서비스는 비즈니스 요구에 따라 별개의 팀에 의해 별개의 시케줄 상에서 LOB 앱(a  Line-of-Business App)의 부분들이 개별적으로 확장 수정 서비스되도록 할 수 있음
  - 분리와 조절 기능 제공
  - 이식성을 제공하는 도커 컨테이너(컨테이너 런타임 환경을 지원하는 모든 장치에서 실행)
  - 결합성을 제공하는 도커 컨테이너(여러 컨테이너가 각 조각들을 제공하며 독립적으로 유지,업데이트,교체,수정 가능)
  - 오케스트레이션과 스케일링이 쉬움(컨테이너는 가볍고, 오버헤드가 거의 없음)
  - 가상 머신이 아닌 도커 컨테이너 기반
    - 가상 머신은 운영 체제에서 자신의 인스턴스에서 실행되기 때문에 고수준의 프로세스 분리 기능을 제공 vs 컨테이너는 호스트 운영체제에서 통제된 영역을 사용 
  ![image](https://user-images.githubusercontent.com/47103479/145210300-d840ce08-1bad-4359-92ad-6d6e6e1f441a.png)

- 도커 이미지
  - 이미지 : 컨테이너 실행에 필요한 파일과 설정값 등을 포함하고 있는 것으로 상태값을 가지지 않고 변하지 않음(Immutable)
    - Ubuntu 이미지 : ubuntu를 실행하기 위한 모든 파일을 가지고 있고 MySQL이미지는 debian을 기반으로 MySQL을 실행하는데 필요한 파일과 실행 명령어 , 포트 정보등을 가지고 있음
    - Gitlab 이미지 : centos를 기반으로 ruby,go,database,redis,gitlab source, nginx 드을 가지고 있음
      - 컨테이너를 실행하기 위한 모든 정보를 가지고 있어서 더 이 상 의존성 파일을 컴파일 하고 설치할 필요 없음
      - Doker hub에 등록하거나 Docker Registry 저장소를 직접 만들어 관리 가능 
  - 컨테이너 : 이미지를 실행한 상태라고 볼 수 있고 추가되거나 변하는 값은 컨테이너에 저장됨
    - 같은 이미지에서 여러 개의 컨테이너 생성 가능, 컨테이너가 추가 및 변경되더라도 이미지는 변경되지 않고 그대로 남아있음
  - 도커 : 특정 프로세스를 운영체제의 나머지와 일정 수준 부리해 실행시킬 수 있음
    - 각 애플리케이션과 종속물이 운영체제 리소스의 분리된 세그먼트를 사용하는 방식

- 도커 파일
  - 도커 이미지를 만들기 위한 설정 파일
  - 여러 가지 명령어를 토대로 Docker File을 작성하면 설정된 내용대로 도커 이미지를 만들 수 있음
  - 도커는 이미지를 만들기 위해 Dockerfile이라는 이미지 빌드용 DSLDomain Specific Language파일을 사용함 
  - 단순 텍스트 파일로 일반적으로 소스와 함께 관리 
  ![image](https://user-images.githubusercontent.com/47103479/145211007-f3f095b1-0cc6-4543-92fc-2f2ceeb45bf6.png)
  ![image](https://user-images.githubusercontent.com/47103479/145211273-dc70802b-b1d5-4248-ba2f-9922ef58cf97.png)

- 도커 VM

  ![image](https://user-images.githubusercontent.com/47103479/145211529-bc8662bf-b1db-4b39-87d3-5ae4e0c68bed.png)

# Docker 환경 이해
- Docker Hub : 도커에서 제공하는 기본 이미지 저장소
  - 회원가입만 하면 대용량의 이미지를 무료로 저장할 수 있고 다운로드 트래픽 또한 무료   
![image](https://user-images.githubusercontent.com/47103479/145816826-31ab34ab-402f-42cd-96ed-6b2ad402d16f.png)
  
  - maven repository와 같이 외부에 공개되어 있는 도커 이미지 레포지토리로 docker pull 명령을 이용하여 컨테이너를 로컬에 받아 오거나, Docker image 빌드 시 베이스 이미지 등을 받아오는데 주로 사용됨
  - ![image](https://user-images.githubusercontent.com/47103479/145817063-793107fb-6091-40c5-9d19-585cea9f9491.png)

- Docker Registry
![image](https://user-images.githubusercontent.com/47103479/145817675-e0375e7a-6f1d-4d9c-860b-00e6a4183614.png)
 
  - 도커 허브를 이용하면 Registry 구축 없이 도커 이미지를 저장 배포할 수 있음 -> 비공개적으로 사용되거나, 사설 네트워크 등에서 사용되기 위해서는 내부 서버에 도커 Registry를 구축해야함 
- Docker 사설 Registry 구축  
  - Docker Registry 구축
    - 도커 Registry 또한 도커 이미지로 배포되고 있음
  - Registry 이미지 다운로드
    - docker pull registry 
  - Registry 컨테이너 생성
    - docker run -d -p 5000:5000--restart=always --name registry registry
  - 도커 이미지 저장하기
    - 도커 이미지를 태깅하고 Registry에 추가한다
    - docker pull ubuntu
    - docker image tag ubuntu localhost:5000/myfirstimage
  - 도커 이미지 배포
    - docker pull localhost:5000/myfirstimage
  - Dokcer Registry 삭제
    - 실행중인 Registry를 종료하고, 컨테이너를 삭제하게 됨
    - docker container stop registry && docker container rm -v registry

- 도커 서비스 환경
  - docker-compose : 여러 도커 컨테이너를 통합적으로 관리하는 CLI 프로그램으로 docker를 설치하면 번들로써 제공
  - 컨테이너 기반을 이용하여 단순한 저장공간 컨테이너(볼륨)을 만들어 저장공간을 컨테이너끼리 연결할 수 있으며, 실행한 호스트의 저장공간에도 접근 가능함 
  - Docker는 게스트 OS를 설치하지 않음 -> 호스트와 OS자원을 직접 사용
  - 도커 프로그램에서 다양한 API를 제공하기 때문에 원하는 만큼 자동화가 가능함
  ![image](https://user-images.githubusercontent.com/47103479/145819027-553a9db4-8c58-4d2e-aaab-299593636729.png)

  - 확장성
    - 이미지만 만들어 놓으면 컨테이너만 관리
    - 서비스 이전이나 신규 서버에 서비스 추가 시 docker run 명령어로 처리
    - 개발서버나 테스트서버 운용 간편 
  - 표준성 
    - 도커를 사용하지 않는 경우 ruby, node.js,go,php로 만든 서비스들의 배포방식은 제각각
    - 컨테이너라는 표준으로 서버를 배포하므로 모든 서비스들의 배포과정이 동일 
  - 이미지
    - 이미지에서 컨테이너를 생성하기 때문에 반드시 이미지를 만드는 과정이 필요
    - 이미지를 저장할 곳이 필요 
  - 설정
    - MySQL_PASS =password와 같이 컨테이너를 띄울 때 환경변수를 같이 지정 
    - 하나의 이미지가 환경변수에 따라 동적으로 설정파일을 생성핟로록 만듬
  - 공유자원
    - 컨테이너는 삭제 후 새로 만들면 모든 데이터가 초기화됨
    - 업로드 파일을 외부 스토지와 링크하여 사용하거나 S3같은 별도의 저장소 필요
    - 세션이나 캐시를 파일로 사용 시 memcached나 redis와 같은 외부로 분리 

- 서비스 빌드 및 배포
![image](https://user-images.githubusercontent.com/47103479/145820565-a0a3b78f-4d95-4ecf-b95e-cc63eb26ae7e.png)
![image](https://user-images.githubusercontent.com/47103479/145819926-8fdb86f6-f163-4b4a-9db4-2e32b9934898.png)
![image](https://user-images.githubusercontent.com/47103479/145820062-d0a0adcd-4ee9-4324-8bb3-ec78d0170224.png)
![image](https://user-images.githubusercontent.com/47103479/145820259-bad0b418-93e1-4def-a8e5-04ac1143943e.png)

# Docker 볼륨과 네트워킹
- Docker 볼륨과 데이터 관리
  - 도커는 데이터를 안전하게 존속시킬 수 이쓴 방식으로 volume, bind mounts, tmpfs의 3가지 방식을 제공함
    - 3가지 방식간의 가장 큰 차이점은 데이터가 Doker Host내에서 어디에 존재하느냐의 차이 
  ![image](https://user-images.githubusercontent.com/47103479/146002564-3e7211f4-bcc0-47e1-8c7a-5a8aa7941ba0.png)
  
  - 도커의 이미지로 컨테이너를 생성하면 읽기 전용이라 쓰기가 불가능
  ![image](https://user-images.githubusercontent.com/47103479/146002828-42a4a574-f41e-426f-88f7-cccc0d88cbdf.png)

- 볼륨
  - 도커 컨테이너에 의해 생성되고 사용되는 데이터를 영속하기 위해 선호되는 메커니즘
  - 바인드 마운트는 호스트 머신의 디렉토리 구조에 따라 달라지지만, 볼륨은 도커에 의해 완전히 관리됨
  ![image](https://user-images.githubusercontent.com/47103479/146003476-10526df0-f612-4000-a440-b3be8f53e4d7.png)

- bind mount
  - 도커 초기부터 사용할 수 있었던 방식으로 volume에 비해 기능이 제한적임
  - Host System의 파일 또는 디렉토리가 Container에 Mount됨
  - 매우 효과적이지만 Host Machine의 File System 디렉토리 구조에 의존적임
  - Docker CLI 명령어로 bind mount를 관리할 수 없음 
- tmpfs mount
  - Docker Host 또는 Container내의 디스크 Data가 유지되지 않음
  - 비영구적인 상태 정보나 민감 정보와 같이 Container의 생명주기와 맞춰서 Data를 보존하고자 할 때 사용할 수 있음 

- Docker Network 구조   
![image](https://user-images.githubusercontent.com/47103479/146005583-c2081f13-15bc-4ddf-a357-8b06a3d042ed.png)

  - 리눅스 시스템 기반, 컨테이너는 기본적으로 eth0와 Io 네트워크 인터페이스를 가지고 있음
  - 컨테이너 내부 IP를 순차적으로 할당을 하며 컨테이너가 재시작될때마다 변경될 수 있음
  - 외부와 연결을 해야 할 경우에는 호스트에 veth(=virtual eth)라는 네트워크 인터페이스를 생성하고 컨테이너의 eth와 연결됨
    - veth 인터페이스는 사용자가 직접 생성할 필요 없이 도커엔진에 의해 자동으로 생성됨 
  - Docker의 5가지 네트워크 구현 방식
  ![image](https://user-images.githubusercontent.com/47103479/146006437-eebe2d98-d5bd-452b-b537-aced1635e51b.png)
  ![image](https://user-images.githubusercontent.com/47103479/146006964-0d7bb0f8-18c8-45dd-a3ed-e6b37d697025.png)

# Docker 서비스
- Docker Compose
  - 한번에 여러 개의 container를 통합 관리 및 운용하기 위한 도구
  - 멀티 컨테이너의 동시 운용 시 컨테이너별 별도의 설정들을 간편하게 작업 가능
  - 기본 수행 절차
    ![image](https://user-images.githubusercontent.com/47103479/146376869-8b63c7f1-c3a8-4dd2-a36b-898d087879a0.png)
    
  - 활용
    - 단일 호스트상, 다수의 독립 환경 운용
    - 컴테이너 볼륨의 보존
    - 변경된 컨테이너의 재생성
    - Variables and moving a composition between environments 
  ![image](https://user-images.githubusercontent.com/47103479/146380206-aa3f70f4-3bb4-42de-bb03-ef00e901d42c.png)
  ![image](https://user-images.githubusercontent.com/47103479/146380553-8d11ace1-308c-45ce-8ad5-b3bb70041c8e.png)
  ![image](https://user-images.githubusercontent.com/47103479/146381136-1969b417-d7e6-430b-b1cf-42e975eb0afb.png) 

  - 여러 개의 컨테이너 옵션과 환경을 정의한 파일을 읽어 컨테이너를 순차적으로 생성함
  - Docker Compose의 설정 파일(docker-compose.yml)은 run 명령어 옵션을 그대로 사용할 수 있으며 컨테이너의 의존성, 네트워크, 볼륨, 컨테이너 수 등을 유동적으로 조절할 수 있음
    ![image](https://user-images.githubusercontent.com/47103479/146381699-147ff541-9a83-4d15-b8a2-3938dce1bc9a.png)
 
    - 파이썬 프로그램이 구동되는 컨테이너와 데이터를 저장하는 redis 서버, 웹서버 컨테이너를 실행한다고 할 때, 각각의 run 명령어 및 다양한 옵션으로 컨테이너를 생성하고 테스트하기에는 매우 번거로움 -> Docker Compose를 활용하면 편리함 
  ![image](https://user-images.githubusercontent.com/47103479/146381964-cd50bdaf-00cb-4267-9f90-71946092b7db.png)
  
  - docker-compose.yml 파일 구조    
    - 기타 command, links, external_links, extra_hosts, prots, expose, volumes 등
    ![image](https://user-images.githubusercontent.com/47103479/146382528-42f03a70-d7f2-474d-9fcc-e116434d46da.png)

- Docker Swarm
  - 도커가 공식적으로 만든 오케스트레이션 도구
    - 오케스트레이션 도구 : 여러 호스트 서버의 컨테이너들을 배포 및 관리를 위한 도구
    - 쿠버네티스를 대신할 도커에서 만든 컨테이너 관리를 위한 툴 
  - 여러 개의 도커 호스트를 함께 클러스팅하여 단일 가상 Docker 호스트 생성
  - 호스트 OS에 Agent만 설치하면 간단하게 작동하고 설정이 쉽고 Agent를 외부에 설치하지 않음
  - 컨테이너 오케스트레이션 도구 : Docker Swarm, APACHE MESOS, KUBERNETES 등
  - 오케스트레이션 도구 기능
    - 컨테이너 배포
    - 컨테이너 자동 배치
    - 컨테이너 자동 복제
    - 컨테이너 그룹에 대한 로드밸런싱
    - 컨테이너 장애 복구
    - 클러스터 외부에 서비스 노출
    - 컨테이너 추가 또는 제거를 이요한 확장 및 축소
    - 컨테이너 서비스간의 인터페이스를 통한 연결 및 네트워크 포트 노출 제어 
  - 시스템 구조
    - Master 노드와 Worker 노드로 시스템을 구성
    - Master 노드에서는 클러스터 관리 작업을 하고 클러스터 상태 유지, 스케줄링 서비스 , Swarm HTTP API Endpoint를 제공
    - Worker 노드는 컨테이너를 실행하는 역할
    ![image](https://user-images.githubusercontent.com/47103479/146383286-3cc3c4df-9713-4401-a02f-54fc46c4ef13.png)
  
  - Swarm 클러스터 구축
  ![image](https://user-images.githubusercontent.com/47103479/146383374-629ef432-017a-4a79-9af5-1e7c79bea7a4.png)

  - Swarm을 통한 어플리케이션 배포
  ![image](https://user-images.githubusercontent.com/47103479/146383508-eb76b9ba-c2dd-4edb-bbee-fe456ffe0c30.png)

## Kubernetes(K8s)
- 컨테이너화된 워크로드와 서비스를 관리하기 위한 이식성이 있고, 확장 가능한 오픈소스 플랫폼
- 선언적 구성과 자동화를 모두 용이하게 해줌
- 구글의 15여 년에 걸친 대규모 상용 워크 로드 운영 경험을 기반으로 만들어졌으며 커뮤니티의 최고의 아이디어와 적용 사례가 결합
- 분산시스템을 탄력적으로 실행하기 위한 프레임 워크를 제공함
- 확장 요구 사항, 장애 조치, 배포 패턴 등을 처리함
- Rancher 2.0, OpenShift(Red Hat), Tectonic(CoreOS), Docker Enterprise Edition 등이 쿠버네티스를 기반으로 플랫폼으로 만들어 대세임을 증명하고 있고 AWS, Google Cloud, Azure, Digtial Ocean, IBM Cloud, Oracle Cloud 등에서 관리형(Managed) 서비스를 내놓음으로써 클라우드 컨테이너 시장을 평정 
![image](https://user-images.githubusercontent.com/47103479/146551884-1ed83b38-66fb-450c-8f6b-7b2637a4a373.png)
![image](https://user-images.githubusercontent.com/47103479/146552673-25e4c1a8-396a-420b-bfe8-405c1e40ca66.png)
![image](https://user-images.githubusercontent.com/47103479/146552421-52e36b86-8563-429d-93b8-5c4d2187cc66.png)
![image](https://user-images.githubusercontent.com/47103479/146552544-2c2d8058-82e8-463d-bf9f-e40f7bd162c1.png)

- 쿠버네티스 커뮤니티와 생태계
![image](https://user-images.githubusercontent.com/47103479/146552719-f4fa3aa2-9437-4c40-b419-0df085f590fb.png)

- 다양한 배포 방식
  ![image](https://user-images.githubusercontent.com/47103479/146554079-56176d29-d0fd-40ca-9f06-ec8f1f02b099.png)
 
  - 쿠버네티스는 Deployment, StatefulSets, DaemonSet, Job, CronJob등 다양한 배포 방식을 지원 
    - Deployment : 새로운 버전의 애플리케이션을 다양한 전략으로 무중단 배포 가능
    - StatefulSets : 실행 순서를 보장하고 호스트 이름과 볼륨을 일정하게 사용할 수 있어 순서나 데이터가 중요한 경우에 사용 가능
    - DaemonSet : 로그나 모니터링 등 모든 노드에 설치가 필요한 경우에 이용
    - Job, CronJob :  배치성 작업 

- 클라우드 지원
![image](https://user-images.githubusercontent.com/47103479/146553230-dc94323f-f561-432b-b24e-ba01b635c861.png)

  - 쿠버네티스는 부하에 따라 자동으로 서버를 늘리는 기능(AutoScaling)이 있고 IP를 할당받아 로드밸런스(LoadBalancer)로 사용가능하며 외부 스토리지를 컨테이너 내부 디렉토리에 마운트하여 사용하는 것도 가능
  - 쿠버네티스는 Cloud Controller를 이용하여 클라우드 연동을 손쉽게 확장할 수 있음
  - 수십 개의 클라우드 업체에서 모듈을 제공하여 관리자는 동일한 설정 파일을 서로 다른 클라우드에서 동일하게 사용 가능함 

- 아키텍쳐
![image](https://user-images.githubusercontent.com/47103479/146553458-b1379fc7-2a33-4e4a-a448-3d4700d7fc3b.png)
![image](https://user-images.githubusercontent.com/47103479/146553683-2e167506-6981-47bd-82c3-09558eaca75d.png)
![image](https://user-images.githubusercontent.com/47103479/146553860-06f63db4-8eae-4ef5-807c-d5317dfa21d4.png)

## Jenkins
![image](https://user-images.githubusercontent.com/47103479/146554285-b18a6ec3-75d7-4f32-9e68-b5b62f6c4f2f.png)
![image](https://user-images.githubusercontent.com/47103479/146554477-7508b955-d909-4a64-8d65-9c2ef159063a.png)
![image](https://user-images.githubusercontent.com/47103479/146554693-cee94a71-b283-4cb7-92c7-f41ce6b867e9.png)
![image](https://user-images.githubusercontent.com/47103479/146555123-bd7fee9c-de16-46a0-adcb-024a932b52aa.png)

# 도커모티너링
- ELK(ElasticSearch, Logstash, Kibana) Stack
![image](https://user-images.githubusercontent.com/47103479/146641301-616a2179-8961-4a99-9ad1-ccc6e293e916.png)
   
   - 분석 및 저장 기능을 담당하는 ElasticSearch
   - 수집 기능을 하는 Logstash
   - 시각화 하는 도구인 Kibana
   - ELK는 접근성과 용이성이 좋아 최근 가장 핫한 Log 및 데이터 분석 도구

## ElasticSearch
![image](https://user-images.githubusercontent.com/47103479/146641361-79753403-72d2-4f3d-be54-6f8f71f02602.png)

  - Lucene 기반으로 개발한 분산 검색엔진
  - JSON 기반의 분산형 검색 및 분석 엔진
  - Logstash를 통해 수신된 데이터를 저장소에 저장하는 역할
  - 데이터를 중심부에 저장하여 예상되는 항목을 검색하고 예상치 못한 항목 검출 가능
  - 정형, 비정형, 위치정보, 메트릭 등 원하는 방법으로 다양한 유형의 검색을 수행하고 결합 가능 
  - 데이터를 중심부에 저장하여 예상되는 항목을 검색하고 예상치 못한 항목 검출 
  ![image](https://user-images.githubusercontent.com/47103479/146641434-34bddb23-f603-438f-b018-4bf376a60152.png)
  ![image](https://user-images.githubusercontent.com/47103479/146641567-190dc2b4-bd23-4afe-a63e-85c09db13801.png)
  ![image](https://user-images.githubusercontent.com/47103479/146641595-e47c7004-3088-4646-a462-4ad9c5d18172.png)

## Logstash
- 확장형 플러그인 에코시스템으로 구성된 동적 데이터 수집 파이프라인
- 오픈소스 서버 기반 데이터 처리 파이프라인
- 다양한 데이터 소스에서 동시에 데이터를 수집하고 변환하여 stash 보관소 전달
- 수집할 로그를 선정해서, 지정된 대상 서버(ElasticSearch)에 인덱싱하여 전송하는 역할을 담당하는 소프트웨어
![image](https://user-images.githubusercontent.com/47103479/146641708-af970226-fe89-4727-9a66-1a819f7666d7.png)

- filter : Logstash 파이프라인의 중간 처리 장치
![image](https://user-images.githubusercontent.com/47103479/146641763-a9244e1f-45ec-470b-bb14-592766651a74.png)

- output : Logstash파이프 라인의 최종 단계
![image](https://user-images.githubusercontent.com/47103479/146641828-d328276a-b1f1-48f4-a6d8-41938398bd47.png)

- codec
  - 입력 또는 출력의 일부로 작동 할 수 있는 스트림 필터
  - 인기 코덱에는 json, msgpack, plain

## Kibana
![image](https://user-images.githubusercontent.com/47103479/146641915-537e824e-f0da-4dcc-bf96-3bd175b0395e.png)

- 확장형 사용자 인터페이스, 데이터를 구체적으로 시각화
- 데이터를 시각적으로 탐색하고 실시간으로 분석 가능(ElasticSearch)
- 시각화를 담당하는 HTML + Javascript 엔진

## Docker ELK
- Docker 설치
![image](https://user-images.githubusercontent.com/47103479/146642264-eea7de85-de5b-418c-a7f0-6a3d6376f1f8.png)

- Docker Compose 설치
![image](https://user-images.githubusercontent.com/47103479/146642098-83bf55ab-842d-41c0-9975-5f245911aa4b.png)

- docker-elk 레포지토리 클론 
![image](https://user-images.githubusercontent.com/47103479/146642155-31c4eec7-5d26-433f-b656-ef9d499f03b2.png)

# Docker 오케스트레이션
## Rancher
- 멀티 호스트에서 컨테이너를 실행하고 관리하기 위한 오픈소스 소프트웨어 플랫폼
- Docker와 Kubernetes를 운영하고 관리
- 컨테이너의 생명주기를 관리하는 기능
- Rancher하나로 Docker 컨테이너를 관리하는데 필요한 전체 소프트웨어 스택 구출 가능 
![image](https://user-images.githubusercontent.com/47103479/146676436-ac430d6b-5884-45d7-8dd1-e514a844ecfa.png)

- Rancher 소프트웨어의 네 가지 구성요소
  - Infra Orchestration
    - Rancher는 Linux 호스트 형태로 원시 컴퓨팅 리소스를 가져옴
    - 각 Linux 호스트는 가상 시스템 또는 물리적 시스템이 될 수 있음
    - Rancher는 각 호스트의 CPU, Memory, Disk Storage, Network Connection 이외에 다른 것들은 예측하지 않음
    - Rancher관점에서는 VM instacnce인지 bare metal 서버인지 구분하지 않음 
  - Container Orchestration and scheduling
    - 컨테이너화된 응용 프로그램을 실행하도록 선택함
    - Rancher는 Docker Swarm, Kubernetes, Mesos를 포함한 모든 인기 있는 컨테이너 오케스트레이션 프레임워크를 이용해서 컨테이너를 배포함, 이외에도 Cattle이라는 컨테이너 오케스트레이션 및 스케쥴링 프레임워크를 지원함
    - Rancher는 Swarm, Kubernetes 및 Mesos 클러스터를 설정, 관리 및 업그레이드 하는 게 광범위하게 사용됨
    - 사용자는 여러 개의 스웜 또는 Kubernetes 클러스터를 만들 수 있으며, 이들 오케스트레이션 프레임워크의 고유기능을 이용해서 응용 프로그램들을 관리 할 수 있음
  - Application Catalog
    - Rancher는 실행해야 할 컨테이너의 정보가 담겨 있는 Application Catalog를 관리함
    - Rancher 사용자는 버튼을 한번 클릭하는 것으로 간단하게 어플리케이션을 실행할 수 있음
    - 자주 사용하는 어플리케이션을 카탈로그 형태로 등록할 수 도있음
    - 등록된 어플리케이션은 자동으로 실행되고 업그레드 됨
    - 이미 다양한 종류의 어플리케이션 카탈로그들이 존재함 
  - Enterprise-grade control
    - Active Directory, LDAP, Github 등의 인증시스템 그리고 Rancher에서 제공하는 RBAC(Role-Based Access Control)을 이용해서, 유저와 그룹의 권한을 설정할 수 있음

- 환경 구성 
  - 3개의 노드 , 두 개 노드에는 Rancher Agent가 설치, 한 노드에는 Rancher Server가 설치 
  ![image](https://user-images.githubusercontent.com/47103479/146676526-667ce02a-1ac3-4c3f-a04c-0eb29b46884e.png)
  ![image](https://user-images.githubusercontent.com/47103479/146676566-211867aa-24c3-451d-8f5e-8cb5caf22401.png)

- 설치
  ![image](https://user-images.githubusercontent.com/47103479/146676672-d1e7c46b-ef1f-4dcc-929d-410a10458eb5.png)
  ![image](https://user-images.githubusercontent.com/47103479/146676675-719d82b6-2d5b-49c5-98c1-512ff8ffc14e.png)

- 멀티 컨테이너 관리
![image](https://user-images.githubusercontent.com/47103479/146676766-ad838a1d-a864-46f9-b053-6c27e1d45e5f.png)
![image](https://user-images.githubusercontent.com/47103479/146676930-2e49dabd-1f17-4695-8135-d7de668155cd.png)
![image](https://user-images.githubusercontent.com/47103479/146676826-c53dadb5-69eb-44d1-8c2c-4b49c3cd82c1.png)
![image](https://user-images.githubusercontent.com/47103479/146676840-1fa21b35-1a98-48b6-ab2e-dedf75a354c5.png)

# AWS 기반 Docker 서비스 구축 
- Docker는 애플리케이션을 신속하게 구축, 테스트 및 배포할 수 있는 소프트웨어 플랫폼
- Docker는 소프트웨어를 컨테이너라는 표준화된 유닛으로 패키징하여, 이 컨테이너에는 라이브러리, 시스템 도구, 코드 , 런타임 등 소프트웨어를 실행하는 데 필요한 모든 것이 포함 
- Dokcer를 사용하면 환경에 구애 받지 않고 애플리케이션을 신속하게 배포 및 확장할 수 있으며 코드가 문제없이 실행될 것임을 확신 
- AWS에서 Docker를 실행하면 개발자와 관리자가 어떠한 규모에서든 매우 안정적이며 저렴한 방식으로 애플리케이션을 구축, 제공 및 실행 가능 
- AWS에서는 두 가지 Docker 라이선싱 모델, 즉 오픈 소스 Dokcer Community Edition(CE)과 구독 기반의 Docker Enterprise Edition(EE) 둘다 지원 

## Docker 작동 방식
- Docker는 코드를 실행하는 표준 방식을 제공
- Docker는 컨테이너를 위한 운영 체제
- 가상머신이 서버 하드웨어를 가상화하는 방식과 비슷하게(직접 관리해야하는 필요성 제거) 컨테이너는 서버 운영 체제를 가상화
- Docker는 각 서버에 설치되며 컨테이너를 구축, 시작 또는 중단하는데 사용할 수 있는 간단한 명령을 제공
- AWS Fargate, Amazon ECS, Amazon EKS 및 AWS Batchn와 같은 AWS 서비스를 사용하면 Docker 컨테이너를 대규모로 실행하고 관리 가능  
- Docker를 사용해야 하는 이유
  - Docker를 사용하면 코드를 더 빨리 전달하고, 애플리케이션 운영을 표준화하고, 코드를 원할하게 이동하고, 리소스 사용률을 높여 비용을 절감
  - Docker를 사용하면 어디서나 안정적으로 실행할 수 있는 단일 객체를 확보
  - Docker의 간단한 구문을 사용해 완벽하게 제어
  - 더 많은 소프트웨어를 더 빨리 제공
  - 운영 표준화 : 작은 커에티너식 애플리케이션을 사용하면 손쉽게 배포하고, 문제를 파악하고, 수정을 위해 롤백
  - 원활하게 이전 : Docker 기반 애플리케이션을 로컬 개발 시스템에서 AWS의 프로덕션 배포로 원활하게 이전 
  - Dokcer 컨테이너를 최신 애플리케이션 및 플랫폼을 생성하는 핵심 빌딩 블록으로 사용
  - Docker에서는 손윕게 분산 마이크로 서비스 아키텍처를 구축 및 실행
  - 표준화된 지속적 통합 및 지속적 전달 파이프라인을 통해 코드를 배포
  - 고도로 확장 가능한 데이터 처리 시스템을 구축
  - 개발자를 위한 완전 관리형 플랫폼을 생성 가능
  - 서비스로서의 컨테이너 : 안전한 IT 관리형 인프라와 콘텐츠로 분산 애플리케이션을 구축 및 제공 

## AWS에서 Docker 실행
- AWS는 Docekr 오픈 소스 및 상용 솔루션 모두에 대한 지원을 제공
- Amazon Elastic Container Service(ECS)는 고도로 확장 가능하고 성능이 뛰어난 컨테이너 관리 서비스
- AWS Fargate는 인프라를 배포하거나 서버를 프로비저닝하거나 관리하지 않고도 프로덕션에서 컨테이너를 실행할 수 있도록 지원하는 Amazon ECS를 위한 기술
- Amazon Elastic Container Service for Kubernetes(EKS)를 사용하면 손쉽게 aws에서 Kubernetes를 실행 
- Amazon Elastic Container Registry(ECR)는 Docker 컨테이너 이미지를 손쉽게 저장하고 관리할 수 있도록 지원하는 안전한 고가용성 프라이빗 컨테이너 레지스트리로서, 빠르게 가져오고 보호하기 위해 저장 이미지를 암호화하고 압축
- AWS Batch를 사용하면 Docker 컨테이너를 사용하여 고도로 확장 가능한 배치 처리 워크로드를 실행 

## AWS Docker 구축
- Docker 컨테이너 배포
  - Amazon Elastic Container Service(ECS)는 확장 가능한 클러스터에서 Docker 애플리케이션을 실행하는 데 사용하는 Amazon Web Services
  ![image](https://user-images.githubusercontent.com/47103479/146772054-a1d0ca94-6d2d-4f44-82f3-dd3953f082eb.png)
  ![image](https://user-images.githubusercontent.com/47103479/146772786-25aaaa6b-8e57-4d9c-b720-14e6e27e2b76.png)
  ![image](https://user-images.githubusercontent.com/47103479/146773047-bf3b04da-7ff1-47d3-9977-2955e6cf4e78.png)









