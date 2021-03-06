# Base Program
사용자 입력을 받아 auto-commit branch에 변경사항을 commit하고 master에 push

## Folder
* code : 사용자 워크스페이스

## Files
* baseProgram.sh : base program - chioce 3 파트 수정
* error_autoCommit.sh : 에러 메세지로 autocommit 해주는 쉘 스크립트
* error_autoCommitProcess.sh : error_autoCommit.sh를 실행해주는 쉘 스크립트
* exe_c.sh : c 코드를 컴파일하여 오류 여부를 체크해주는 쉘 스크립트
* exe_java.sh : java 코드를 컴파일하여 오류 여부를 체크해주는 쉘 스크립트
* test1~7.py/c/java : 에러 테스트 코드
* baseProgram.py :
** path로 설정한 경로의 폴더 내에 파이썬, c, java 파일을 스캔하고 해당 파일들을 유저가 컴파일하는 것을 감지할 시에 compile한다. 이 때 컴파일 에러가 발생하면 해당 에러메세지로 commit한다(choice == 3).
** path로 설정한 경로의 폴더 내에 파이썬, c, java 파일을 스캔하고 해당 파일들을 유저가 실행하는 것을 감지할 시에 compile한 뒤 실행한다. 실행 시 에러가 발생하면 해당 에러메세지로 commit한다(choice == 3.1).
** path로 설정한 경로의 폴더 내에 파이썬, c, java 파일을 스캔하고 해당 파일들이 실행 중단 될 시에 auto-commit을 한다(choice == 3.2).
* compile_c.sh : input 값으로 전달받은 파일을 유저가 컴파일 중인지 검사하고 만약 컴파일 중이면 sub_compile_c.sh를 실행한다. 이후 sub_compile_c.sh가 정상적으로 컴파일을 마치지 않았을 시 컴파일 에러 메세지로 error_autoCommitProcess.sh를 실행한다.
* sub_compile_c.sh : input 값으로 전달받은 파일을 컴파일한다.
* compile_java.sh : input 값으로 전달받은 파일을 유저가 컴파일 중인지 검사하고 만약 컴파일 중이면 sub_compile_java.sh를 실행한다. 이후 sub_compile_java.sh가 정상적으로 컴파일을 마치지 않았을 시 컴파일 에러 메세지로 error_autoCommitProcess.sh를 실행한다.
* subcompile_java.sh : input 값으로 전달 받은 파일을 컴파일 한다.
* exe_c.sh : input 값으로 전달받은 파일을 유저가 실행 중인지 검사하고 만약 실행 중이면 sub_exe_c.sh를 실행한다. 이후 sub_exe_c.sh가 정상적으로 실행을 마치지 않았을 시 실행 에러 메세지로 * error_autoCommitProcess.sh를 실행한다.
* sub_exe_c.sh : input 값으로 전달 받은 파일을 컴파일한 뒤 실행한다.
* exe_java.sh : input 값으로 전달받은 파일을 유저가 실행 중인지 검사하고 만약 실행 중이면 sub_exe_java.sh를 실행한다. 이후 sub_exe_java.sh가 정상적으로 실행을 마치지 않았을 시 실행 에러 메세지로 error_autoCommitProcess.sh를 실행한다.
* sub_exe_java.sh : input 값으로 전달 받은 파일을 컴파일 한 뒤 실행한다.
* error_autoCommit.sh : 오류 메세지를 input 값으로 주면 해당 메세지로 auto-commit을 한다.
* errorautoCommitProcess.sh : error_autoCommit.sh를 실행시켜 준다.
* error_killProcess.sh : error 기능을 구현할 때 사용되는 쉘 스크립트들을 종료해준다.


## Preconditions
 * git 사용자명과 password 저장 (아래의 명령어 순서대로 실행)
    - `git config --global credential.helper store`
    - `git config --global credential.helper cache`
 * local repository에 autoCommit.sh, userComit.sh, baseProgram.py를 추가하고 git에 commit & push
 * auto-commit branch 생성 후 해당 branch로 checkout
    - `git checkout -b auto-commit`
 * git push <base branch name>을 실행 후 요청이 있을 경우 cmd/terminal/base 상에서 github에 로그인
 * local repository에 autoCommit.sh, userComit.sh, baseProgram.py를 추가하고 git에 commit & push
 * 해당 local repository는 이미 github remote가 완료됨을 전제로 작동함
 * gcc와 javac가 설치되어 있어야 한다.
 * 에러 감지를 원하는 소스코드를 컴파일할 시 c 소스코드의 경우 소스코드의 이름과 동일하게 컴파일 파일을 생성해야 한다.

## How to use?
1. 파일 작업
2. baseProgram 실행
    * auto-commit?[y/n] y입력 시 현재까지의 변경사항이 auto-commit branch에 "Auto Commit"이란 commit message로 commit & push 됨
    * push to other branch?[y/n] y입력 시 commit&push할 branch명, commit message입력.
    * 입력한 branch에는 최종 결과만 commit됨
3. 조건 설정
    * code 폴더 안의 작업할 코드들을 생성.
    * 해당 코드들에서 에러가 발생할 시 자동으로 commit.
    * 커밋 메세지는 해당 코드 실행시 콘솔에서 출력되는 오류 메세지로 commit됨.
    * 실행 취소시 time out으로 commit 메세지가 설정되어 commit됨.

## 추가 구현 예정
* python, c, java 외 다른 언어 소스코드 오류 발생 시 commit 가능하도록 다양한 언어 추가 지원 구현 예정.

 
### 데모(Demo) 
https://user-images.githubusercontent.com/53044223/121273797-08d28a80-c904-11eb-8634-04764b16280f.mp4

git source tree
![image (1)](https://user-images.githubusercontent.com/53044223/121279850-33c2db80-c910-11eb-9607-95d8bf290e9a.png)
