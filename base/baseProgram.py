import subprocess
import time
import os

choice = 0

while choice != 6:
    print("Menu")
    print("1. New")
    print("2. Continue")
    print("3. Select mode")
    print("4. Git add file")
    print("5. Git push to branch")
    print("6. Delete auto-commit branch")
    print("7. Exit")
    choice = int(input(">> "))

    if choice == 1:
        subprocess.call(['sh', './setting.sh'])
        subprocess.call(['sh', './autoCommitProcess.sh'])
    
    elif choice == 2:
        subprocess.call(['sh', './continue.sh'])
        subprocess.call(['sh', './autoCommitProcess.sh'])

    elif choice == 3:
        subprocess.call(['sh', './killProcess.sh'])

        
        path = "./code/"

        file_list = os.listdir(path)


        py_list = [file for file in file_list if file.endswith(".py")]

        c_list = [file for file in file_list if file.endswith(".c")]
        for i in range(len(c_list)): c_list[i] = c_list[i].split('.')[0]

        java_list = [file for file in file_list if file.endswith(".java")]
        for i in range(len(java_list)): java_list[i] = java_list[i].split('.')[0]



        for i in range(len(py_list)) :
            p = subprocess.Popen(['python', path + py_list[i]], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            
            if err == '':
                pass
            else:
                subprocess.call(['sh', './continue.sh'])
                subprocess.call(['sh', './autoCommitProcess.sh', err])
            

        for i in range(len(c_list)) :
            p = subprocess.Popen(['sh', './exe_c.sh', path + c_list[i], c_list], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()

            if err == '':
                pass
            else:
                subprocess.call(['sh', './continue.sh'])
                subprocess.call(['sh', './error_autoCommitProcess.sh ' + err])

        for i in range(len(java_list)) :
            p = subprocess.Popen(['sh', './java_c.sh', path + java_list[i]], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()

            if err == '':
                pass
            else:
                subprocess.call(['sh', './continue.sh'])
                subprocess.call(['sh', './error_autoCommitProcess.sh ' + err])
        
    

    
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

        branch = str(input("Where to checkout?(branch_name) "))

        subprocess.call(['bash', './deleteBranch.sh', branch])

    elif choice == 7:
        subprocess.call(['bash', './killProcess.sh'])
        break

    else:
        print("Wrong Input! Please input again")