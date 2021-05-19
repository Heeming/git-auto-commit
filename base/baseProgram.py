import subprocess
import time
import os

choice = 0

while choice != 6:
    print("Menu")
    print("1. New")
    print("2. Continue")
    print("3. Error Backup mode")
    print("4. Git add file")
    print("5. Git push to branch")
    print("6. Exit")
    choice = int(input(">> "))

    if choice == 1:
        subprocess.call(['sh', './setting.sh'])
        subprocess.call(['sh', './autoCommitProcess.sh'])
    
    elif choice == 2:
        subprocess.call(['sh', './continue.sh'])
        subprocess.call(['sh', './autoCommitProcess.sh'])

    elif choice == 3:
        path = "./code/"
        file_list = os.listdir(path)

        py_list = [file for file in file_list if file.endswith(".py")]
        #c_list = [file for file in file_list if file.endswith(".c")]
        #java_list = [file for file in file_list if file.endswith(".java")]

        for i in range(len(py_list)) :
            try :
                subprocess.check_output( ['python', path + py_list[0]], universal_newlines=True )
            except Exception as ex:
                branch = str("error")
                msg = str(ex)

                subprocess.call(['sh', './continue.sh'])
                subprocess.call(['sh', './autoCommitProcess.sh'])
        
    
    elif choice == 4:
        subprocess.call(['bash', './killProcess.sh'])

        filename = str(input("What file to add?(file_name) "))
        subprocess.call(['sh', './addFile.sh', filename])

        subprocess.call(['sh', './continue.sh'])
        subprocess.call(['sh', './autoCommitProcess.sh'])

    elif choice == 5:
        subprocess.call(['bash', './killProcess.sh'])
        branch = str(input("Where to push?(branch_name) "))
        msg = str(input("Write commit message: "))
        
        subprocess.call(['sh', './userCommit.sh', branch, msg])

        subprocess.call(['sh', './continue.sh'])
        subprocess.call(['sh', './autoCommitProcess.sh'])

    elif choice == 6:
        subprocess.call(['bash', './killProcess.sh'])

    else:
        print("Wrong Input! Please input again")