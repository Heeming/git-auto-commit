# GUI
base program에 GUI를 추가

## Files

Program
- program.py : base program에 GUI가 추가된 파일. 모든 UI가 통합되어 있다.

개별 UI Files
- checkoutUI.py      : branch checkout 시 어떤 브랜치로 checkout하는지 설정하는 창
- cloneRepoUI.py     : Repository clone 시 clone할 repository 정보를 입력하는 창
- gitAutoCommitUI.py : 현재 git-auto-commit을 실행하고 있는 repository control 창
- initRepoUI.py      : local에 새로운 repository 생성 시 생성 할 repository 정보를 입력하는 창
- pushUI.py          : git push 시 commit message와 branch를 지정하는 창
- repoSelectUI.py    : 어떤 repository에 git-auto-commit을 실행할 것인지 선택하는 창 
- selectMode.py      : git-auto-commit의 사용자 조건를 선택하는 창
- signInUI.py        : 로그인 창


## Preconditions
- pyqt5가 install 되어 있어야 한다.
 -  설치 방법 (linux-using python3) `pip3 install pyqt5`

## How to use?
 1. 모든 폴더를 모두 다운 받는다
 2. gui 폴더의 program.py를 실행시킨다

## 추가 구현 예정
