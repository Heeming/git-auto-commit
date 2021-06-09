#!/bin/bash
while :
do
  # echo "Specify file name"
  specify_filename="$1"

  if ! git diff --quiet $specify_filename 
  then
    git checkout auto-commit
    git add $specify_filename
    git commit -m "Auto Commit: tracking $specify_filename"
    git push -u origin auto-commit

  # else
    #echo "Working tree clean. Nothing to commmit."
  fi

  sleep 60
done
