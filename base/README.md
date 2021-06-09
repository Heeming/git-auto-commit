# Base Program

사용자 입력을 받아 auto-commit branch에 변경사항을 commit하고 master에 push

## Files

- baseProgram.py  : base program ( Now not work )
- addFile.sh      : 파일을 지정하여 git add 되지 않은 파일일 경우 add 하는 쉘 스크립트
- autoCommit.sh   : 변경사항을 체크하여 auto-commit branch에 변경사항 commit & push 하는 쉘 스크립트
- autoCommitProcess.sh : autoCommit.sh를 background process로 실행시키는 쉘 스크립트
- continue.sh : 기존에 git-auto-commit 프로그램으로 auto-commit했던 repository에 git-auto-commit 프로그램을 다시 실행 시 환경 설정하는 쉘 스크립트
- deleteBranch.sh : auto-commit 전용 branch (branch name : auto-commit )를 삭제하는 쉘 스크립트
- killProcess.sh : autoCommitProcess.sh가 생성한 background process를 kill하는 쉘 스크립트
- setting.sh : git-auto-commit을 처음 적용한 repository 거나 이전에 deleteBranch.sh를 실행한 repository에 프로그램 실행 시 환경 설정하는 쉘 스크립트
- userCommit.sh   : 사용자로부터 commit message와 push할 branch명을 입력받아 해당 branch에 commit하는 쉘 스크립트
