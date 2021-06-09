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
