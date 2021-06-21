# 사용자 조건에 따른 git-auto-commit 시스템
The project git-auto-commit with user customizing in 2021 Open Source Software Project course.

## Introduction
사용자가 설정한 조건에 따라 file change를 git에 자동으로 commit & push 해주는 시스템이다. 사용자가 auto-commit을 사용할 폴더와 github repository를 등록하면 repository에 auto-commit 전용 branch를 새로 생성한다. 사용자 조건에 따라 auto-commit을 하며, 해당 commit은 해당 branch에 기록된다. 사용자가 프로그램에서 auto-commit을 해제하면 branch를 삭제한다.

<img src="https://user-images.githubusercontent.com/60775453/122745173-af833780-d2c3-11eb-9241-91c39e0eaf03.png" width=80% height=80% >

## Features
기본 사용자 조건 : 사용자가 모든 파일에 대해서, 혹은 특정 부분/특정 파일을 지정하여 사용자 조건을 customizing할 수 있다. 
- [base]
  - repository 변경사항 감지 시 자동 commit
  - background process로 생성
  - auto commit 전용 branch 생성 및 해당 branch에만 push
  - git add file 기능
  - user-commit & push 기능
  -  auto-commit 해제 및 branch 삭제
- [time]
  - 일정 시간마다 commit
  - 파일 생성 시점 기준으로 사용자가 설정한 시간마다 자동으로 저장하고 commit
- [error]
  - 코드 컴파일 중 에러 발생 시 commit
  - 에러 메세지 발생 시 commit
  - 실행 중단 시 commit
- [file]
  - 사용자가 특정 파일을 지정하면 그 파일에서만 변경 사항 감지 후 commit
  - 전체 코드의 n%가 변경된 경우 commit
- [GUI]
  - 위의 기본 사용자 조건을 사용자가 Customizing을 쉽게 달성할 수 있도록 하기 위한 GUI 개발

## Quick Start


## Documents
- [base](https://github.com/Heeming/git-auto-commit/blob/master/base/README.md)
- [time](https://github.com/Heeming/git-auto-commit/blob/master/time/README.md)
- [error](https://github.com/Heeming/git-auto-commit/blob/master/error/README.md)
- [file](https://github.com/Heeming/git-auto-commit/blob/master/file/README.md)
- [GUI](https://github.com/Heeming/git-auto-commit/blob/master/gui/README.md)

## License
[MIT license](https://opensource.org/licenses/MIT)
```
MIT License

Copyright (c) 2021 Heeming

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
