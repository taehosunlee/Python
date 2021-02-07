# =(alignment)를 통해 변수에 data를 저장함.
a= [1,2,3] # a에 [1,2,3]저장함.  C나 JAVA는 형식을 입력해줘야하지만, 파이썬은 스스로 판단(list)


# 함수들
# id(변수) : 변수가 가리키는 객체 주소값

print(id(a)) #2214548049984

b=a
print(id(b)) #2214548049984    a와 b는 가리키는 대상이 동일하다.

print(a==b)

a[1]=4
print(a)  #1,4,3
print(b)  #1,4,3   동일한 대상이므로,  a를 바꿔도 b도 같이 바뀜



### 그렇다면  a와 같은 값을 지니나, 객체주소가 다른 b를 만들고 싶다면?

# 1. : 사용

a=[1,2,3,4]
b=a[:]

print(a,b)
print(id(a),id(b))


# 2. copy모듈 사용

from copy import copy
a=[1,2,3]
b=copy(a)


print(a,b)
print(id(a),id(b))




## 변수 만드는 여러가지 방법
(a,b) = ("python","Java")  # 튜플로 동시에 변수지정 가능 , list로도 가능
print(a)
[a,b] = ['Python','Javaa']
print(a)

a=b="C++"
print(a+b)




# 조건, 반복문
# 조건부 표현식 (단축가능)
score = 70
message ="success" if score>=60 else "failure"
print(message)

# while,for
# break : 무한루프 종료.  continue : 이후 명령문 진행하지않고, 반복문의 처음으로 돌아감



# for : 리스트로도 가능
a = [(1,2),(3,4),(5,6)]
for (first,second) in a :
    print(first+second)


# for는 range 함수와 같이 쓰는 경우가 많다.
a= range(0,11) #0~10
a=list(a)
print(a)
add=0
for i in range(0,101) :
    add+=i

print(add) #55


# 구구단 만들기
for i in range(1,10) :
    gugu=[]
    for j in range(1,10) :
        gugu.append(i*j)
    print("{0}단 입니다 : ".format(i),gugu)


# 리스트 내포할 경우 좀 더 간단히 표현해보기
a=[1,2,3,4]
result=[num*3 for num in a]
result_a=[num*3 for num in a if num%2==0]  # 짝수만 가져오기.
print(result)
print(result_a)



# for 문 2개 연속 쓰기
result_b=[x*y for x in a for y in a]
print(set(result_b))
