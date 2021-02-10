# 에러가 발생했을 때 그 에러에 대해 예외처리 해주는 것
# 계산기에 숫자를 입력해야하는데 문자를 입력했다던지, 홈페이지에 주소를 잘못 적거나, 사용자가 많아 서버 접속이 안된다던지.

# try 밑에 있는걸 해보다가, 에러가 발생했을 때 except를 찾아서,  해당 에러이면 그 밑에껄 실행한다.
'''
try :   
    print("나누기 전용 계산기입니다")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : "))) # int 씌워주는건 정수 뽑을거라.
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0]/nums[1]))    만약 nums[2]가 없는데 아래에서 뽑으려고 한다면?? IndexError
    print( "{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))


except ValueError : 
    print("에러! 잘못된 값을 입력하였습니다.")


except ZeroDivisionError as err : #해당 err를 그대로 표시하겠다.  as err -> print(err)
    print(err)

except Exception as err :   # 그 외 모든 에러발생.  익셉션을 err로 받고, 무슨 err인지 확인가능
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)



#############################에러 발생시키기_raise  ###############################

try :   
    print("한 자리 숫자 나누기 전용 계산기입니다")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1>=10 or num2 >=10 :
        raise ValueError # 의도적으로 ValueError 발생시키기
    print( "{0} / {1} = {2}".format(num1,num2,num1/num2))

except ValueError : 
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
'''


print("="*50)    
print("프로그램 시작")    
print("="*50)    
#############################  사용자 정의 예외처리(5시1분~)  ###############################

class BigNumberError(Exception) : #exception을 상속받고
    def __init__(self,msg) : 
       self.msg=msg

    def __str__ (self) : 
        return self.msg
try :   
    print("한 자리 숫자 나누기 전용 계산기입니다")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1>=10 or num2 >=10 :
        raise BigNumberError("입력 값 : {0} , {1}".format(num1,num2)) # 의도적으로 해당 ERR Raise
    print( "{0} / {1} = {2}".format(num1,num2,num1/num2))

except ValueError : 
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

except BigNumberError as err : 
    print("에러가 발생하였습니다. 한 자리 숫자만 입력해주세요")
    print(err)

## Raise에서 발생된 big#err ->  입력값 문구를 받게되고, 품고있다가  아래 as err로 표현됨.