# + 계산기를 하나 만들었다.  그러나 동일한 파일 내에 계산기 2개,3개,4개... 여러개
# 가 필요할 경우,  def add1, def add2... 무수히 많아진다.
# 이를 간략히 하기위해 Class를 만든다.


# class(과자 틀) / object 또는 instance (과자 틀로 찍어낸 과자)  
# cal1=calculation()    calculation class는 class이고  cal1은 객체(object)가 된다.
# cal1,cal2 등 객체는 독립적으로 역할수행하며 독립적 결과값 갖는다. **객체는 고유하다.




# add,mul,div,sub  의 계산기 class 만들어보자.

class calculator : 
    def __init__(self,a,b) :
        self.a = a
        self.b = b
    
    def add(self) :
        self.result=self.a+self.b
        return self.result

    def sub(self) :
        self.result=self.a-self.b
        return self.result

    def mul(self) :
        self.result=self.a*self.b
        return self.result

    def div(self) :
        self.result=self.a/self.b
        return self.result


c=calculator(4,5)
print(c.add())
print(c.mul())
print(type(c))


'''
class calculator :
    def __init__(self) : pass
    
    def add(self,a,b) :
        self.result=a+b
        return self.result

    def sub(self,a,b) :
        self.result=a-b
        return self.result

    def mul(self,a,b) :
        self.result=a*b
        return self.result

    def div(self,a,b) :
        self.result=a/b
        return self.result

d=calculator()
print(d.mul(321,401))
'''


## 상속에 대해
## 보통 상속은 기존 class를 변경하지 않고 기능을 추가하거나 변경하고 싶을 때 사용.
## 기존 클래스가 라이브러리 형태로 제공되거나, 수정이 허용되지 않을 때 용이.
## 상속이, 부모클래스의 메소드를 모두 사용가능


class morecal(calculator) :
    def __init__(self,a,b,c) :
        calculator.__init__(self,a,b)  ## calculator 상속받음
        self.c = c
        print("{0},{1},{2}".format(self.a , self.b , self.c))

    def pow (self) : 
        result = (self.a * self.b) ** self.c
        return result

d=morecal(3,5,2)
print(d.pow())


# 만약 div 함수를 쓰는데, 0으로 나눌 때 에러발생을 피하고싶다?

class safecal(calculator) :
    def div(self) :
        if self.b == 0 :
            return 0
        else : return self.a / self.b

s=safecal(3,0)
sa=safecal(9,2)
print(s.div())
print(sa.div())
