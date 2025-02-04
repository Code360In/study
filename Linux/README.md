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

## man
- man [모르는 커맨드]
![image](https://user-images.githubusercontent.com/47103479/148059251-efee27f3-97d6-46d0-aa03-d7b4274c13ef.png)

  - 1. 섹션, 매뉴얼 이름 : DATE(1)에서 1은 공식 매뉴얼의 전체 내용 중 몇 번째 섹션에 해당하는 곳인지를 말함. 대부분의 유닉스 계열의 운영체제는 아래와 같은 여러 섹션으로 구성된 공식 메뉴얼을 갖고 있음
  - 2. NAME : 커맨드의 이름과 커맨드에 대한 간단한 설명
  - 3. SYNOPSIS : 어떻게 커맨드를 실행할 수 있는지, 사용 가능한 형식(인자, 옵션들의 조합)을 보여줍니다. 지금 보면 대괄호 안에 있는 것들(-jRu)이 사용 가능한 옵션을 나타냄, 대괄호 없는 new_date 같은 것이 인자
  - 4. DESCRIPTION : 커맨드에 대한 좀더 자세한 설명과 각 옵션에 대한 설명

## 디렉토리와 파일
![image](https://user-images.githubusercontent.com/47103479/148059550-2aff96f8-cc20-4bee-a222-0f9f6e5041d4.png)

- 틸드(Tilde) : ~ 현재 사용자의 홈 디렉토리 
- pwd(print the name of working directory) : 현재 작업중인 워킹 디렉토리 
- cd(change directory) : 디렉토리를 변경 

- 절대 경로
  - 루트 디렉토리를 기준으로 어떤 파일이나 디렉토리가 가지고 있는 고유한 경로 (/Users/js/Document)
- 상대 경로
  - 나의 현재 위치를 기준으로 나타낸 경로(./Documnet)
![image](https://user-images.githubusercontent.com/47103479/148065863-51d80497-39b7-4580-9dd2-f8c96ee1557f.png)
![image](https://user-images.githubusercontent.com/47103479/148631918-6867bef4-3964-4818-a3cd-20a20e90a4ad.png)
![image](https://user-images.githubusercontent.com/47103479/148631919-e83ab5f3-0f65-4408-af83-c0ba9c833ffd.png)
![image](https://user-images.githubusercontent.com/47103479/148631921-34203435-cc7d-40e5-b110-882b10ff797b.png)
![image](https://user-images.githubusercontent.com/47103479/148631923-beec8e0f-dd57-48f9-946d-0bf167cfc51b.png)

# Vim(vi improved)
- Vim 공식 사용 설명서(https://vimhelp.org/#help.txt)
- Vim을 게임처럼 재미있게 배울 수 있는 사이트(https://vim-adventures.com/)
![image](https://user-images.githubusercontent.com/47103479/148631915-8094e46e-a9f4-4c4d-865b-9bc7fba11ecb.png)

- 원래 있던 vi라는 텍스트 에디터 프로그램의 더 향상된(improved) 버전
- 일반 모드(Normal Mode)
- 입력 모드(Insert Mode)
- 비주얼 모드(Visual Mode) :v(한칸씩) , V(줄단위로 블록지정할때)
- 명령 모드(Command Mode)
![image](https://user-images.githubusercontent.com/47103479/148630550-a95b622c-bb19-476b-8ba6-9ee4ccaa3095.png)
![image](https://user-images.githubusercontent.com/47103479/148630592-ec6cb36a-feb3-4dd3-bf62-4c4b6dae8a6d.png)

```shell
$ i : 입력모드로 전환 
$ esc : 일반모드
$ a : 커서를 한 칸 뒤로 옮기고 입력 모드로 전환 
$ I : insert, 커서를 첫 번째 칸으로 옮기고 입력모드로 전환 
$ A : 커서를 맨 마지막 카능로 옮기고 입력 모드로 전환 
$ o : open, 커서를 다음 줄로 옮기고 입력 모드로 전환
$ O : 커서 위에 빈 줄이 생기고 입력 모드로 전환 
$ : : 명령 모드로 전환 
$ w [파일이름] : write, 저장하기 
$ q : quit, 나가기 
$ ! : 강제 실행 
$ /[텍스트] : 명령 모드로 전환 ,텍스트 검색 
$ n : next, 다음 검색 내용으로 이동(N : 역방향 탐색)
$ s/[텍스트]/[바꿀텍스트] : subtitute, 텍스트 대체
$ % : 범위를 파일 전체로 
$ g : global, 문장에 등장하는 모든 단어 변경 
$ c : confirm, 확인 
  - $ :%s/!/#/g : 모든 !를 #으로 바꿈
  - $ :%s/!/#/gc : 사용자가 바꿀걸 하나하나 확인해가면서 바꿈 y/n  
$ ctrl + g : 내 커서의 위치를 알려줌 
$ 0(숫자) : 커서가 줄의 첫 번째 칸으로 이동 
$ $ : 커서가 줄의 마지막 칸으로 이동 
$ gg : 파일의 맨 처음으로 이동
$ G : 파일의 맨 마지막으로 이동 
$ x : 텍스트 한 칸씩 삭제 
  - 숫자 + x : 원하는 만큼 삭제
$ dd : 문장 삭제하기 
$ u : undo , 이전 작업 취소 
$ y : yank, 복사하기 
$ p : paste, 커서 다음 칸에 붙여넣기(P : 커서 이전 칸에 붙여넣기) 
$ d : delete, 삭제하기 
$ dd : 한 줄을 통째로 삭제 
```
5k : 위로 5줄
![image](https://user-images.githubusercontent.com/47103479/148631607-3c8a6fe8-6cdb-4053-9504-95960e2a90e8.png)

- sudo :  sudo 라고 쓴 이유는 시스템에 프로그램을 설치할 때는 일반 사용자가 아닌 그보다 더 높은 관리자 권한이 필요하기 때문
  - 외부 프로그램 설치가 그런 작업 중 대표적인 예인 거구요. 사실 이 부분을 더 잘 알려면 유닉스에서 사용자 권한(permission)이라고 하는 부분
  - 관리자 계정으로서의 권한을 갖고 어떤 작업을 해야할 때 sudo 를 가장 맨 앞에 써줘야 한다는 사실

# code
```shell
$ clear : 터미널 화면을 깔끔하게
$ date : 날짜 출력
$ cal  : 달력 출력
$ sudo apt install ncal : 라이브러리 설치 
$ man cal : 공식문서 help (스페이스바 or 아래화살표)
$ cd / : 루트 디렉토리로 감 
$ cd ~ : 홈 디렉토리(cd /Users/js) 
$ cd - : 바로 직전에 있는 경로로 이동 
$ ls : 현재 자식 디레토리에 있는 모든 걸 보여줌
$ ls - l(long listing format) : 결과를 긴 리스트 형식으로 보여줌 
$ ls -a(all) : 숨겨져 있는 자식 디렉토리나 파일을 볼 수 있음,(숨겨져있는설정파일들)
$ ls -a -l, ls-al : 숨겨져+자세한것들 
$ ls -d(directory) : 디렉토리 자체의 정보 , 특정 디렉토리나 파일의 정보 -> ls 커맨드의 인자 , 디렉토리 자체의 정보 -> -d 옵션
$ mkidr [폴더명] : 디렉토리 만들기(make directroy)
  - mkidr 'dev programming' : 공백이 있는 디렉토리나 파일이름 사용시 작은따옴표 사용 
$ touch [파일명] : 파일 만들기 
$ mv [파일명] [옮길장소]  : 디렉토리나 파일을 옮김(move)
$ mv [파일명] [바꿀이름] : 디렉토리나 파일의 이름을 변경
$ cp [원본파일] [복사할파일] : copy $ paste 복사&붙여넣기(-i옵션, -r 옵션)
  - -i 옵션 : interactive : 상호 작용하는 사용자에게 확인 받기 
  - -r 옵션 : 디렉토리 복사-붙여넣기할때 recursive, 재귀적, 자신이 자신을 반복적으로 호출
$ rm [삭제파일] : remove 디렉토리와 파일 삭제 (-r 옵션)
$ rm -r -i [삭제파일] : 삭제 꿀팁 
$ cat [파일명] : concatenate, 이어 붙이다, 파일들의 내용을 이어서 출력 , 봐야 할 내용이 단순할 때
$ less [파일명] : 한 화면에 하나의 파일을 보여줌 , 봐야할 내용이 많거나 하나씩 봐야할 때 
  - :n (next 다음 파일로 이동) , :p (previous 이전 파일로 이동) 
  - 화살표로 이동, space(한줄단위로이동), b(위로 한 페이지 이동) G(가장 마지막으로 이동) g(가장 처음으로 이동) q(quit)
$ head -n 20 [파일명] : 파일의 맨 앞부분을 보여줌(옵션 n, 20줄 출력)
$ tail [파일명] : 파일의 맨 뒷부분을 출력(default 10)
$ history : 사용한 커맨드의 내역을 보여줌 
  - ![history내 사용할 해당번호 123] : history 상에서 커맨드 실행 
$ ctrl + a : 커서가 맨 앞으로 이동 
$ ctrl + e : 커서가 맨 뒤로 이동 
$ VIM
```

![image](https://user-images.githubusercontent.com/47103479/147945114-1752f7a4-6856-4024-b301-b8fd0f0ffecd.png)
![image](https://user-images.githubusercontent.com/47103479/147945144-2d183139-0432-4fcf-bff4-969ad8d2220c.png)
![image](https://user-images.githubusercontent.com/47103479/148065444-6d22eaae-2315-44a9-8b0b-5109a3232ae2.png)
![image](https://user-images.githubusercontent.com/47103479/148065480-2667c8e8-03af-4155-921a-cc885ce22d8a.png)
![image](https://user-images.githubusercontent.com/47103479/148065787-0a7412b3-803e-4520-83d7-36dbd46a7ac6.png)
![image](https://user-images.githubusercontent.com/47103479/148227789-face1068-a720-4922-9bec-ef146c648ecb.png)
![image](https://user-images.githubusercontent.com/47103479/148228606-135f5489-07f2-4de2-bb0b-90ba6a443ec9.png)
