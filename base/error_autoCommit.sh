#!/bin/bash
while :
do
  #echo "Checking for uncommitted changes in the git working tree"

  if ! git diff --quiet
  then
    git --no-pager checkout auto-commit
    git --no-pager add .
    git --no-pager commit -m "Error-Auto Commit/Error Message : $@"
    git --no-pager push -u origin auto-commit

  #else
    #echo "Working tree clean. Nothing to commmit."
  fi

  sleep 60
done
