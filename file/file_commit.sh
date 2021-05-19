echo "Specify file"

file_name = "$1"

if ! git diff $file_name --quiet
then
  git checkout auto-commit
  git add $file_name
  git commit -m "Auto Commit: tracking only $file_name"
  git push -u origin auto-commit

else
  echo "Working tree clean. Nothing to commmit."
fi
