import datetime as dt
import subprocess
import time
import os

# auto commit 실행 - subprocess에서 에러가 계속 나서 주석처리해놓음
def auto_commit():
    print("auto commit을 시행합니다")
    #subprocess.call(['sh', './continue.sh'])
    #subprocess.call(['sh', './TimeAutoCommitProcess.sh'])


# 파일생성시간을 계산
def createtime(file):
    if os.path.isfile(file):
        ctime = os.path.getctime(file)  # create time 생성
        ymd_ctime = dt.datetime.fromtimestamp(ctime)  # 출력 형태를 ymd의 format으로 변경
        return ymd_ctime


# 파일생성시간을 timestamp를 이용해 float형 숫자로 바꾼 후, float형을 int형으로 변환
def start(filename):
    start_time = createtime(filename)
    start_time_timestamp = int(start_time.timestamp())
    return start_time_timestamp


# 현재시간을 timestamp를 이용해 float형 숫자로 바꾼 후, float형을 int형으로 변환
def stop():
    stop_time = dt.datetime.now()
    stop_time_timestamp = int(stop_time.timestamp())
    return stop_time_timestamp


# (현재 시간 - 파일 생성 시간) % 60n을 통해서 나머지 계산
def remainder(filename, start, stop, n):
    time_remainder = (stop - start(filename)) % (60 * n)
    return time_remainder


# 나머지가 0이 되면 autocommit 실행
def ctime_based_autocommit(filename, start, stop, n):
    print("시도 중") # 함수가 실행될 때마다 '시도 중'을 출력
    print(remainder(filename, start, stop, n)) # 나머지 출력
    if remainder(filename, start, stop, n) == 0:
        # auto commit 실행 - subprocess에서 에러가 계속 나서 주석처리해놓음
        #subprocess.call(['sh', './continue.sh'])
        #subprocess.call(['sh', './TimeAutoCommitProcess.sh'])
        print("백업되었습니다.")

choice = 0

while choice != 8:
    print("Menu")
    print("1. New")
    print("2. Continue")
    print("3. Time backup mode")
    print("4. Create time backup mode")
    print("5. Error Backup mode")
    print("6. Git add file")
    print("7. Git push to branch")
    print("8. Exit")
    choice = int(input(">> "))

    if choice == 1:
        subprocess.call(['sh', './setting.sh'])
        subprocess.call(['sh', './autoCommitProcess.sh'])

    elif choice == 2:
        subprocess.call(['sh', './continue.sh'])
        subprocess.call(['sh', './autoCommitProcess.sh'])

    elif choice == 3:
        num = int(input('Enter the minutes you want to set up : '))  # GUI에서 사용자가 분을 세팅했다고 가정
        while True:
            try:
                print("시도")
                time.sleep(num*60)
                auto_commit()
            except Exception as ex:  # GUI에서 체크버튼 해제되었다고 가정
                print(ex)

    elif choice == 4:
        filename = str(input('Enter your file name : '))  # GUI에서 사용자가 특정 파일 선택했다고 가정
        n = int(input('Enter the minutes you want to set up : '))  # GUI에서 사용자가 분을 n으로 세팅했다고 가정
        while True:
            try:
                print("시도")
                time.sleep(1)
                ctime_based_autocommit(filename, start, stop(), n)  # 파일 생성 시간을 기준으로 n분마다 auto commit하는 걸 백그라운드에서 실행
            except Exception as ex:  # GUI에서 체크버튼 해제되었다고 가정
                print(ex)
            #if :  # GUI에서 체크버튼 해제되었다고 가정
                #print("버튼 해제2")
                #break

    elif choice == 5:
        path = "./code/"
        file_list = os.listdir(path)

        py_list = [file for file in file_list if file.endswith(".py")]
        # c_list = [file for file in file_list if file.endswith(".c")]
        # java_list = [file for file in file_list if file.endswith(".java")]

        for i in range(len(py_list)):
            try:
                subprocess.check_output(['python', path + py_list[0]], universal_newlines=True)
            except Exception as ex:
                branch = str("error")
                msg = str(ex)

                subprocess.call(['sh', './continue.sh'])
                subprocess.call(['sh', './autoCommitProcess.sh'])


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
    else:
        print("Wrong Input! Please input again")