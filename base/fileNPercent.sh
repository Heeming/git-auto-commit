#!/bin/sh

path="$1"

cd $path

filename="$2"
n="$3"

while :
do
  if ! git diff --quiet $filename
  then
    diff_msg=`git diff --stat $filename`
    FILE_ROW_COUNT=$(cat $filename| wc -l) # 전체 줄 수 
    change_line=$(echo $diff_msg | cut -f 3 -d' ') # 변경된 줄 수 
    change=$(($change_line*100))
    change_percent=$(($change/$FILE_ROW_COUNT))

    echo "total : $FILE_ROW_COUNT"
    echo "changed : $change_line"
    echo "change * 100 : $change"
    echo "percent : $change_percent"

    if [ $change_percent -gt $n ]
    then
      git checkout auto-commit
      git add .
      git commit -m "Auto Commit: More than $n percent change detected."
      git push -u origin auto-commit
    fi
  fi

  sleep 10
done
