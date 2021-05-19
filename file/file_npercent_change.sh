echo "Checking file change for n%"

file_name = "$1"

percent = "$2"

git add $file_name

git diff $file_name

# n%만 변경 감지 어떻게?