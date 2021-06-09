#!/bin/bash
echo "git add file"

if [ "$1" = "" ]
then echo "please write file name which need to git add"
else
  filename="$1"
  git add $filename
  git commit -m "Add file::$filename"
  git push -u origin auto-commit
fi
