#!/bin/bash
while :
do
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

  # else
    #echo "Working tree clean. Nothing to commmit."
  fi

  sleep 60
done
