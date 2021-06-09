echo "Checking file change for n%"

file_name = "$FILENAME"
percent = "$PERCENT"

git add $FILENAME
git diff --cached $FILENAME


# n%만 변경 감지 어떻게?