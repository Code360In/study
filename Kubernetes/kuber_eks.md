# 쿠버네티스 구성 요소
![image](https://user-images.githubusercontent.com/47103479/135873903-5f7ee9a6-c835-42ab-8bd3-361f3f0769a0.png)
![image](https://user-images.githubusercontent.com/47103479/135873913-76e7bd76-9dae-4fda-975b-d15112be55c8.png)
![image](https://user-images.githubusercontent.com/47103479/135874035-f8052710-e3f7-4422-9907-6bb5bbbcc1c1.png)

## 네이티브 쿠버네티스 구성 요소 
- AWS_EKS 
![image](https://user-images.githubusercontent.com/47103479/135874233-208b429f-d70d-4a76-87c5-0cb845859ca8.png)

- Azure_AKS
![image](https://user-images.githubusercontent.com/47103479/135874448-10275429-db50-4b52-9e0f-fcac3a0ce035.png)

- GCP_GKE
![image](https://user-images.githubusercontent.com/47103479/135874558-21a20457-5c83-4d84-af28-e34fbfd41f28.png)

## 쿠버네티스 기본 철학
- 마이크로서비스 아키텍처
  * 하는일이 분할
  * cf] 모놀리식 아키텍처 (하나의 사람이 다 하는거)
![image](https://user-images.githubusercontent.com/47103479/135875036-0aa0ca8c-1cda-4b01-bd19-43801a1a6307.png)

- 선언적인 구조 , 각 시스템의 값만 갖고 있고 각 할일들만 함, 각자의 역할에 맡게 고유의 일만 함 
- 일을 계속 추적해서 계속 맞춤 
![image](https://user-images.githubusercontent.com/47103479/135875975-87a30553-272d-4ccc-9e23-4ddfc22efe80.png)
- API 서버 모든것의 중심, 중요한 요소 

# 쿠버네티스 에러 디버깅
## 배포된 파드가 문제가 생겼을때
- 파드만 배포된 경우 
  * 이 경우 문제,, 단일 파드이므로 
- 디플로우먼트로 생선된 파드의 경우 
  * 파드가 지워지면 다시 만들면 돼 , 지정해준 숫자만큼 생성되기로 되어있음
  * ![image](https://user-images.githubusercontent.com/47103479/135876949-933d8388-900f-44da-9bf2-467c3f522058.png)

## 워커 노드의 구성 요소에 문제가 생겼다면
- Kubelet 에 문제가 생겼을 때
- 컨테이너 런타임에 문제가 생겼을때(docker) - systemctl stop docker

## 마스터 노드의 구성 요소에 문제가 생겼을 때 
- 스케줄러 삭제했을 때  
  * kubectl get pods -n kube-system
  * kubectl get pods -n kube-system -o wide
  * kubectl delete pod kube-scheduler-m-k8s -n kube-system
- kubelet이 멈췄을때 
  * systemctl stop kubelet
  * kubectl delete pod kube-scheduler-m-k8s -n kube-system
- 컨테이너런타임이 멈췄을때 
  * systemctl stop docker
  * curl 172.16.132.32
  * systemctl status docker # 도커 상태 확인

## 쿠버네티스 오브젝트
- 쿠버네티스의 기본 오브젝트 
- 네임스페이스 
![image](https://user-images.githubusercontent.com/47103479/136144386-8222cc8d-5884-443d-9079-8dc931026620.png)

- 볼륨 : 영속적인 데이터를 보존하기 위해 
![image](https://user-images.githubusercontent.com/47103479/136144589-91da0a7b-a4fd-425a-9690-43b4008571ac.png)
![image](https://user-images.githubusercontent.com/47103479/136144761-220eb8dc-f286-4945-a469-62b83dc0fa98.png)

- Pod : 자유롭게 생성하고 삭제 가능 
``` kube
- kubectl edit deployment del-deploy
- :wq 저장하고 나가기
```

## 쿠버네티스 팁 
- kubectl <tab> <tab> (k <tab> <tab>)
- alias
 
## 쿠버네티스 업그레이드
![image](https://user-images.githubusercontent.com/47103479/136145525-cd0ccedb-5514-4e50-8472-e37a7dda2a26.png)
