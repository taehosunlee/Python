# import 없이 쓰는 함수 python built in function

# input : 사용자 입력을 받는 함수
"""
language = input("무슨 언어를 좋아하세요?")
print("{0}은 아주 좋은 언어입니다.".format(language))
"""

# dir : 어떤 객체를 넘겨줬을 때, 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
"""
print(dir())
import random # random 외장함수를 가져온다
print(dir())
import pickle
print(dir())
print(dir(random))
"""


# lst = [1,2,3]
# print(dir(lst)) # list에서 쓸 수 있는 함수들이 나옴

name = "Jim"
print(dir(name))