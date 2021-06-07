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

c_list = [file for file in file_list if file.endswith(".c")]
java_list = [file for file in file_list if file.endswith(".java")]



for i in range(len(py_list)) :
    p = subprocess.Popen(['python', path + py_list[i]], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    
    if err == '':
        pass
    else:
        subprocess.call(['sh', './continue.sh'])
        print('/////////')
        subprocess.call(['sh', './autoCommitProcess.sh', err])
    
'''
for i in range(len(c_list)) :
#    p = subprocess.Popen(['python', path + py_list[i]], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    if err == '':
        pass
    else:
        subprocess.call(['sh', './continue.sh'])
        subprocess.call(['sh', './error_autoCommitProcess.sh ' + err])

for i in range(len(java_list)) :
#    p = subprocess.Popen(['python', path + py_list[i]], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    if err == '':
        pass
    else:
        subprocess.call(['sh', './continue.sh'])
        subprocess.call(['sh', './error_autoCommitProcess.sh ' + err])
        '''