# 리스트 []
# [] 안에 숫자, 문자, 리스트 내 리스트 등 모든 자료형 다 들어갈 수 있음.

# 리스트의 인덱싱과 슬라이싱

print("\n"+"-"*20+"List"+"-"*20+"\n")

a= [1,2,3,4,5,6]
print(a[0])  #1
print(a[1]+a[2])  #2+3 = 5
print(a[-1]) # 마지막에 있는 6


a= [1,2,3,["a","b","c"]]

print(a[1])  # 2
print(a[3]) # ["a","b","c"]
print(a[-1]) # ["a","b","c"]

print(a[-1][0])  # a   --> a,b,c 리스트에서 첫번쨰인 a
print(a[-1][1])  # b
print(a[-1][2])  # c


#  Quiz.  삼중 구조의 List
a= [1,2,['a','b',['Life','is']]]  # Life 끄집어내려면?

print(a[-1][-1][0]) # = print(a[2][2][0])


# 슬라이싱(나누기)

p=[]
for i in range(1,11) : 

    p.append(int(i))

print(p) # [1~10]
print(p[3:6]) #4,5,6
print(p[-3:])    # 문자열과 완전 똑같다.

c = "Life is too short"
print(c[-3:])

k=[1,2,['a','b','c',["life","is","too","short"],'5','p']]

print(k[2][2:5]) # ['c', ['life', 'is', 'too', 'short'], '5']
print(k[2][3][2]) # too



# 리스트 연산하기 (+,*,len)


a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)

d=a*3
print(d)
print(len(d))


# 리스트 수정과 삭제

a=[1,2,3]
a[2]=4
print(a) #1,2,4

del a[1]
print(a)  #1,4

b= [1,2,3,4,5,6,7]
del b[5:]

print(b)




# 그 외 함수
# append, sort(정렬), reverse(순서뒤집기), index(위치반환)
# insert(a,b)  a 위치에 b 넣기
# remove(x) : 리스트에서 첫번째로 나오는 x 지우기
# pop(x) : x번째 요소를 끄집어내고, 리스트 내에선 지운다.
# pop() : 맨 마지막꺼 끄집어내고, 리스트 내에서 지운다.
# count(x) : x의 갯수 세기
# extend : 확장.  a.extend([4,5]) = a+=[4,5]
# clear : 다 지우기

# list.index( value ) : 값을 이용하여 위치를 찾는 기능
# list.extend( [value1, value2] ) : 리스트 뒤에 값을 추가 (‘+’연산자 보다 성능이 좋음)
# list.insert( index, value ) : 원하는 위치에 값을 추가
# list.sort( ) : 값을 순서대로 정렬
# list.reverse( ) : 값을 역순으로 정렬
# list = str.split() : 문자열 => 리스트, 공백시 스페이스 기준
# "".join( list ) : 리스트에서 문자열으로

a=[1,2,3,4,5] 
a.insert(1,4)  
print(a) #[1,4,2,3,4,5]

a.remove(4)  
print(a)  #[1,2,3,4,5]


b=a.pop(4)  
print(b)  #5
print(a)  #[1,2,3,4]


'''------------------------------------------------------------------'''
print("\n"+"-"*20+"Tuple"+"-"*20+"\n")

# 튜플 : 리스트랑 거의 비슷한디,() 쓰고 순서라던지, 추가 제거라던지.. 
#        수정 불가능함.  그 외는 완전히 리스트와 동일함
#        인덱싱, 슬라이싱, 튜플 더하기 등  가능
#        t1[3] , t1[1:3] , len(t1), t1*3, t1+t2, 등..

# (name,age,hobby) = ("김종국",20,"코딩")  # 튜플을 이용해 한꺼번에 변수 넣어줄 수 있음.


t1 = ()
t2 = (1,) # 요소 1개일 때 :  , 안붙으면 1  붙으면 (1,)로 나
t3 = (1,2,3)
t4 = 1,2,3 #튜플은 () 안붙여도 된다
t5 = ('a','b',('ab','cd'))
a=(1,2,3)
b=a+(4,)  ## 요소 1개면 무조건 , 붙여야

print(t1,t2,t3,t4,t5)
print(t2+t3+t4)
print(b)

'''------------------------------------------------------------------'''
print("\n"+"-"*20+"Dictionary"+"-"*20+"\n")

# 딕셔너리 : '이름'='홍길동' 등 대응관계.  연관배열 또는 해쉬(Hash)라고 함
# Key = Value.  Key를 통해 Value를 얻는다.
# 리스트나 튜플, 문자열은 요소값을 얻기 위해 슬라이싱이나 인덱싱 사용했다
# 그러나 딕셔너리는 단 한가지 방법 뿐이다. key로 value를 얻는다.
# key는 고유 값이므로 중복이 되면  뒤에 꺼 하나만 남고 다 무시된다.

# 리스트를 Value로 사용 가능하지만, Key로는 사용 불가하다.


# 기본 구조 : {Key1:Value1,Key2:Value2,Key3:Value3,...)
# 추가시 : a[key4]=Value4 ->  key4:Value4 쌍 추가.


a = {1:"a", 2:["b","c"]}
print(a[2])

a["new"]="dictionary"
print(a["new"])
print(a)


# 함수들
# del a[1] : key가 1인 key:value 삭제
# keys() : Key만을 모아서 보여준다
# values() : value들만 보여준다.
# items() : key, value 쌍을 튜플로 묶은 값을 items 객체로 돌려줌
# clear() : 모두 지우기.
# get(x,'디폴트값') : x라는 Key로 Value 얻기. a[key] 와 동일하지만, 없는 키를 넣었을 때
#           a[key]는 에러발생  a.get(key)는 None 띄워줌
# 'Key' in Dictionary : 딕셔너리 내에 Key가 있는지 True, False.   Value는 못찾음.
# Key에는 문자열,숫자,튜플 등 immutable 값이 들어간다.  리스트 같은 변화 가능한 것은 못들어감.
# pop(key) : key 의 value 뽑기.

Myprofile = {'name' : 'Taeho' , 'age': 17, 'phone' : '01051257289'}
print(Myprofile.keys())
print(Myprofile.items())

for k in Myprofile.keys() :
    print(k)

for k in Myprofile.items() :
    print(k)


print(Myprofile.get('ppo'))
print(Myprofile.get('ppo','없는 키입니다'))    # none일시 나올 것 적어줄 수 있음

print("name" in Myprofile)  # Key 찾을 수 있음  True
print("Taeho" in Myprofile) # Value  내용물은 못찾음. False


'''------------------------------------------------------------------'''
print("\n"+"-"*20+"집합"+"-"*20+"\n")

# 집합은 순서 상관 없으며, 중복 안된다. 말 그대로 수학적 집합
# 순서가 없으므로 인덱싱 불가.  인덱싱으로 접근하려면 튜플이라 리스트로 치환 필요.

# 교집합,차집합, 합집합 : 집합을 유용하게 사용하는 때.
# 원소 추가하기 add(), update()
# 원소 제거하기 remove()


s1=set("hello")
print(s1) # e, h, l, o  중복 없어지고 순서 뒤죽박죽.
s2=list(s1)
print(s2)
print(s2[1])


s1= set([1,2,3,4,5,6])
s2= set([4,5,6,7,8,9])
s3= {'k','l','remove'}

print(s1&s2)
print(s1|s2) #shift + \   s1|s2 = s1.union(s2)
print(s1-s2) # = s1.diffrenece(s2)

s1.add("add")
s2.update([00,"0a","0b"])
s3.remove("remove")

print(s1,s2,s3)
