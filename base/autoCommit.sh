#!/bin/bash
path="$1"

cd $path

while :
do

  if ! git diff --quiet
  then
    git checkout auto-commit
    git add .
    git commit -m "Auto Commit"
    git push -u origin auto-commit

  fi
done
