import os
import datetime as dt
import schedule
import subprocess
import time

# 백업 시간이 아직 되지 않을 경우 출력할 문구
def not_commit():
    print("백업 시간이 아직 되지 않았습니다.")

# 파일생성시간을 계산
def createtime(file):
    if os.path.isfile(file):
        ctime = os.path.getctime(file)  # create time 생성
        ymd_ctime = dt.datetime.fromtimestamp(ctime)  # 출력 형태를 ymd의 format으로 변경
        return ymd_ctime

# 파일생성시간을 timestamp를 이용해 float형 수로 변환
def start(file):
    start_time = createtime(file)
    start_time_timestamp = start_time.timestamp()
    return start_time_timestamp

# 현재시간을 timestamp를 이용해 float형 수로 변환
def stop():
    stop_time = dt.datetime.now()
    stop_time_timestamp = stop_time.timestamp()
    return stop_time_timestamp

# (현재 시간 - 파일 생성 시간) % 60n을 통해서 나머지 계산
def remainder(start, stop, n):
    time_remainder = (stop - start) % (60 * n)
    return time_remainder

# 나머지가 0이 되면 autocommit 실행
def ctime_based_autocommit(file, start, stop, n):
    # 이걸 백그라운드에서 계속 실행하려면 어떻게???
    if remainder(start, stop, n) == 0:
        subprocess.call(['sh', './continue.sh'])
        subprocess.call(['sh', './autoCommitProcess.sh'])
    else:
        not_commit()


fname = str(input('Enter your file name : '))  # GUI에서 사용자가 특정 파일 선택했다고 가정
n = int(input('Enter the minutes you want to set up : '))  # GUI에서 사용자가 분을 n으로 세팅했다고 가정

remainder(start(fname),stop(), n) # (현재 시간 - 파일 생성 시간) % 60n을 통해서 나머지 구하기
ctime_based_autocommit(fname, start(fname), stop(), n) # 파일 생성 시간을 기준으로 n분마다 auto commit하는 걸 백그라운드에서 실행