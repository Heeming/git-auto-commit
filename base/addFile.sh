#!/bin/bash

path="$1"

cd $path

filename="$2"
git add $filename
git commit -m "Add file::$filename"
git push -u origin auto-commit
