import subprocess
import time
import os

choice = 0

while choice != 10:
    print("Menu")
    print("1. New")
    print("2. Continue")
    print("3. Specify file name mode")
    print("4. Change more than n percent mode")
    print("5. Specify line section mode")
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
        subprocess.call(['bash', './killProcess.sh'])
        subprocess.call(['sh', './setting.sh'])

        specify_filename = str(input("Specify file_name to detect : "))

        subprocess.call(['sh', './file_addFile.sh', specify_filename])
        subprocess.call(['sh', './filename.sh', specify_filename])

    elif choice == 4:
        subprocess.call(['bash', './killProcess.sh'])
        subprocess.call(['sh', './setting.sh'])

        n = int(input("Input percent : "))
        filename = str(input("Add filename : "))

        subprocess.call(['sh', './addFile.sh', filename])
        subprocess.call(['sh', './file_npercent.sh', filename, n])

    elif choice == 5:
        subprocess.call(['bash', './killProcess.sh'])
        subprocess.call(['sh', './setting.sh'])

        filename = str(input("Add filename : "))
        n = int(input("Start line : "))
        m = int(input("Finish line : "))

        subprocess.call(['sh', './addFile.sh', filename])
        subprocess.call(['sh', './file_section.sh', filename, n, m])

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