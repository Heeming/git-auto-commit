#!/bin/bash
path="$1"

cd $path

specify_filename="$2"

while :
do

  if ! git diff --quiet $specify_filename
  then
    git checkout auto-commit
    git add .
    git commit -m "Auto Commit: tracking $specify_filename"
    git push -u origin auto-commit
  fi
done
