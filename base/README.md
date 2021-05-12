# Base Program
사용자 입력을 받아 auto-commit branch에 변경사항을 commit하고 master에 push

## Files
* baseProgram.sh : base program
* autoCommit.sh : 변경사항을 체크하여 auto-commit branch에 변경사항 commit & push 하는 쉘 스크립트
* userCommit.sh : 사용자로부터 commit message와 push할 branch명을 입력받아 해당 branch에 commit하는 쉘 스크립트

## Preconditions
 * git 사용자명과 password 저장 (아래의 명령어 순서대로 실행)
    - `git config --global credential.helper store`
    - `git config --global credential.helper cache`
 * local repository에 autoCommit.sh, userComit.sh, baseProgram.py를 추가하고 git에 commit & push
 * auto-commit branch 생성 후 해당 branch로 checkout
    - `git checkout -b auto-commit`

## How to use?
1. 파일 작업
2. baseProgram 실행
    * auto-commit?[y/n] y입력 시 현재까지의 변경사항이 auto-commit branch에 "Auto Commit"이란 commit message로 commit & push 됨
    * push to other branch?[y/n] y입력 시 commit&push할 branch명, commit message입력.
    * 입력한 branch에는 최종 결과만 commit됨
