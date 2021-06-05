import schedule
import subprocess
import time

def auto_commit():
    subprocess.call(['sh', './continue.sh'])
    subprocess.call(['sh', './autoCommitProcess.sh'])
    print("백업되었습니다.")

def time_based_autocommit(n):
    schedule.every(n).minutes.do(auto_commit) # n분마다 auto_commit 실행

num = int(input('Enter the minutes you want to set up : ')) # GUI에서 사용자가 분을 세팅했다고 가정

# 백그라운드에서 계속 실행하는 거 어떻게? 모르겠어서 일단 while true로 해놓음
while True:
    schedule.run_pending()
    time_based_autocommit(num) # GUI에서 사용자가 분을 세팅했다고 가정