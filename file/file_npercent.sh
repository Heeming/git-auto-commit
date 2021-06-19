#!/bin/bash
while :
do
  filename="$1"
  n="$2"

  echo "Checking file change for $n%"

  diff_msg=`git diff --stat $filename`
  FILE_ROW_COUNT=$(cat $filename| wc -l) # 전체 줄 수 
  change_line=$(echo $diff_msg | cut -f 3 -d' ') # 변경된 줄 수 
  change=`expr $change_line / $FILE_ROW_COUNT` # 변경된 줄 수 / 전체 줄 수 
  change_percent=`expr $change \* 100` # percent = 변경된 줄 수 / 전체 줄 수 * 100
  echo "전체 줄 수 : $FILE_ROW_COUNT"
  echo "변경된 줄 수 : $change_line"
  echo "변경 : $change"
  echo "변경 된 퍼센트 : $change_percent"

  # if ! git diff --quiet
  if [! git diff --quiet] && [$change_percent -gt $n]
  then
    git checkout auto-commit
    git add $filename
    git commit -m "Auto Commit: More than $n percent change detected."
    git push -u origin auto-commit

  # else
    #echo "Working tree clean. Nothing to commmit."
  fi

  sleep 60
done
