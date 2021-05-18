import subprocess
import specify_file

# 특정 파일의 특정 구간 지정
def specify_percent():
    specify_filename() # 특정 파일 지정
    
    percent = str(input('What percenttage change do you want to commit?'))

    subprocess.call(['sh', './file_npercent_change.sh', percent])

