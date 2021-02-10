
# Quiz) 당신의 학교에서는 파이썬 코딩대회를 주최합니다.
# 참석율을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
# 댓글 작성자들 중, 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상, 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되, 중복불가
# 조건3 : random 모듈의 shuffle과 sample을 활용


# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다



# (활용 예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,3))  # lst 목록에서 , 랜덤으로 3개를 뽑겠다.

from random import *

lst = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
chicken = {randint(1,20)}
coffee = lst - chicken

print(chicken)
print(coffee)
coffee = list(coffee)
print(sample(coffee,3))  # sample문은 List에서만 쓸 수 있다.
chicken = list(chicken)



print("-- 당첨자 발표 --")
print("치킨 당첨자 : ",chicken)
print("커피 당첨자 : ",sample(coffee,3))
print("-- 축하합니다 --")


## 답지 ##

users = range(1,21)  # 1부터 21 직전까지.  1~20까지 숫자 생성
# print(type(users))
# print(users)

users = list(users)
# print(type(users))
print(users)
shuffle(users)  # shuffle은 리스트만 된다.
print(users)

winners = sample(users,4) # sample은 List에서만 가능

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")

############################################  차집합으로 하기.

chicken = sample(users,1)  #sample은 list. 차집합 불가 --> set(집합) 으로 바꿔주기.
print(type(chicken))
print(type(winners))
chicken = set(chicken)
winners = set(winners)

print(type(chicken))
print(type(winners))

coffee = winners - chicken



print("-- 당첨자 발표 --")
print(f"치킨 당첨자 : ",chicken)
print(f"커피 당첨자 : ",coffee)
print("-- 축하합니다 --")