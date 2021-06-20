# Time Program

시간에 대한 사용자 입력을 받아 해당 시간이 지날 때마다 auto-commit branch에 commit하고 push

## Files

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

## Preconditions
  
 * 윈도우 사용자는 리눅스를 추가적으로 반드시 설치할 것.  
(보편적으로 WSL2를 설치하거나, virtual machine을 통해 리눅스를 설치하면 윈도우 사용자도 실행이 가능하다.  
하지만, 작성자의 경우 WSL2를 설치하고 나서도 /bin/bash 에러를 겪고, virtual machine은 설치도 못한 채 amd-v error를 겪었다.  
/bin/bash는 lxrun /install을 해야 해결 가능한데 이 명령어 자체가 먹히질 않으며(이때 bash를 사용해도 된다지만 bash를 사용했을 때도 에러가 발생하여 무조건 lxrun /install을 이용하는 수밖에 없었다),  
윈도우 로컬 계정을 이용하는 경우 실패할 수도 있다지만 본인의 경우, 로컬이 아닌 이메일 계정이기 때문에 해결 방법도 전혀 찾을 수 없었다.  
virtual machine의 amd-v error의 경우, 바이오스 진입하여 해결이 가능하지만, 나의 경우 이 방법도 실패하여 실행이 불가능하였다.  
본인과 같이 에러를 겪는 특이한 케이스의 경우, 이 프로그램의 실행은 보장될 수 없는 점을 유의하기 바란다.)  
 * git 사용자명과 password 저장 (아래의 명령어 순서대로 실행)
    - `git config --global credential.helper store`
    - `git config --global credential.helper cache`
 * local repository에 shell 파일들, baseProgram.py를 추가하고 git에 commit & push
 * auto-commit branch 생성 후 해당 branch로 checkout
    - `git checkout -b auto-commit`
 * git push <base branch name>을 실행 후 요청이 있을 경우 cmd/terminal/base 상에서 github에 로그인
 * local repository에 autoCommit.sh, userComit.sh, baseProgram.py를 추가하고 git에 commit & push
 * 해당 local repository는 이미 github remote가 완료됨을 전제로 작동함
  
## 1-1. How to use?
1. baseProgram.py 실행 `python3 baseProgram.py`
2. 모드 선택 `>> 3`
3. 퍼센트 입력, 파일지정 `Enter your file name : $file_name`
4. 실행 시간으로부터 시간이 n분 지날 때마다 autoCommit 실행
  
## 1-2. result of time_based_autocommit
![time_based_autocommit_1](https://user-images.githubusercontent.com/69781815/121240393-3d7b1d80-c8d5-11eb-9967-8187303871d0.gif)  
![time_based_autocommit_2](https://user-images.githubusercontent.com/69781815/121240397-3f44e100-c8d5-11eb-9a2b-325e94054bdb.gif)  
  
### 2. createtime_based_autocommit
This function allows us to autocommit every n minutes from creation time of the file you set.  
  
## 2-1. How to use?
1. baseProgram.py 실행 `python3 baseProgram.py`
2. 모드 선택 `>> 4`
3. 퍼센트 입력, 파일지정 `Enter your file name : $file_name`
4. 파일 생성 시간으로부터 시간이 n분 지날 때마다 autoCommit 실행
  
## 2-2. result of createtime_based_autocommit
![createtime_based_autocommit](https://user-images.githubusercontent.com/69781815/121240409-42d86800-c8d5-11eb-9e36-34d8af9f884a.gif)
  
## 3. 추가 구현할 사항
- 없음