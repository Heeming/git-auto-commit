#!/bin/sh

path="$1"

cd $path

crtime="$2"

interval="$3"

zero=0

while :
do
  now=`date +%s`
  sub=$(($now-$crtime))
  mod=$(($sub%$interval))

  if [[ ! git diff --quiet ]] && [[ $mod = $zero ]]
  then
    git checkout auto-commit
    git add .
    git commit -m "Auto Commit"
    git push -u origin auto-commit
  fi
done
