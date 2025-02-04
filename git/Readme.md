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
- $ git push --set-upstream origin premium : 로컬 레포지토리의 내용을 맨 처음 리모트 레포지토리에 보낼 때
- $ git branch [새 브랜치 이름] : 새로운 브랜치를 생성
- $ git checkout -b [새 브랜치 이름] : 새로운 브랜치를 생성하고 그 브랜치로 바로 이동
- $ git branch -d [기존 브랜치 이름] : 브랜치 삭제
- $ git checkout [기존 브랜치 이름] : 그 브랜치로 이동
- $ git merge [기존 브랜치 이름] : 현재 브랜치에 다른 브랜치를 머지
- $ git merge --abort : 머지를 하다가 conflict가 발생했을 때, 일단은 머지 작업을 취소하고 이전 상태로 돌아감
- $ git fetch : 로컬 레포지토리에서 현재 HEAD가 가리키는 브랜치의 업스트림(upstream) 브랜치로부터 최신 커밋들을 가져옴(가져오기만 한다는 점에서, 가져와서 머지까지 하는 git pull과는 차이가 있음)
- $ git blame : 특정 파일의 내용 한줄한줄이 어떤 커밋에 의해 생긴 것인지 출력 
- $ git revert : 특정 커밋에서 이루어진 작업을 되돌리는(취소하는) 커밋을 새로 생성
- $ git stash  : 작업 내용 저장
- $ git stash list : 작업 내용 조회(=스택 살펴보기)
- $ git stash apply [작업 내용의 아이디] : 작업 내용 적용 
- $ git stash drop [작업 내용의 아이디] : 작업 내용 제거 
- $ git stash pop [작업 내용의 아이디] : 작업 내용을 적용하면서 동시에 스택에서도 제거
- $ git cherry-pick [작업 내용의 아이디] : 원하는 작업이 있는 커밋의 내용만 가져올 수 있는 커맨드 
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

# 브랜치
- 하나의 코드 흐름
- 마스터 브랜치 : 레포지토리를 만들고 커밋을 하면 자동으로 생기는 브랜치(기본 브랜치)

![image](https://user-images.githubusercontent.com/47103479/136790568-e39ce9f9-a5ae-483a-976e-31eced9185f9.png)
![image](https://user-images.githubusercontent.com/47103479/136790692-23a83280-4cce-41e3-8704-9ca9f42235ef.png)
![image](https://user-images.githubusercontent.com/47103479/136790997-ad85a78c-d72b-4de6-9b5d-233203511f19.png)
- git remote add origin https://github.com/kyuri-dev/Math_Box.git
	- remote : 리모트 레포지토리에 관한 작업을 할 때 쓰는 커맨드
	- add : 새로운 리모트 레포지토리등록
	- url을 origin이라는 이름으로 등록 
- git push -u origin master
	- 현재 로컬 레포지토리에 있는 master 브랜치의 내용(=master 브랜치와 관계된 모든 커밋들)을 origin이라는 리모트 레포지토리로 보냄
	- -u는 --set-upstream 
- git push origin master:master 
	-  master:master에서 더 먼저 나오는 master는 로컬 레포지토리의 master 브랜치(~에서)/더 뒤에 나오는 master는 리모트 레포지토리의 master 브랜치(~으로)를 나타냄 

- HEAD(어떤 커밋 하나를 가리킴) -> 어떤 커밋을 가리키는존재 (branch를 가르켜) 
- branch(하나의 코드 관리 흐름)->어떤 커밋을 가르키는 존재(포인터)
![image](https://user-images.githubusercontent.com/47103479/136795311-6b99213a-8913-4ab2-b2ec-5c335230e370.png)

-git reset [--hard 또는 --soft 또는 --mixed] 9033 
	- HEAD는 여전히 같은 브랜치를 가리키고, HEAD가 가리키는 브랜치가 다른 특정 커밋을 가리키게 됨
	- 이 때문에 결국 HEAD가 간접적으로 가리키던 커밋도 바뀌게 됨
	- 과거의 커밋으로 git reset을 한다고 그 이후의 커밋들이 삭제되는 게 절대 아니고 계속 남아있음
	- git reset은 과거의 커밋뿐만 아니라 현재 HEAD가 가리키는 커밋 이후의 커밋으로도 할 수 있음
![image](https://user-images.githubusercontent.com/47103479/136795674-0915022e-b0cb-4fad-b3c1-6f6766ce85eb.png)

- Fast-forward 머지
	- 새로운 커밋이 생기는 게 아니라 단지 브랜치가 이동하게 되는 머지를 Fast-forward 머지
	- Fast-forward는 어떤 영상이나 소리를 빨리감기(앞으로 감기)한다는 뜻으로 지금 master 브랜치가 더 최신 커밋으로 이동
- 3-way 머지 
	-  base때의 내용과 비교했을 때 달라진 부분이 있는 것이 우선시
	-  두 브랜치에서 둘다 변화가 일어났을 때는 Conflict를 발생시켜서 사용자가 스스로 선택하게끔 함

# 협업하기 
- 파일 수정해서 add . -> commit으로 메시지 수정 -> push 하면 에러발생 -> git pull을 통해서 다시 add하고 commit(:wq)한뒤에 push하기
![image](https://user-images.githubusercontent.com/47103479/136814767-f7a610c2-ba1c-4972-a93d-45efddebc029.png)
![image](https://user-images.githubusercontent.com/47103479/136814928-681a6439-60b9-4c7e-a91e-16fdaf8b415d.png)

- git fetch(리모트 레포지토리의 브랜치를 검토해야할 때) -> git diff로 비교 / git pull(리모트 레포지토리의 브랜치를 검토할 필요없이 바로 합치고 싶을 때) => git pull = git fetch + git merge 
	- 리모트 레포지토리에서 가져온 브랜치의 내용을 머지하기 전에 점검해야할 필요가 있을 때 사용 
	- 리모트 레포지토리에 있는 브랜치의 내용과 내가 작성한 코드를 비교해서 잘못된 부분이 없는지 검토해야할 때 
- 리모트 레포지토리의 브랜치에 문제가 있을 때 
	- 잘못된 코드를 추가한 개발자에게 함수를 지우고 다시 리모트 레포지토리에 올려달라고 하기
	- 잘못된 부분을 알아서 해결하고 다시 git push 하기 
	![image](https://user-images.githubusercontent.com/47103479/136962237-177f0678-7487-4319-9a07-479d4cbf6a4e.png)

- git blame : 어떤 파일의 특정 코드를 누가 작성했는지 찾아내기 위한 커맨드 
![image](https://user-images.githubusercontent.com/47103479/136962907-3ebfaabb-d86c-47a2-818e-c31e6cac6c4d.png)

- git revert - 커밋하고 리버트 / 여러개의 커밋 리버트 가능 
![image](https://user-images.githubusercontent.com/47103479/136963626-466cff51-5f4b-494e-b64f-90e15c11c1ad.png)
![image](https://user-images.githubusercontent.com/47103479/136963849-de7624ef-d494-4c84-a1af-a20072822e0e.png)

- git reset 파일이름 : 해당 이름으로 리셋 
- git reflog HEAD가 가리켰던 commit들의 id 확인
- git log --pretty=oneline --all --graph : --graph -> 커밋 히스토리가 각 브랜치와의 관계가 잘 드러나도록 그래프 형식으로 출력 

- GUI 환경에서 작업 : GitKraken, Sourcetree 등 
- Sourcetree tutorial :  https://support.atlassian.com/bitbucket-cloud/docs/create-a-new-repository/

- git rebase : 브랜치를 베이스로 재지정한다
	- git rebase --continue
	- rebase는 새로운 커밋을 만들지 않음
	- rebase로 만들어진 커밋 히스토리는 merge로 만들어진 커밋 히스토리보다 좀 더 깔끔
	- rebase : 커밋 히스토리를 깔끔하게 유지하는게 더 중요한 경우  <-> merge : 두 브랜치를 합쳤다는 정보가 커밋 히스토리에 꼭 남아야 하는 경우

- git stash 
	- 어떤 브랜치에서 하던 작업을 아직 커밋하지 않았는데 다른 브랜치로 가야하는 상황에서 작업 중이던 내용을 잠깐 저장하고 싶을 때
	- working directory에서 작업하던 내용을 깃이 따로 보관(stack - 어떤 데이터를 저장하는 구조) 
	- 최근 커밋 이후로 작업했던 내용은 모두 스택에 옮겨지고 working directory 내부는 다시 최근 커밋의 상태로 초기화
	![image](https://user-images.githubusercontent.com/47103479/136980938-97904d18-4fcc-4f64-b1d8-83c89f0507ed.png)
	![image](https://user-images.githubusercontent.com/47103479/137139387-af8d98f5-633e-489e-bc82-7af797858c07.png)

- git cherry-pick
	- git history --all --graph -> git cherry-pick ca288
- git reset 
	- --hard : working directory 초기화
	- --mixed , --soft : working directory의 상태를 건드리지 않는 옵션 

- .gitignore 파일 : working directory 내에 존재하는 파일들 중에서 마치 존재하지 않는 것처럼 Git이 인식해야할 파일들의 목록이 적힌 파일
	- *.py[cod] - .pyc 또는 .pyo 또는 pyd로 끝나는 파일명
	- *$py.class - $py.class로 끝나는 파일명
	- *.so - .so로 끝나는 파일명

# 정리 
## Git 써보기
- git init : 현재 디렉토리를 Git이 관리하는 프로젝트 디렉토리(=working directory)로 설정하고 그 안에 레포지토리(.git 디렉토리) 생성
- git config user.name 'codeit' : 현재 사용자의 아이디를 'codeit'으로 설정(커밋할 때 필요한 정보)
- git config user.email 'teacher@codeit.kr' : 현재 사용자의 이메일 주소를 'teacher@codeit.kr'로 설정(커밋할 때 필요한 정보)
- git add [파일 이름] : 수정사항이 있는 특정 파일을 staging area에 올리기
- git add [디렉토리명] : 해당 디렉토리 내에서 수정사항이 있는 모든 파일들을 staging area에 올리기 
- git add . : working directory 내의 수정사항이 있는 모든 파일들을 staging area에 올리기
- git reset [파일 이름] : staging area에 올렸던 파일 다시 내리기
- git status : Git이 현재 인식하고 있는 프로젝트 관련 내용들 출력(문제 상황이 발생했을 때 현재 상태를 파악하기 위해 활용하면 좋음) 
- git commit -m "커밋 메시지" : 현재 staging area에 있는 것들 커밋으로 남기기
- git help [커맨드 이름] : 사용법이 궁금한 Git 커맨드의 공식 메뉴얼 내용 출력

## GitHub 시작하기
- git push -u(또는 --set-upstream) origin master : 로컬 레포지토리의 내용을 처음으로 리모트 레포지토리에 올릴 때 사용합니다.
- git push : 위의 커맨드를 한번 실행하고 난 후에는 git push라고만 쳐도 로컬 레포지토리의 내용을 리모트 레포지토리에 올릴 수 있습니다.
- git pull : 바로 위의 위에 있는 커맨드를 한번 실행하고 난 후에는 git pull이라고만 쳐도 리모트 레포지토리의 내용을 로컬 레포지토리로 가져옵니다.
- git clone [프로젝트의 GitHub 상 주소] : GitHub에 있는 프로젝트를 내 컴퓨터로 가져오기

## Git에서 커밋 다루기
- git log : 커밋 히스토리를 출력
- git log --pretty=oneline : --pretty 옵션을 사용하면 커밋 히스토리를 다양한 방식으로 출력할 수 있습니다. --pretty 옵션에 oneline이라는 값을 주면 커밋 하나당 한 줄씩 출력해줍니다. --pretty 옵션에 대해 더 자세히 알고싶으면 이 링크를 참고하세요. 
- git show [커밋 아이디] : 특정 커밋에서 어떤 변경사항이 있었는지 확인
- git commit --amend : 최신 커밋을 다시 수정해서 새로운 커밋으로 만듦
- git config alias.[별명] [커맨드] : 길이가 긴 커맨드에 별명을 붙여서 이후로는 별명으로도 해당 커맨드를 실행할 수 있게 설정
- git diff [커밋 A의 아이디] [커밋 B의 아이디] : 두 커밋 간의 차이 비교
- git reset [옵션] [커밋 아이디] : 옵션에 따라 하는 작업이 달라짐(옵션을 생략하면 --mixed 옵션이 적용됨) 
		(1) HEAD가 특정 커밋을 가리키도록 이동시킴(--soft는 여기까지 수행)

		(2) staging area도 특정 커밋처럼 리셋(--mixed는 여기까지 수행)

		(3) working directory도 특정 커밋처럼 리셋(--hard는 여기까지 수행)

		그리고 이때 커밋 아이디 대신 HEAD의 위치를 기준으로 한 표기법(예 : HEAD^, HEAD~3)을 사용해도 됨

- git tag [태그 이름] [커밋 아이디] : 특정 커밋에 태그를 붙임

## Git에서 브랜치 사용하기
- git branch [새 브랜치 이름] : 새로운 브랜치를 생성
- git checkout -b [새 브랜치 이름] : 새로운 브랜치를 생성하고 그 브랜치로 바로 이동
- git branch -d [기존 브랜치 이름] : 브랜치 삭제
- git checkout [기존 브랜치 이름] : 그 브랜치로 이동
- git merge [기존 브랜치 이름] : 현재 브랜치에 다른 브랜치를 머지
- git merge --abort : 머지를 하다가 conflict가 발생했을 때, 일단은 머지 작업을 취소하고 이전 상태로 돌아감

## Git 실전 I
- git fetch : 로컬 레포지토리에서 현재 HEAD가 가리키는 브랜치의 업스트림(upstream) 브랜치로부터 최신 커밋들을 가져옴(가져오기만 한다는 점에서, 가져와서 머지까지 하는 git pull과는 차이가 있음)
- git blame : 특정 파일의 내용 한줄한줄이 어떤 커밋에 의해 생긴 것인지 출력 
- git revert : 특정 커밋에서 이루어진 작업을 되돌리는(취소하는) 커밋을 새로 생성

## Git 실전 Ⅱ
- git reflog : HEAD가 그동안 가리켜왔던 커밋들의 기록을 출력
- git log --all --graph : 모든 브랜치의 커밋 히스토리를, 커밋 간의 관계가 잘 드러나도록 그래프 형식으로 출력
- git rebase [브랜치 이름] : A, B 브랜치가 있는 상태에서 지금 HEAD가 A 브랜치를 가리킬 때, git rebase B를 실행하면 A, B 브랜치가 분기하는 시작점이 된 공통 커밋 이후로부터 존재하는 A 브랜치 상의 커밋들이 그대로 B 브랜치의 최신 커밋 이후로 이어붙여짐(git merge와 같은 효과를 가지지만 커밋 히스토리가 한 줄로 깔끔하게 된다는 차이점이 있음)
- git stash : 현재 작업 내용을 스택 영역에 저장
- git stash apply [커밋 아이디] : 스택 영역에 저장된 가장 최근의(혹은 특정) 작업 내용을 working directory에 적용
- git stash drop [커밋 아이디] : 스택 영역에 저장된 가장 최근의(혹은 특정) 작업 내용을 스택에서 삭제
- git stash pop [커밋 아이디] : 스택 영역에 저장된 가장 최근의(혹은 특정) 작업 내용을 working directory에 적용하면서 스택에서 삭제
- git cherry-pick [커밋 아이디] : 특정 커밋의 내용을 현재 커밋에 반영

## 그 밖에 알아야할 사실 
- (1) git commit이라고만 쓰고 실행하면 커밋 메시지를 입력할 수 있는 텍스트 에디터 창이 뜹니다. 거기서 커밋 메시지를 입력하고 저장하고 나면 커밋이 이루어집니다.
- (2) git push와 git pull은 그 작업 단위가 브랜치입니다. 예를 들어, master 브랜치에서 git push를 하면 master 브랜치의 내용만 리모트 레포지토리의 master 브랜치로 전송되지, premium 브랜치의 내용이 전송되는 것은 아닙니다.(git push에 --all이라는 옵션을 주면 모든 브랜치의 내용을 전송할 수 있기는 합니다.)


