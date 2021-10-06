# git code
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
- $ git push -u origin master : 로컬 레포지토리의 내용을 처음으로 리모트 레포지토리에 올릴 때 사용
- $ git push : 로컬 레포지토리의 내용을 리모트 레포지토리에 보내기 
- $ git pull : 리모트 레포지토리의 내용을 로컬 레포지토리로 가져오기
- $ git clone [프로젝트의 GitHub 상 주소] : GitHub에 있는 프로젝트를 내 컴퓨터로 가져오기
- $ git config alias.history 'log --pretty=oneline' : alias 로 git history라고만 써도 git log --pretty=oneline을 실행
- $ git reset [옵션] [커밋 아이디](git reset --hard 7f3d) , git reset --hard HEAD^(바로 이전 커밋), git reset --hard HEAD~2(2단계 전에 있는 커밋)
- $ git tag [태그 이름] [커밋 아이디] : 태그달기 
- $ git tag : 태그 조회 , git show [태그 이름] : 태그와 연결된 커밋 확인 
- $ git log : 커밋 히스토리를 출력
- $ git log --pretty=oneline : --pretty 옵션을 사용하면 커밋 히스토리를 다양한 방식으로 출력 --pretty 옵션에 oneline이라는 값을 주면 커밋 하나당 한 줄씩 출력
- $ git show [커밋 아이디] : 특정 커밋에서 어떤 변경사항이 있었는지 확인
- $ git commit --amend : 최신 커밋을 다시 수정해서 새로운 커밋으로 만듦
- $ git config alias.[별명] [커맨드] : 길이가 긴 커맨드에 별명을 붙여서 이후로 별명으로 해당 커맨드를 실행할 수 있도록 설정
- $ git diff [커밋 A의 아이디] [커밋 B의 아이디] : 두 커밋 간의 차이 비교
- $ git reset [옵션] [커밋 아이디] : 옵션에 따라 하는 작업이 달라짐(옵션을 생략하면 --mixed 옵션이 적용됨) 
		(1) HEAD가 특정 커밋을 가리키도록 이동시킴(--soft는 여기까지 수행)
		(2) staging area도 특정 커밋처럼 리셋(--mixed는 여기까지 수행)
		(3) working directory도 특정 커밋처럼 리셋(--hard는 여기까지 수행)
		그리고 이때 커밋 아이디 대신 HEAD의 위치를 기준으로 한 표기법(예 : HEAD^, HEAD~3)을 사용해도 됨
- $ git tag [태그 이름] [커밋 아이디] : 특정 커밋에 태그를 붙임

``` 

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

## cmd code
- cd .. 앞으로 이동 

# GitHub(원격 저장소)
- 원격 레포지토리(리모트 레포지토리) : 깃허브의 레포지토리
- 로컬 레포지토리 : 내 컴퓨터의 레포지토리 
- $ git remote add origin https://github.com/mjs1995/Math_box.git
- $ git push -u origin master
- 로컬 레포지토리에서 리모트 레포지토리로 푸시하는 방법 

![image](https://user-images.githubusercontent.com/47103479/136201251-e0d15094-9de3-4270-8837-a44a341a2d81.png)

- 깃허브가 최신일 경우 

![image](https://user-images.githubusercontent.com/47103479/136201785-469f2c87-34b8-4593-a469-c78f2c03c610.png)

- 깃허브에 collaborator 지정

![image](https://user-images.githubusercontent.com/47103479/136202235-a9b9902d-809f-48b0-9722-66710b2c2c65.png)

- 깃허브에 다른사람 리포지토리 가져오기 

![image](https://user-images.githubusercontent.com/47103479/136202662-594e846d-8110-47e4-bbd0-bc4e62a5e303.png)

# 커밋
- 히스토리 : 커밋의 아이디로 구분 아래로 갈수록 old
- oneline : 한줄만 보여주기

![image](https://user-images.githubusercontent.com/47103479/136203719-bfd2026b-b444-4bfc-bfb6-26f5c821c694.png)
![image](https://user-images.githubusercontent.com/47103479/136204158-2de048fb-1307-4a14-8f64-0966cfe2592c.png)

- 옵션 다르게 보여주는 방법 : 바뀌면 i눌러서 글쓰기 / ESC 누른다음 :wq 엔터

![image](https://user-images.githubusercontent.com/47103479/136204733-2398c645-abf3-418b-a3ed-dc29ca6b6a99.png)
![image](https://user-images.githubusercontent.com/47103479/136204533-19671d34-d3f0-4496-a849-8aaa963abab0.png)

- 최신 커밋 수정 : $ git commit --amend

![image](https://user-images.githubusercontent.com/47103479/136205182-d310c887-03e3-4b98-99ec-94fa4ee9fb4d.png)

- 커밋 메시지 작성 가이드라인
   - 커밋 메시지의 제목과 상세 설명 사이에는 한 줄을 비워두기
   - 커밋 메시지의 제목 뒤에 온점(.)을 붙이지 않기
   - 커밋 메시지의 제목의 첫 번째 알파벳은 대문자로 작성
   - 커밋 메시지의 제목은 명령조로 작성(Fix it / Fixed it / Fixes it)
   - 커밋의 상세 내용에는 이런 걸 적으면 좋음
     - 왜 커밋을 했는지
     - 어떤 문제가 있었고
     - 적용한 해결책이 어떤 효과를 가지는지
   - 다른 사람들이 자신의 코드를 바로 이해할 수 있다고 가정하지 말고 최대한 친절하게 작성

- 커밋 가이드라인
  - 하나의 커밋에는 하나의 수정사항, 하나의 이슈(issue)를 해결한 내용만 남기기
  - 현재 프로젝트 디렉토리의 상태가 그 내부의 전체 코드를 실행했을 때 에러가 발생하지 않는 상태인 경우에만 커밋
 
 - 두 커미 사이의 변화 : git diff 
 - HEAD : 가장 최근에 한 커밋을 가리킴 
 - git reset : 과거 커밋으로 돌아가고 싶을때
   - --mixed : HEAD가 특정 커밋을 가리키도록 함, staging area를 특정 커밋의 모습처럼 리셋함, working directory는 건드리지 않고 git reset 하기 이전 상태 그대로 둠
   - --hard : HEAD가 특정 커밋을 가리키도록 함, staging area도 특정 커밋의 모습처럼 리셋함, working directory도 특정 커밋의 모습처럼 리셋함
     
 ![image](https://user-images.githubusercontent.com/47103479/136215840-953144a1-c2db-4cf8-a31a-fae490158135.png)
 ![image](https://user-images.githubusercontent.com/47103479/136216251-b6e6ae82-1f88-428c-b597-1d3d92b77105.png)

