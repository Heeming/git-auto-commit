#!/bin/base

path="$1"

cd $path

crtime="$2"

interval="$3"
min=$(($interval/60))

filename="$4"

zero=0

while :
do
  now=`date +%s`
  sub=$(($now-$crtime))
  mod=$(($sub%$interval))

  if ! git diff --quiet 
  then
    if [ $mod -eq $zero ]
    then
      git checkout auto-commit
      git add .
      git commit -m "Auto Commit: Every $min past from creation time of $filename"
      git push -u origin auto-commit
    fi
  fi
done
