# Git(버전관리)
- 버전 관리와 동시 협업 능력, 다른 컴퓨터에 작업물 보내기(백업본)
- 목표
  * 빠른 속도 
  * 단순한 디자인
  * 비선형적 개발 지원(수천 개의 브랜치를 병행할 수 있음, 브랜치가 뭔지는 나중 챕터에서 배웁니다.)
  * 완전 분산형 시스템  
  * 리눅스와 같은 거대한 프로젝트도 속도 저하의 문제없이 관리할 수 있는 시스템

- 작업 영역 
  - working directory(working tree) : 작업을 하는 프로젝트 디렉토리를
  - staging area(index) : git add를 한 파일들이 존재하는 영역
  - repository : working directory의 변경 이력들이 저장되어 있는 영역

- 상태
  - Untracked 상태 : 파일이 Git에 의해서 그 변동사항이 전혀 추적되고 있지 않는 상태
  - Tracked 상태 : 파일이 Git에 의해 그 변동사항이 추적되고 있는 상태
    - Staged 상태 : 파일의 내용이 수정되고나서, staging area에 올라와있는 상태를 Staged(스테이징된, stage area에 올려진) 상태
    - Unmodified 상태 : 현재 파일의 내용이 최신 커밋의 모습과 비교했을 때 전혀 바뀐 게 없는 상태면 그 파일은 Unmodified(수정되지 않은, 변한 게 없는) 상태
    - Modified 상태 : 최신 커밋의 모습과 비교했을 때 조금이라도 바뀐 내용이 있는 상태면 그 파일은 Modified(수정된) 상태  
  ![image](https://user-images.githubusercontent.com/47103479/136045401-d754cf5e-0c43-4fd5-9597-7b4cb2a26254.png)

    - Add the file : Untracked 상태의 파일을 처음으로 git add 해주면 Staged 상태
    - Edit the file : 최신 커밋과 비교했을 때 차이가 없는 Unmodified 상태의 파일의 내용을 수정하면 Modified 상태
    - Stage the file : Modified 상태의 파일을 git add 해주면 Staged 상태
    - Remove the file : 파일을 삭제하면 당연히 Git에서 더이상 인식하지 않음
    - Commit : 커밋을 하면 staging area에 있던 파일들이 커밋에 반영되고, 이제 모든 파일들은 최신 커밋과 차이가 없게 되니까 Unmodified 상태



- 레포지토리 
  - 커밋이 저장되는 곳 
  - 프로젝트 디렉토리 버전 관리 , 버전별 프로젝트 모습, 버전별 변경 사항에 대한 설명 .git 디렉토리
- commit 
  - 프로젝트 디렉토리의 특정 모습을 하나의 버전으로 남기는 행위 & 결과물 
  - 하나의 버전에 담기는 동작을 커밋한다. 사진처럼 저장 
  - 주의사항 
    - 사용자의 이름과 이메일 주소 설정
    - 커밋 메세지 남기기(옵션 -m)
    - 커밋할 파일을 git add로 지정해주기 
   
  ![image](https://user-images.githubusercontent.com/47103479/136030609-77c5a72b-00ec-4db3-84ef-c977549b1f1c.png)
  ![image](https://user-images.githubusercontent.com/47103479/136030784-f3edb24b-1ec9-47b5-a837-8e05d4177661.png)
  ![image](https://user-images.githubusercontent.com/47103479/136031993-078b9250-d5ee-425b-95b3-5f6e40784f3c.png)
  ![image](https://user-images.githubusercontent.com/47103479/136044607-b12e3881-9699-4236-8d38-c72495e2d54e.png)

## git code
```git
- $ git init : 현재 디렉토리를 Git이 관리하는 프로젝트 디렉토리(=working directory)로 설정하고 그 안에 레포지토리(.git 디렉토리) 생성
- $ git config user.name 'codeit' : 현재 사용자의 아이디를 'codeit'으로 설정(커밋할 때 필요한 정보)
- $ git config user.email 'teacher@codeit.kr' : 현재 사용자의 이메일 주소를 'teacher@codeit.kr'로 설정(커밋할 때 필요한 정보)
- $ git add [파일 이름] : 수정사항이 있는 특정 파일을 staging area에 올리기
- $ git add [디렉토리명] : 해당 디렉토리 내에서 수정사항이 있는 모든 파일들을 staging area에 올리기 
- $ git add . : working directory 내의 수정사항이 있는 모든 파일들을 staging area에 올리기
- $ git reset [파일 이름] : staging area에 올렸던 파일 다시 내리기
- $ git status : Git이 현재 인식하고 있는 프로젝트 관련 내용들 출력(문제 상황이 발생했을 때 현재 상태를 파악하기 위해 활용하면 좋음) 
- $ git commit -m "커밋 메시지" : 현재 staging area에 있는 것들 커밋으로 남기기
- $ git help [커맨드 이름] : 사용법이 궁금한 Git 커맨드의 공식 메뉴얼 내용 출력
``` 
## cmd code
- cd .. 앞으로 이동 

# GitHub(원격 저장소)
