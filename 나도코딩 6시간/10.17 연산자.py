# print (3>=5) #TRUE, FALSE
# print (2**10) #제곱 2^10
# print (5%3) #나머지 구하기
# print (18//3) #몫 구하기
# print (5>=5) #TRUE

# print (3 == 3) #앞과 뒤가 똑같은지 확인  TRUE
# print (4 == 2) #FALSE
# print (3+4 ==7) #TRUE 같다
# print (1 != 3) #TRUE  같지 않다
# print (not(1 != 3)) #TRUE 의 not(반대) = FALSE  # print (not True)
# print (not True)

# print ((3>0) and (3<5)) #True
# print ((3>0) & (3<5)) #True
# print ((3>0) or (3>5)) #True  하나만 맞으면 Ture
# print (3<5>4)  #True  세개 연속해서도 가능

# print (3+4*4) #19
# print ((3+4)*2) #14

'''number = 2+3*4  #14
print(number)
number = number +2  #16
print(number)
number +=2   # number에다 +2를 더한다.
print(number)
number *=3  #number에 *3을 한 수를 넣는다
print(number)
number /=6 #number를 6으로 나눈 수를 넣늗나
print (number)
number %=7 # 나머지 구하기
print (number)'''

'''print (abs(-5))  # 절대값. 5
print (pow(4,2)) # 4의 2승 16
print (max(5,12,16,30))  #최대값
print (min(5,12,16,30))  #최소값
print (round(3.6))  #반올림 (정수)

from math import *  # math library 안에 있는 모든 함수를 쓰겠다.  floor 쓸 수 있어짐.
print (floor(3.64))  #내림(정수)
print (ceil(3.44)) #올림
print (sqrt(16)) # 4.  루트. 제곱근 구하기
print (sqrt(2))'''

from random import * # random library 쓴다.
# print(random()) # 0.0~1.0 미만의 임의의 값 생성
# print(random() * 10) # 0.0~10.0 미만의 임의의 값 생성
# print(int(random() * 10))  # 0~10 미만의 임의의 정수 생성
# print(int(random() * 10)+1)  # 1~10 이하의 임의의 정수 생성


#print(int(random()*45+1)) #1~45 이하의 임의의 정수

# 좀 더 간단히!
#print(randrange(1,46)) # 1~46미만의 임의의 값을 생성하라

#print(randint(1,45)) # 1~45 이하의 임의의 값 생성


from random import *
print ( "당신은 최근에 코딩 스터디 모임을 새로 만들었습니다")
total = 4
online = 3
offline = 1
print ( "월 "+str(total)+"회 스터디를 하는데 "+str(online)+"번은 온라인으로 하고")
print ( offline,"번은 오프라인으로 하기로 했습니다")

#offline 날짜 뽑기 (random형)
#조건1 : 랜덤으로 날짜 뽑아야함
#조건2 : 월별 날짜는 다름을 감안, 1~28일 사이로
#조건3 : 매월1~3일은 스터디 준비로 제외
# offdate = randrange(4,29)
offdate = randint(4,28)
# offdate = int(random()*25+4)

# randrang(4,29) = randint(4,28) = int(random()*25+4)

print ("오프라인 수업 날짜는 " ,offdate,"일로 정해졌습니다")
print ("오프라인 수업 날짜는 " +str(offdate)+"일로 정해졌습니다")