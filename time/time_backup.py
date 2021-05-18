import schedule

def auto_commit():
    # base 파일 실행 명령어
    print("백업되었습니다.")

def time_based_autocommit(n):
    schedule.every(n).minutes.do(auto_commit) # n분마다 auto_commit 실행

n = int(input('Enter the minutes you want to set up : ')) # GUI에서 사용자가 분을 세팅했다고 가정
time_based_autocommit(n) # GUI에서 사용자가 분을 세팅했다고 가정