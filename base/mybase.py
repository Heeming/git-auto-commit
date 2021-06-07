import subprocess
import time
import os

path = "./code/"
file_list = os.listdir(path)

print(file_list)

py_list = [file for file in file_list if file.endswith(".py")]
print(py_list)

#c_list = [file for file in file_list if file.endswith(".c")]
#java_list = [file for file in file_list if file.endswith(".java")]


for i in range(len(py_list)) :
    try :
        print("&&")
        print("11\n", subprocess.check_output( ['python', path + py_list[i]], universal_newlines=True), "\n11" )
        print("&&")
        
    except Exception as ex:
        branch = str("error")
        msg = str(ex)

        print("!!!!!!!!!!!commit")
        
        subprocess.call(['sh', './continue.sh'])
        subprocess.call(['sh', './autoCommitProcess.sh'])