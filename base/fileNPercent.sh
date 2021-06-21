#!/bin/sh

path="$1"

cd $path

filename="$2"
n="$3"

while :
do
  diff_msg=`git diff --stat $filename`
  FILE_ROW_COUNT=$(cat $filename| wc -l) # 전체 줄 수 
  change_line=$(echo $diff_msg | cut -f 3 -d' ') # 변경된 줄 수 
  change=$(($change_line/$FILE_ROW_COUNT)) # 변경된 줄 수 / 전체 줄 수 
  change_percent=$(( $change*100 )) # percent = 변경된 줄 수 / 전체 줄 수 * 100

  if [[ ! git diff --quiet ]] && [[ $change_percent -gt $n ]]
  then
    git checkout auto-commit
    git add .
    git commit -m "Auto Commit: More than $n percent change detected."
    git push -u origin auto-commit
  fi

  sleep 10
done
