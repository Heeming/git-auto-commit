import subprocess
import time
import os

def auto_commit():
    subprocess.call(['sh', './continue.sh'])
    subprocess.call(['sh', './autoCommitProcess.sh'])
    print("백업되었습니다.")

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

def specify_percent():
    specify_filename() # 특정 파일 지정
    
    percent = str(input('What percenttage change do you want to commit?'))

    subprocess.call(['sh', './file_npercent_change.sh', percent])
    
choice = 0

while choice != 9:
    print("Menu")
    print("1. New")
    print("2. Continue")
    print("3. Specify file name mode")
    print("4. Specify file section mode")
    print("5. Specify percent of all files mode")
    print("6. Git add file")
    print("7. Git push to branch")
    print("8. Delete auto-commit branch")
    print("9. Exit")
    choice = int(input(">> "))

    if choice == 1:
        subprocess.call(['sh', './setting.sh'])
        subprocess.call(['sh', './autoCommitProcess.sh'])
    
    elif choice == 2:
        subprocess.call(['sh', './continue.sh'])
        subprocess.call(['sh', './autoCommitProcess.sh'])

    elif choice == 3:
        file_name = str(input('Specify file name to detect : '))
        #subprocess.call(['sh', './fileNameProcess.sh', file_name])
        
    elif choice == 4:
        path = "./code/"
        file_list = os.listdir(path)

        py_list = [file for file in file_list if file.endswith(".py")]
        #c_list = [file for file in file_list if file.endswith(".c")]
        #java_list = [file for file in file_list if file.endswith(".java")]

        #file_name = str(input('Specify file name to detect : '))

        for i in range(len(py_list)) :
            try :
                subprocess.check_output( ['python', path + py_list[0]], universal_newlines=True )
                #subprocess.call(['sh', './fileNameProcess.sh', file_name])
            except Exception as ex:
                branch = str("error")
                msg = str(ex)

                subprocess.call(['sh', './continue.sh'])
                subprocess.call(['sh', './autoCommitProcess.sh'])

    elif choice == 5:
        pass

    elif choice == 6:
        subprocess.call(['bash', './killProcess.sh'])

        filename = str(input("What file to add?(file_name) "))
        subprocess.call(['sh', './addFile.sh', filename])

        subprocess.call(['sh', './continue.sh'])
        subprocess.call(['sh', './autoCommitProcess.sh'])

    elif choice == 7:
        subprocess.call(['bash', './killProcess.sh'])
        branch = str(input("Where to push?(branch_name) "))
        msg = str(input("Write commit message: "))
        
        subprocess.call(['sh', './userCommit.sh', branch, msg])

        subprocess.call(['sh', './continue.sh'])
        subprocess.call(['sh', './autoCommitProcess.sh'])

    elif choice == 8:
        subprocess.call(['bash', './killProcess.sh'])

        branch = str(input("Where to checkout?(branch_name) "))

        subprocess.call(['bash', './deleteBranch.sh', branch])

    elif choice == 9:
        subprocess.call(['bash', './killProcess.sh'])
        break

    else:
        print("Wrong Input! Please input again")