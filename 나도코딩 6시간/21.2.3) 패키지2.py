# 여태껏 사용한 모듈, 패키지는 동일 라이브러리에 있었다.

# 위치를 확인하고 싶다면?


from travel import *
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))