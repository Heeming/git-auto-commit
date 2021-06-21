#!/bin/bash
path="$1"  
branch="$2"
cd $path

if ! git diff --quiet
then

    git checkout auto-commit
    git add .
    git commit -m "Auto Commit"
    git push -u origin auto-commit

    git checkout $branch
    git branch -D auto-commit
    git push origin $branch

    git checkout $branch

    git push origin --delete auto-commit

else
    git checkout $branch
    git branch -D auto-commit


    git checkout $branch

    git push origin --delete auto-commit
fi
