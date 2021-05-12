echo "Checking for uncommitted changes in the git working tree"

if ! git diff --quiet
then
  git checkout auto-commit
  git add .
  git commit -m "Auto Commit"
  git push -u origin auto-commit

else
  echo "Working tree clean. Nothing to commmit."
fi
