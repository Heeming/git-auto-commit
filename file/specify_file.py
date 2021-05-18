import subprocess
import baseProgram

# 특정 파일 지정
def specify_filename():
    file_name = str(input('Specify file name to detect : '))
    subprocess.call(['sh', './file_commit.sh', file_name])

# 특정 파일의 특정 구간 지정
def specify_filesection():
    specify_filename()
    
    file_section = str(input('Do you want to specify section? [y/n] '))

    if file_section == "y" or file_section == "Y":
        file_section_start = str(input('Specify start section number in file to detect : '))
        file_section_finish = str(input('Specify finish section number in file to detect : '))
        subprocess.call(['sh', './file_section_commit.sh', file_section_start, file_section_finish])
    else:
        subprocess.call(['sh', './file_commit.sh', file_name])

