# Base Program

git-auto-commit 프로그램. program.py가 해당 프로그램이다. .sh파일은 프로그램 실행에 필요한 쉘 스크립트이다. 

## Files

### Program
- program.py  : git-auto-commit 프로그램. GUI가 사용되었다.

### Shell Script
#### Commit mode
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

#### Otherwise
- setting.sh : git-auto-commit을 처음 적용한 repository 거나 이전에 deleteBranch.sh를 실행한 repository에 프로그램 실행 시 환경 설정하는 쉘 스크립트
- continue.sh : 기존에 git-auto-commit 프로그램으로 auto-commit했던 repository에 git-auto-commit 프로그램을 다시 실행 시 환경 설정하는 쉘 스크립트
- killProcess.sh : autoCommitProcess.sh가 생성한 background process를 kill하는 쉘 스크립트
- addFile.sh      : 파일을 지정하여 git add 되지 않은 파일일 경우 add 하는 쉘 스크립트
- userCommit.sh   : 사용자로부터 commit message와 push할 branch명을 입력받아 해당 branch에 commit하는 쉘 스크립트
- deleteBranch.sh : auto-commit 전용 branch (branch name : auto-commit )를 삭제하는 쉘 스크립트

## How to use?
### Preconditions
1. 실행을 위해선 pyqt5가 설치되어있어야 한다.
   설치 방법 (linux) : `pip install pyqt5`
2. Terminal에서 github 로그인이 되어 있어야 한다.
   git push 명령어를 통해 로그인이 되어 있는지 아닌지에 대한 확인 작업이 반드시 필요하다. 로그인이 되어 있지 않을 경우, git push에 대해 오류를 일으킨다.

### Execute
1. base폴더를 다운 받는다.
2. base 폴더에서 `python3 program.py`를 실행시킨다.

## 추가 구현 예정
1. login: GUI를 통한 login 기능
2. cloneRepository: GUI를 통한 respository clone 기능
3. make localRepository: GUI를 통해 local에 새로운 repository를 생성하는 기능
4. make push to option : 현재는 모든 auto-commit이 remote repository에 push까지 되도록 개발되어 있다. 해당 push에 대해 사용자가 push 여부를 지정할 수 있도록 할 예정이다.
5. branch & commit graph : respository 선택 후 화면에 해당 respoisotry의 git log(branch, commit)이 graph로 보여지며 실시간으로 업데이트 되도록 개발할 예정이다. 현재는 repository 선택 시의 git log가 보여지고 업데이트 되지는 않는다.
6. open multiple repositories : tab 기능을 이용해 한번에 여러 repository를 open하여 개별적으로 auto-commit을 사용할 수 있도록 개발하고자 한다.
7. select multiple modes : auto-commit mode 설정 시 여러 모드를 중복 선택 가능하도록 할 예정이다. 현재는 GUI 상으론 중복 선택이 가능하지만, 실제로 중복선택할 경우 에러가 발생한다. 각 모드별로 동시 실행 가능한 것과 불가능한 것을 나눠, 동시 실행 불가능한 모드의 경우 GUI자체에서 중복 선택 불가능하도록 만들 예정이다.
8. manage merging : master branch 혹은 다른 개발 브랜치로 auto-commit branch를 merge할 경우 conflict 등의 문제가 발생할 수 있다. 이를 다룰 수 있는 기능을 추가할 계획이 있다.
9. Vscode Extension : Vscode Extension으로 프로그램을 확장할 계획이 있다.
