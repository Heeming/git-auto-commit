#!/bin/bash
while :
do
  filename="$1"
  n="$2"

  echo "Checking file change for $n%"

  diff_msg=`git diff --stat $filename`
  total_line=$(cat $filename| wc -l) # 전체 줄 수 
  changes_line=$(echo $diff_msg | cut -f 3 -d' ') # 변경된 줄 수 
  changes=`expr $changes_line \* 100` # 변경된 줄 수 * 100
  change_percent=`expr $changes / $total_char` # percent = 변경된 줄 수 / 전체 줄 수 * 100
  echo "전체 줄 수 : $total_line"
  echo "변경된 줄 수 : $changes_line"
  echo "변경 : $changes"
  echo "변경된 퍼센트 : $change_percent"

  # if ! git diff --quiet
  if [ "$change_percent" -gt "$n" ];then
    git checkout auto-commit
    git add $filename
    git commit -m "Auto Commit: More than $n percent change detected."
    git push -u origin auto-commit

  # else
    #echo "Working tree clean. Nothing to commmit."
  fi

  sleep 60
done
