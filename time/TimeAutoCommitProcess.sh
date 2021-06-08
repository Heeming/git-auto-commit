#!/bin/bash

do
  #echo "Checking for uncommitted changes in the git working tree"

  if ! git diff --quiet
  then
    git --no-pager checkout auto-commit
    git --no-pager add .
    git --no-pager commit -m "Auto Commit"
    git --no-pager push -u origin auto-commit

  #else
    #echo "Working tree clean. Nothing to commmit."
  fi

done