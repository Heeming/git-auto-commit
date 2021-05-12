import subprocess

autoCommit = str(input('do autoCommit?[y/n] '))

if autoCommit == "y" or autoCommit == "Y":
    subprocess.call(['sh', './autoCommit.sh'])

pushToMaster = str(input('push to other branch?[y/n] '))

if pushToMaster == 'y' or pushToMaster == 'Y':
    branch = str(input("Where to push?(branch_name) "))
    msg = str(input("Write commit message: "))
    
    subprocess.call(['sh', './userCommit.sh', branch, msg])