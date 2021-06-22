# 사용자 조건에 따른 git-auto-commit 시스템
The project git-auto-commit with user customizing in 2021 Open Source Software Project course.

## Introduction
사용자가 설정한 조건에 따라 file change를 git에 자동으로 commit & push 해주는 시스템이다. 사용자가 auto-commit을 사용할 폴더와 github repository를 등록하면 repository에 auto-commit 전용 branch를 새로 생성한다. 사용자 조건에 따라 auto-commit을 하며, 해당 commit은 해당 branch에 기록된다. 사용자가 프로그램에서 auto-commit을 해제하면 branch를 삭제한다.

## Features
기본 사용자 조건 : 사용자가 모든 파일에 대해서, 혹은 특정 부분/특정 파일을 지정하여 사용자 조건을 customizing할 수 있다. 
- [base]
  - repository 변경사항 감지 시 자동 commit
  - background process로 생성
  - auto commit 전용 branch 생성 및 해당 branch에만 push
  - git add file 기능
  - user-commit & push 기능
  -  auto-commit 해제 및 branch 삭제
- [time]
  - 일정 시간마다 commit
  - 파일 생성 시점 기준으로 사용자가 설정한 시간마다 자동으로 저장하고 commit
- [error]
  - 코드 컴파일 중 에러 발생 시 commit
  - 에러 메세지 발생 시 commit
  - 실행 중단 시 commit
- [file]
  - 사용자가 특정 파일을 지정하면 그 파일에서만 변경 사항 감지 후 commit
  - 전체 코드의 n%가 변경된 경우 commit
- [GUI]
  - 위의 기본 사용자 조건을 사용자가 Customizing을 쉽게 달성할 수 있도록 하기 위한 GUI 개발

## Quick Start
- 프로젝트 다운로드
```bash
> git clone 프로젝트-주소
> cd git-auto-commit
> cd base
> git checkout 브랜치-이름
> python baseProgram.py
```
## How to use?
1. how to start 
<img src="https://github.com/Heeming/git-auto-commit/blob/master/img/1.png" width=50% height=50%>

2. main window1
<img src="https://github.com/Heeming/git-auto-commit/blob/master/img/2.png" width=50% height=50%>

3. click open repostiroy chooing repository window show
<img src="https://github.com/Heeming/git-auto-commit/blob/master/img/3.png" >

4. main window2 - after choosing repository
<img src="https://github.com/Heeming/git-auto-commit/blob/master/img/4.png" >

5. select mode window - when click ChangeMode button in main window2
<img src="https://github.com/Heeming/git-auto-commit/blob/master/img/5.png" >

6. file choosing window - when lick Add File button on select mode UI
<img src="https://github.com/Heeming/git-auto-commit/blob/master/img/6.png" >

7. change spinbox value
<img src="https://github.com/Heeming/git-auto-commit/blob/master/img/7.png" >

8. choose file1
<img src="https://github.com/Heeming/git-auto-commit/blob/master/img/8.png" >

9. choose file2 and change spinbox value
<img src="https://github.com/Heeming/git-auto-commit/blob/master/img/9.png" >

10. choose file3
<img src="https://github.com/Heeming/git-auto-commit/blob/master/img/10.png" >

11. push window - when click Push button on main window2
<img src="https://github.com/Heeming/git-auto-commit/blob/master/img/11.png" >

12. delete auto-commit window when click delete auto-commit branch on main window2
<img src="https://github.com/Heeming/git-auto-commit/blob/master/img/12.png" >


## Files Descriptions & Documents
### [base](https://github.com/Heeming/git-auto-commit/blob/master/base/README.md)
  - Program
    - program.py  : git-auto-commit 프로그램. GUI가 사용되었다.

  - Shell Script
    - Commit mode
      - autoCommit.sh   : 변경사항을 체크하여 auto-commit branch에 변경사항 commit & push 하는 쉘 스크립트
      - autoCommitProcess.sh : autoCommit.sh를 background process로 실행시키는 쉘 스크립트

      - fileAutoCommit.sh : 변경사항을 tracking할 파일을 지정하여, 해당 파일에 변경사항이 발생하는 경우에만 전체 파일에 대해 변경사항을 commit & push하는 쉘 스크립트
      - fileAutoCommitProcess.sh : fileAutoCommit.sh를 background process로 실행시키는 쉘 스크립트
      - fileNPercent.sh : 특정 파일을 지정하여 해당 파일의 내용이 지정한 퍼센트 이상으로 변경되었을 경우 전체 파일에 대해 변경사항을 commit & push하는 쉘 스크립트
      - fileNPercentProcess.sh : fileNPercent.sh를 background process로 실행시키는 쉘 스크립트

      - timeAutoCommit.sh : 일정 시간이 지날때마다 자동으로 변경사항을 commit & push하는 쉘 스크립트
      - timeAutoCommitProcess.sh : timeAutoCommit.sh를 background process로 실행시키는 쉘 스크립트
      - filetimeAutoCommit.sh : 특정 파일을 지정하여 해당 파일의 생성시간 기준으로 일정 간격의 시간이 지나면 자동으로 변경사항을 commit & push하는 쉘 스크립트
      - filetimeAutoCommitProcess.sh : filetimeAutoCommit.sh를 background process로 실행시키는 쉘 스크립트

    - Otherwise
      - setting.sh : git-auto-commit을 처음 적용한 repository 거나 이전에 deleteBranch.sh를 실행한 repository에 프로그램 실행 시 환경 설정하는 쉘 스크립트
      - continue.sh : 기존에 git-auto-commit 프로그램으로 auto-commit했던 repository에 git-auto-commit 프로그램을 다시 실행 시 환경 설정하는 쉘 스크립트
      - killProcess.sh : autoCommitProcess.sh가 생성한 background process를 kill하는 쉘 스크립트
      - addFile.sh      : 파일을 지정하여 git add 되지 않은 파일일 경우 add 하는 쉘 스크립트
      - userCommit.sh   : 사용자로부터 commit message와 push할 branch명을 입력받아 해당 branch에 commit하는 쉘 스크립트
      - deleteBranch.sh : auto-commit 전용 branch (branch name : auto-commit )를 삭제하는 쉘 스크립트

    - How to use?
      - Preconditions
        1. 실행을 위해선 pyqt5가 설치되어있어야 한다.
           설치 방법 (linux) : `pip install pyqt5`
        2. Terminal에서 github 로그인이 되어 있어야 한다.
           git push 명령어를 통해 로그인이 되어 있는지 아닌지에 대한 확인 작업이 반드시 필요하다. 로그인이 되어 있지 않을 경우, git push에 대해 오류를 일으킨다.

      - Execute
        1. base폴더를 다운 받는다.
        2. base 폴더에서 `python3 program.py`를 실행시킨다.

### [time](https://github.com/Heeming/git-auto-commit/blob/master/time/README.md)
- killProcess.sh, setting.sh, continue.sh, addFile.sh : 기존 파일과 동일
- TimeAutoCommitProcess.sh : autocommit을 실행하는 파일(반복 X)
- baseProgram.py : time_based_autocommit과 createtime_based_autocommit에 대한 function들을 포함하는 파일
-> function들
	1) auto_commit : shell 파일 실행
	2) time_based_autocommit : 매 n분마다 auto_commit function 실행
	3) createtime : 파일 생성시간을 계산하여 ymd 포맷으로 계산
	4) start : 파일 생성시간을 timestamp를 이용해 float형 숫자로 바꾼 후, float형을 int형으로 변환
	5) stop : 현재 시간을 timestamp를 이용해 float형 숫자로 바꾼 후, float형을 int형으로 변환
	6) remainder : (현재 시간 - 파일 생성 시간) % 60n을 통해서 나머지 계산
	7) ctime_based_autocommit : remainder가 0이 되면 shell 파일 실행

### [error](https://github.com/Heeming/git-auto-commit/blob/master/error/README.md)
- baseProgram.sh : base program - chioce 3 파트 수정
- error_autoCommit.sh : 에러 메세지로 autocommit 해주는 쉘 스크립트
- error_autoCommitProcess.sh : error_autoCommit.sh를 실행해주는 쉘 스크립트
- exe_c.sh : c 코드를 컴파일하여 오류 여부를 체크해주는 쉘 스크립트
- exe_java.sh : java 코드를 컴파일하여 오류 여부를 체크해주는 쉘 스크립트
- test1~7.py/c/java : 에러 테스트 코드

### [file](https://github.com/Heeming/git-auto-commit/blob/master/file/README.md)
- file_autoCommit.sh : 사용자가 파일 이름을 지정하면 그 파일의 변경사항이 감지되면 commit & push 하는 쉘 스크립트
- file_section.sh : 사용자로부터 전체 코드의 특정 구간 n부터 m을 입력받아 특정 구간 내에 변경사항이 발생하면 commit & push 하는 쉘 스크립트
- file_npercent.sh : 사용자로부터 전체 코드의 몇%가 변경되면 커밋할것인지 n을 입력받아 변경사항이 n% 이상이면 commit & push 하는 쉘 스크립트

### [GUI](https://github.com/Heeming/git-auto-commit/blob/master/gui/README.md)
- checkoutUI.py : branch checkout 시 어떤 브랜치로 checkout하는지 설정하는 창
- cloneRepoUI.py : Repository clone 시 clone할 repository 정보를 입력하는 창
- gitAutoCommitUI.py : 현재 git-auto-commit을 실행하고 있는 repository control 창
- initRepoUI.py : local에 새로운 repository 생성 시 생성 할 repository 정보를 입력하는 창
- pushUI.py : git push 시 commit message와 branch를 지정하는 창
- repoSelectUI.py : 어떤 repository에 git-auto-commit을 실행할 것인지 선택하는 창
- selectMode.py : git-auto-commit의 사용자 조건를 선택하는 창
- signInUI.py : 로그인 창

## Demo
[Demo vedio](https://drive.google.com/drive/folders/14EXzA5BIJCla3NhSRaD8_JMwRASzUYEl?usp=sharing)

1. execute-openRepository
<img src="https://github.com/Heeming/git-auto-commit/blob/master/gif/1.gif" width=50% height=50%>

2. basic auto-commit mode
<img src="https://github.com/Heeming/git-auto-commit/blob/master/gif/2.gif" width=50% height=50%>

3. time auto-commit mode1
<img src="https://github.com/Heeming/git-auto-commit/blob/master/gif/3.gif" width=50% height=50%>

4. time auto-commit mode2
<img src="https://github.com/Heeming/git-auto-commit/blob/master/gif/4.gif" width=50% height=50%>

5. file auto-commit mode1
<img src="https://github.com/Heeming/git-auto-commit/blob/master/gif/5.gif" width=50% height=50%>

6. file-auto commit mode2
<img src="https://github.com/Heeming/git-auto-commit/blob/master/gif/6.gif" width=50% height=50%>

7. add file
<img src="https://github.com/Heeming/git-auto-commit/blob/master/gif/7.gif" width=50% height=50%>

8. push
<img src="https://github.com/Heeming/git-auto-commit/blob/master/gif/8.gif" width=50% height=50%>

9. delete auto-commit branch
<img src="https://github.com/Heeming/git-auto-commit/blob/master/gif/9.gif" width=50% height=50%>


## Contribution guidelines
- [CONTRIBUTING](https://github.com/Heeming/git-auto-commit/blob/master/CONTRIBUTING.md)

## Code of Conduct
- [CODE_OF_CONDUCT](https://github.com/Heeming/git-auto-commit/blob/master/CODE_OF_CONDUCT.md)

## License
[MIT license](https://opensource.org/licenses/MIT)
```
MIT License

Copyright (c) 2021 Heeming

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
