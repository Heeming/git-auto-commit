# File Program

사용자 입력을 받아 auto-commit branch에 변경사항을 commit하고 push

## Files

- file_autoCommit.sh : 사용자가 파일 이름을 지정하면 그 파일의 변경사항이 감지되면 commit & push 하는 쉘 스크립트
- file_section.sh : 사용자로부터 전체 코드의 특정 구간 n부터 m을 입력받아 특정 구간 내에 변경사항이 발생하면 commit & push 하는 쉘 스크립트
- file_npercent.sh : 사용자로부터 전체 코드의 몇%가 변경되면 커밋할것인지 n을 입력받아 변경사항이 n% 이상이면 commit & push 하는 쉘 스크립트

## Preconditions

- git push <base branch name>을 실행 후 요청이 있을 경우 cmd/terminal/base 상에서 github에 로그인
- local repository에 autoCommit.sh, userComit.sh, baseProgram.py를 추가하고 git에 commit & push
- 해당 local repository는 이미 github remote가 완료됨을 전제로 작동함

# 1. 특정 파일 지정 (Done)

file_autoCommit.sh : 사용자가 파일 이름을 지정하면 그 파일의 변경사항이 감지되면 commit & push 하는 쉘 스크립트

## How to use?

1. baseProgram.py 실행 `python3 baseProgram.py`
2. 모드 선택 `>> 3`
3. 파일 이름 입력 `Specify file_name to detect : $file_name`
4. $file_name 의 파일 수정
5. autoCommit 실행

## 실행 예시

1. `python3 baseProgram.py` `>> 3`
<img src="https://user-images.githubusercontent.com/60775453/121275988-c52e4f80-c908-11eb-9242-971e6f7d1853.png" width=70% height=70% >
2. 파일 이름 지정 `Specify file_name to detect : $file_name`
<img src="https://user-images.githubusercontent.com/60775453/121276158-1c342480-c909-11eb-843c-dde82886b473.png" width=70% height=70% >
3. 오토커밋
<img src="https://user-images.githubusercontent.com/60775453/121276052-e42ce180-c908-11eb-9f67-12cbd0115c34.png" width=50% height=50% >
4. git kraken
<img src="https://user-images.githubusercontent.com/60775453/121276234-4259c480-c909-11eb-8ee3-87da7ada1f4f.png" width=90% height=90% >

## 추가 구현 예정

- 사용자 입력에 따라 autoCommit.sh를 background에서 반복적으로 실행시키고 background 실행을 중단하는 shell 혹은 python 코드

# 2. 특정 파일의 전체 줄의 n% 이상 변경 감지 (Doing : Fix Type error)

file_npercent.sh : 사용자로부터 전체 코드의 몇%가 변경되면 커밋할것인지 n을 입력받아 변경사항이 n% 이상이면 commit & push 하는 쉘 스크립트

## How to use?

1. baseProgram.py 실행 `python3 baseProgram.py`
2. 모드 선택 `>> 4`
3. 퍼센트 입력, 파일지정 `Input percent : $n`, `Add file name : $file_name`
4. $file_name 의 파일 수정
5. 전체 코드의 n% 이상 변경 감지 시 autoCommit 실행

## 코드

```bash
  echo "Checking file change for n%"

  filename="$1"
  n="$2"
  _100="100"
  diff_msg=`git diff --stat $filename`

  change_line=$(echo $diff_msg | cut -f  3 -d' ') # 변경된 줄 수
  FILE_ROW_COUNT=$(cat $filename| wc -l) # 전체 줄 수
  change=`expr $change_line / $FILE_ROW_COUNT` # 변경된 줄 수 / 전체 줄 수
  change_percent=`expr $change \* $_100` # percent = 변경된 줄 수 / 전체 줄 수 * 100
  echo "$FILE_ROW_COUNT"

  if ! git diff --quiet && $change_percent > $n
  then
    git checkout auto-commit
    git add $filename
    git commit -m "Auto Commit: More than $n percent change detected."
    git push -u origin auto-commit
```

## 실행예시

### 고려할 사항

1. 초기에 파일의 전체 라인 수를 읽기 때문에 0줄인 파일은 작업 불가
2. 한 줄의 길이가 아니라 단순 줄 수로 퍼센트 계산하므로 한 줄의 코드 길이에 따라 퍼센트가 부정확함


# 3. 특정 파일에서 변경사항을 감지할 구간 설정 (Doing : Fix Type error)

file_section.sh : 사용자로부터 전체 코드의 특정 구간 n부터 m을 입력받아 특정 구간 내에 변경사항이 발생하면 commit & push 하는 쉘 스크립트

## How to use?

1. baseProgram.py 실행 `python3 baseProgram.py`
2. 모드 선택 `>> 5`
3. 파일지정, 구간설정 `Add file : $file_name`, `Start line : $n`, `Finish line : $m`
4. $file_name 의 파일 수정
5. 전체 코드 중 n부터 m 구간의 코드 변경 시 autoCommit 실행

## 코드
```bash
#!/bin/bash
while :
do
  echo "Specify file section"

  filename="$1"
  n="$2" # 시작 줄
  m="$3" # 마지막 줄
  diff_msg=`git diff --stat $filename`

  change_line=$(echo $diff_msg | cut -f  3 -d' ') # 현재 변경된 줄 수 
  FILE_ROW_COUNT=$(cat $filename| wc -l) # 전체 줄 수 

  if ! git diff --quiet && ($change_line > $n || $change_line < $m)
  then
    git checkout auto-commit
    git add $filename
    git commit -m "Auto Commit: section $n ~ $m change detected."
    git push -u origin auto-commit

  # else
    #echo "Working tree clean. Nothing to commmit."
  fi

  sleep 60
done
```

## 보완할 점
- type error

