'''
Quiz) 당신은 cocoa 서비스를 이용하는 택시 기사입니다.
50명의 승객과 매칭기회가 있을 때, 총 탑승 승객수를 구하는 프로그램을 작성하시오.

조건1 : 승객별 운행 소요시간은 5분~50분 사이의 난수로 정해집니다
조건2 : 당신은 소요시간 5분~15분 사이의 승객만 매칭해야합니다.

(출력문 예제)
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 18분)

총 탑승 승객 : 2분
'''


from random import *

users = range(1,51)
users = list(users)
print(users)


hour=[randint(1,50)]

i = 1
while i<50 :
    hour.append(randint(1,50))
    i=i+1

print(hour)


h=0
k=0
while h<50 : 
    if hour[h]<=15 and hour[h]>=5 :
        print("[O]")
    else :
        print("[ ]")

    print(h+1,"번째 손님, (소요시간 : " + str(hour[h]) + "분)")
    
    if hour[h]>=5 and hour[h]<=15 : 
        k=k+1
    h=h+1

print ( "총 탑승 승객 : {0}".format(k))  

###### 실패함.  답지 보기.  2:27


###답지
'''
from random import *

cnt = 0

for i in range(1,51) :
    time = randint(5,50)
    
    if time>=5 and time<=15 :
        print("[O]" + str(i) +"번째 손님 (소요시간 {0}".format(time))
        cnt=cnt+1
    elif time<5 or time>15 :
        print("[ ]" + str(i) + "번째 손님 (소요시간 {0}".format(time))

print("총 탑승 승객 : {0}".format(cnt))
'''