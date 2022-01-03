# 리눅스
-  GUI(Graphical User Interface)  <-> 리눅스 CLI(Command-Line Interface)
-  GUI
  -  한 화면에 많은 정보를 담을 수 있음, 눈으로 보고 대상을 선택 가능, 윈도우 바탕화면
- CLI
  -  눈에 보이는 거라곤 고작 터미널 하나

![image](https://user-images.githubusercontent.com/47103479/136699359-95bb718f-9a5b-48fa-b9f7-f946683d33f9.png)

```
- ls : list의 약자
- ls -al : a - 숨긴 파일 불러오기  
- ls -alt : 시간 순으로 보여주기 
- alias : 지정해놓은 약자 표기 
- mv(move) test 123 :  이동 또는 이름 바꾸기 
- mkdir(make diretory) tt : 디렉토리 생성 
- touch 파일명 : 파일 생성
- cd(change diretory)
- cd .. : 상위 폴더 
- cd - : 이전 풀더로 가기
- cp(copy) 123 456 -> ls : 복사 
- pwd : 절대적인 경로
- rm(remove) : 삭제 
- rm -i 456 : i라는 명령어 같이쓰면 지우기전 다시 물어봐줌 
- clear  : 지우기
- top  : cpu 보는법
- htop : cpu 깔끔하게 보는법 
- q : 종료 
- ps(process) : 얼마나 돌아가는지 , 현재 실행하는 프로그래밍 자체를 확인 
- df : 디스크 도는거 다 보여줌 
- du : 몇 바이트씩 가지고 있는지, 디스크 용량 확인 
- find : 현재 풀더에서 들어있는 모든 폴더 검색 
- find | grep confing : grep을 통해서 위치를 찾아 
- man(manual) + 명령어 : 메뉴얼 help 알려줌 
- which ls : 위치가 어딨는지
- tail : 선택한 파일의 실시간 트래킹 끝에만 보여줌 
- apt-get : 필요한 패키지, 프로그램을 설치 할 수 있는 패키지 관리 도구
- nohup : 내 스크립트가 터미널을 끄더라도 계속 실행시키고 싶을 때 & 와 함께 백그라운드로 실행
- screen(tmux) : nohup을 통해 백그라운드로 가버린 프로세스는 다시 볼 수 없지만 Screen을 띄워서 실행하면, 해당 세션을 다시 복원할 수 있음 
```

## 쉘 스크립트
- 셔뱅, #!{인터프리터 위치} : 셀 스크립트 시작할 때 맨 처음에 기입 
- vl ss_test 
- bash ss_test
- which bash 
- chmod 755 ss_test 

# 유닉스 커맨드 라인 
## CLI 환경과 유닉스
- 유닉스(Unix-certified)와 유사 유닉스(Unix-like)
![image](https://user-images.githubusercontent.com/47103479/147937170-66e0c221-de22-4a4a-b344-fdac88a6e188.png)
![image](https://user-images.githubusercontent.com/47103479/147937214-4f8f4cee-7fc8-4f2b-8219-cfa529d6e59b.png)

- BSD(Berkerly Software Distribution)운영 체제
  - BSD는 리눅스보다도 더 이전에 탄생한 운영 체제
  - 오늘날의 macOS는 Unix - BSD - NeXTStep - macOS 순의 역사를 거쳐 탄생한 것

## 인자 옵션
- 인자는 커맨드가 작동할 대상을 지정하기 위해 사용
  - 인자(커맨드 동작 대상자 지정) cal 2030 / cal 3 2030
- 옵션은 커맨드가 구체적으로 어떤 방식으로 동작할지를 지시하기 위해 사용
  - 옵션(커맨드의 구체적인 동작 방식 지정) : cal -y , 


## 우부투 설치
- 필수 설치 
  - Oracle VM VirtualBox
  - 우분투(https://ubuntu.com/download/desktop)
  - 우분투 가상 환경 만든뒤에 컨트롤러:IDE에 다운받은 우분투 경로 설정 후 start 한뒤에 옵션 설정 
![image](https://user-images.githubusercontent.com/47103479/147939476-bbb871af-af31-4ef8-bd66-c5ad1c724d66.png)
![image](https://user-images.githubusercontent.com/47103479/147943962-92d73dc2-cd62-4c0d-823b-f8203e281e57.png)

# code
```shell
$ clear
$ date
$ cal 
$ sudo apt install ncal
```

![image](https://user-images.githubusercontent.com/47103479/147945114-1752f7a4-6856-4024-b301-b8fd0f0ffecd.png)
![image](https://user-images.githubusercontent.com/47103479/147945144-2d183139-0432-4fcf-bff4-969ad8d2220c.png)
