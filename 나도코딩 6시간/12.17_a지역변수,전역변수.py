#지역변수는 함수 내에서만 쓸 수 있는것.  함수가 호출되면 사용됐다가 끝나면 사라짐
# 전역변수는 프로그램 내 어디서든 쓸 수 있음

gun = 10
'''
def checkpoint(soldiers) : #경계근무 나가는 군인 수
    gun = gun-soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))

checkpoint(2) #2명이 경계근무 나감.
print("남은 총 : {0}".format(gun))  

## 에러남!! gun은 함수 바깥에선 정의됐지만, 함수 내에선 값이 설정 안됨. 함수 내 gun은 값이 없으므로 err발생
## --> 이게 바로 지역변수
'''


def checkpoint(soldiers) : #경계근무 나가는 군인 수
    gun=20
    gun = gun-soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun)) #전역변수 gun 10

checkpoint(2) #2명이 경계근무 나감.  여기서 쓰이는 gun은 함수 내 지역변수 20
print("남은 총 : {0}".format(gun))  #전역변수 gun 10

print("------------구분-----------")

def checkpoint2(soldiers) : #경계근무 나가는 군인 수
    global gun # 전역변수 gun 10 사용하겠다.
    gun = gun-soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

    
print("전체 총 : {0}".format(gun)) #전역변수 gun 10

checkpoint2(2) #2명이 경계근무 나감.  여기서 쓰이는 gun은 함수 내 전역변수 10
print("남은 총 : {0}".format(gun))  #전역변수 gun-2 8


print("---------------구분2---------------------")  #일반적으로 전역변수를 많이쓰면 코드도 복잡해지고 어려워져서
# 권장되는 방법은 아니다. 가급적 함수의 전달값으로 parameter로 던져서 쓰고 반환값으로 받는 방법을 사용한다.

def checkpoint_ret(gun,soldiers) : 
    gun = gun-soldiers
    print("함수 내 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun)) 

gun = checkpoint_ret(gun,2)   # 그냥 checkpoint_ret(gun,2)  만 쓰면,  return값 못받는다.
print("남은 총 : {0}".format(gun)) 

print("--------------------------")
print("전체 총 : {0}".format(gun)) 
checkpoint_ret(gun,2)   # 그냥 checkpoint_ret(gun,2)  만 쓰면,  return값 못받는다.
print("남은 총 : {0}".format(gun)) 