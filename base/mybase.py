import subprocess
import time
import os
import logging
import traceback

path = "./code/"
file_list = os.listdir(path)

print(file_list)

py_list = [file for file in file_list if file.endswith(".py")]
print(py_list)

#c_list = [file for file in file_list if file.endswith(".c")]
#java_list = [file for file in file_list if file.endswith(".java")]


massage = ''

for i in range(len(py_list)) :
    try :
        print("&&")
        massage = subprocess.check_output( ['python', path + py_list[i]], universal_newlines=True, stderr=subprocess.PIPE)
        print("&&")
        
    except Exception as ex:
        print(massage)
        print(subprocess.Popen.communicate())
        branch = str("error")
        msg = str(ex)

        print("!!!!!!!!!!!commit")
        print(ex)
        
        #subprocess.call(['sh', './continue.sh'])
        #subprocess.call(['sh', './autoCommitProcess.sh'])