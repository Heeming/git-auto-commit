echo "UserCommit and Push"

branch="$1"
message="$2"

git checkout $branch
git merge --squash auto-commit
git commit -m "$message"
git push -u origin master

git checkout -b auto-commit-temp
git merge --no-edit auto-commit

git commit --amend -m "User makes commit and push it to user branch."
git push -f

git branch -d auto-commit
git branch -m auto-commit-temp auto-commit

git push -u origin auto-commit