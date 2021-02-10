# 내장함수완 다르게 직접 import 해야함  list of python modules



# import random

# lst = [1,5,4,7]
# print(lst)
# random.shuffle(lst)

# print(lst)



# glob : 경로 내의 폴더 / 파일 목록 조회(윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일. 근데 나도코딩6시간에 들어가있어, .py 파일이 없다고 나온다.



# os : 운영체제에서 제공하는 기본 기능

import os
# print(os.getcwd()) # 현재 디렉토리
# folder = "sample_dir"

# if os.path.exists(folder) : # sample_dir이란 폴더가 있으면, 아래 구문 실행
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder) #폴더 삭제
#     print(folder,"폴더를 삭제하였습니다")
# else:
#     os.makedirs(folder) #폴더 생성
#     print(folder,"폴더를 생성하였습니다")

# print(os.listdir()) # 해당 폴더에 있는것들 알려줌.


# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%M-%d %H:%M:%S")) #연,월,일,시,분,초

import datetime
print("오늘 날짜는", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) #100일 저장
print("우리가 만난지 100일은", today+td) #오늘부터 100일 후