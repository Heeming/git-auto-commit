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

    # echo "Last commit is not merged."
    # echo -e "Where to push?(branch_name) \c"
    # read branch
    # echo -e "Write commit message: \c"
    # read -a message

    git checkout $branch
    git branch -D auto-commit
    git push origin $branch

    git checkout $branch
    # git merge --squash auto-commit
    # git commit -m "${message[@]}"
    # git push -u origin master

    git push origin --delete auto-commit

else
    # message="$2"

    git checkout $branch
    git branch -D auto-commit


    git checkout $branch
    # git merge --squash auto-commit
    # git commit -m "${message[@]}"
    # git push -u origin master

    git push origin --delete auto-commit


fi
