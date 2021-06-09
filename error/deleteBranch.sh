#!/bin/bash
  
if ! git diff --quiet
then
    git --no-pager checkout auto-commit
    git --no-pager add .
    git --no-pager commit -m "Auto Commit"
    git --no-pager push -u origin auto-commit

    # echo "Last commit is not merged."
    # echo -e "Where to push?(branch_name) \c"
    # read branch
    # echo -e "Write commit message: \c"
    # read -a message

    branch="$1"
    # message="$2"

    git checkout $branch
    # git merge --squash auto-commit
    # git commit -m "${message[@]}"
    # git push -u origin master

    git push origin --delete auto-commit
    git branch -D auto-commit

else
    branch="$1"
    # message="$2"

    git checkout $branch
    # git merge --squash auto-commit
    # git commit -m "${message[@]}"
    # git push -u origin master

    git push origin --delete auto-commit
    git branch -D auto-commit

fi
