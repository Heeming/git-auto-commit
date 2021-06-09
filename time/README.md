# Time Program

사용자 입력을 받아 auto-commit branch에 변경사항을 commit하고 push

## Files

- TimeAutoCommitProcess.sh : autocommit을 실행하는 파일(반복 X)
- baseProgram.py : time_based_autocommit과 createtime_based_autocommit에 대한 functions들을 포함하는 파일

## Preconditions

- git push <base branch name>을 실행 후 요청이 있을 경우 cmd/terminal/base 상에서 github에 로그인
- local repository에 autoCommit.sh, userComit.sh, baseProgram.py를 추가하고 git에 commit & push
- 해당 local repository는 이미 github remote가 완료됨을 전제로 작동함

## 1. time_based_autocommit
This function allows us to autocommit every n minutes from now.  
shell file을 불러올 때 에러가 나서 그 부분은 주석 처리를 해놓았으며,   
그 부분을 빼고는 온전하게 완성되었다.  
  
![time_based_autocommit](https://user-images.githubusercontent.com/69781815/121240360-32c08880-c8d5-11eb-8d90-eb81dee08834.JPG)  
  
  
## 1-1. How to use?(미완성이라 3번은 완성이 되어야 할 수 있음)

1. baseProgram.py 실행 `python3 baseProgram.py`
2. 모드 선택 `>> 3`
3. 퍼센트 입력, 파일지정 `Add file name : $file_name`
4. 파일 생성 시간으로부터 시간이 n분 지날 때마다 autoCommit 실행
  
## 1-2. result of time_based_autocommit
![time_based_autocommit_1](https://user-images.githubusercontent.com/69781815/121240393-3d7b1d80-c8d5-11eb-9967-8187303871d0.gif)  
![time_based_autocommit_2](https://user-images.githubusercontent.com/69781815/121240397-3f44e100-c8d5-11eb-9a2b-325e94054bdb.gif)  
  
  

### 2. createtime_based_autocommit
This function allows us to autocommit every n minutes from creation time of the file you set.  
shell file을 불러올 때 에러가 나서 그 부분은 주석 처리를 해놓았으며,   
그 부분을 빼고는 온전하게 완성되었다.  
  
![createtime_based_autocommit](https://user-images.githubusercontent.com/69781815/121240365-348a4c00-c8d5-11eb-8844-f28af420a5da.JPG) 
  
  
## 2-1. How to use?(미완성이라 3번은 완성이 되어야 할 수 있음)

1. baseProgram.py 실행 `python3 baseProgram.py`
2. 모드 선택 `>> 4`
3. 퍼센트 입력, 파일지정 `Add file name : $file_name`
4. 파일 생성 시간으로부터 시간이 n분 지날 때마다 autoCommit 실행
  
  
## 2-2. result of createtime_based_autocommit
![createtime_based_autocommit](https://user-images.githubusercontent.com/69781815/121240409-42d86800-c8d5-11eb-9e36-34d8af9f884a.gif)
  

  
  
When you select the option from the menu, time_based_autocommit and createtime_based_autocommit can be performed by this logic:  
  
![logic](https://user-images.githubusercontent.com/69781815/121240377-36eca600-c8d5-11eb-8d70-86f868181bd1.JPG)  

## 3. 추가 구현 예정

- shell 파일을 실행시키는 subprocess.call를 실행 시 생기는 에러를 보완