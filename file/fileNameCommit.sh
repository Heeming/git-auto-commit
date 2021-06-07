#!/bin/bash
while :
do
  #echo "Specify file name"

  file_name="$1"

  if ! git diff $file_name --quiet
  then
    #git config --global credential.helper store
    #git config --global credential.helpter cache

    #git --no-pager checkout -b specify_file

    git --no-pager checkout -b $file_name
    git --no-pager add $file_name
    git --no-pager commit -a -m "Auto Commit: tracking only $file_name"
    git --no-pager push -u origin auto-commit

  else
    #echo "Working tree clean. Nothing to commmit."
  fi

  sleep 60
done
