def add(a,b) :
    result=a+b
    return result

b=add(3,4)
print(b)

def say() :
    print("hi!")

say()

def add2(a,b) :
    print("{0}+{1}의 합은 {2}입니다".format(a,b,a+b))


add2(5,100)


####### 여러개의 입력값을 받는 함수  *args ##################

def profile(name,age,*language) :
    print("이름 : {0}\t나이: {1}\t".format(name,age), end=" ")
    for lang in language :
        print(lang, end=" ")
    print() #줄바꿈을 위해 넣음.


profile("유재석",20,"Python","Java","C","C++","C#","Minitab")
profile("김태호",25,"Python","Swift") 

def add_many(*args) :
    result=0
    for i in args :
        result = result+i
    return result

result=add_many(1,2,3,4,5,6,7,8,9,10)
print(result)


def add_mul(choice,*args) :
    if choice=="add" :
        result=0
        for i in args :
            result+=i
        return result
    if choice=="mul" :
        result=1
        for i in args :
            result*=i
        return result


print(add_mul("add",1,2,3,4,5,6,7,8,9,10))
print(add_mul("mul",1,2,3,4,5,6,7,8,9,10))


#### 키워드 파라미터  **kwargs ####
#### ** 두개 붙일 경우 딕셔너리로 저장된다.### a=1 -> a:1  name=taeho -> name:taeho


def print_kwargs(**kwargs) :
    print(kwargs)

print_kwargs(a=1)
print_kwargs(id="taehosunlee",password="Toakdm***",name="taeho")



### 결과값은 언제나 하나이다.  결과값 2개를 return시키면 튜플로 나온다**
def mass(a,b) :
    summ = a+b
    mul = a*b
    return summ,mul

print(mass(7,8))  #  (15,56)

summ, mul = mass(7,8)  # 결과값 따로다로 받고싶으면 이렇게 2개 써주면 됨.
print(summ)
print(mul)



### return 을 2개 쓰면?? 첫번째꺼 하나만 쓰고 함수 나온다.  이걸 이용해
### return을 특정 상황에서 즉시 함수 탈출용으로 쓸 수 있다

def say_nick(name) :
    if name=="바보" :
        return
    print("당신의 닉네임은 %s입니다" %name)

say_nick("도로도롱")
say_nick("밥봅")
say_nick("바보")  # return받아 바로 탈출했기에  아무것도 안나옴.
