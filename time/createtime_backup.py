import os
import datetime as dt

def auto_commit():
    # base 파일 실행 명령어
    print("백업되었습니다.")

def createtime(file):
    if os.path.isfile(file):
        ctime = os.path.getctime(file)  # create time 생성
        ymd_ctime = dt.datetime.fromtimestamp(ctime)  # 출력 형태를 ymd의 format으로 변경
        return ymd_ctime

def start(file):
    start_time = createtime(file)
    return start_time

def stop():
    stop_time = dt.datetime.now()
    return stop_time

def delta(start, stop, n):
    delta_time = (stop - start) / n
    print(delta_time)

# def ctime_based_autocommit(file, start, stop, n):
    # 만약 delta(start,stop, n)의 시간 단위가 자연수이거나 분 단위가 자연수이면 -> ~.hour, ~.minute으로 해결하려고 했는데 되지를 않네요...
        # auto commit을 한다.

fname = str(input('Enter your file name : '))  # GUI에서 사용자가 특정 파일 선택했다고 가정
n = int(input('Enter the minutes you want to set up : '))  # GUI에서 사용자가 분을 세팅했다고 가정
delta(start(fname), stop(), n)