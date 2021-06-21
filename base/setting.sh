#!/bin/bash
path="$1"

cd $path

git config --global credential.helper store
git config --global credential.helpter cache

git checkout -b auto-commit
