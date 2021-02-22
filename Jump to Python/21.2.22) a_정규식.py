import re

p= re.compile('[a-z]+')  #  패턴객체 p : 영문자 반복


### 1)  match와 search

m= p.match('python')   
m1= p.match('3 python')
print(m)  # <re.Match object; span=(0, 6), match='python'>   0~6까지 매칭된다.
print(m1)  #  None.  match 함수는 처음부터 정규식과 매치되는지 조사하기 때문에, 매칭안됨

            
n= p.search('python is funny')   
n1= p.search('3 python is funny') 
print(n)  # <re.Match object; span=(0, 6), match='python'>   0~6까지 매칭된다.
print(n1)  #  <re.Match object; span=(2, 8), match='python'>


m=p.match("python match")   # 보통 이렇게 쓰인다
if m :
    print('Match found :', m.group())   # m.group으로 m 내용 보여줌
else : 
    print('No match')


###2)  findall() 와 finditer()

findall = p.findall("life is too short")
finditer = p.finditer("life is too short")

print(findall)  # 객체들을 모조리 찾는다.  그 객체들을 list로 돌려줌
print(finditer) # findall과 동일하지만 그 결과로 반복가능한 객체(iterator object)를 돌려준다. 반복 가능한 객체가 포함하는 각각의 요소는 match 객체이다

for i in findall : 
    print(i)

###3) group, start, end, span
print(m.group())
print(m.start())
print(m.end())
print(m.span())

print("-"*100)






print("-"*100)


###4) 압축하기
p=re.compile('[a-z]+')
m=p.match("python")  # 을 압축 가능하다

n=re.match('[a-z]+', "python")

print(m)
print(n)


### 컴파일 옵션  Dotall, Ignorecase, multiline, verbose
import re

p=re.compile('a.b', re.DOTALL)   # DOTALL은  줄바꿈까지 .에 포함시킴
p1=re.compile('[a-z]', re.IGNORECASE)  # 대소문자 상관없이 매칭

# p4=re.compile('a.b', re.)

m=p.match('a\nb')  # <re.Match object; span=(0, 3), match='a\nb'>
m1=p1.match('Python') # <re.Match object; span=(0, 1), match='P'>

print("-"*50)  #-----------------------------------------------

# multiline
p2=re.compile('^python\s\w+', re.MULTILINE)   # ^,$ 와 사용  ^는 처음,  $는 마지막이 매치돼야함.
p3=re.compile('python$\s\w+', re.MULTILINE)

data="""python one
life is too short
python two
you need python
python three"""

print(p2.findall(data)) # ['python one', 'python two', 'python three']  ^에 의해 처음이 python인것만 가져옴   기준은 한 라인.
print(p3.findall(data)) # ['python\npython']  $에 의해 끝이 python인거 가져옴.  기준은 한 라인.

print("-"*50)  #-----------------------------------------------

# VERBOSE(=X)  풀어쓰기 & 보기 편하게.

charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

charref = re.compile(r"""
&[#]                # Start of a numeric entity reference
(
    0[0-7]+         # Octal form
    | [0-9]+        # Decimal form
    | x[0-9a-fA-F]+ # Hexadecimal form
)
;                   # Trailing semicolon
""", re.VERBOSE)


# | ^ $ \A \Z \b \B

p=re.match('Crow|Servo', 'Crow Hello')
print(p)

print(re.match('^Life', 'Life is too short'))  # Lift
print(re.match('^Life', 'That is too short Life'))  # None

print(re.search('Life$', 'Life is too short'))  # None
print(re.search('Life$', 'That is too short Life'))  # Life.   # 이 경우 match 쓰면 None 뜬다

print("-"*60) #-----------------------------------------------

# 그루핑
p=re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m=p.search("park 010-1234-1234") 
print(m.group(1))
print(m.group(2))

# 문자열 재참조하기.  \1  
p = re.compile(r'(\b\w+)\s+\1')   # (\b\w+)\s+1  은  "(그룹)+" "+(그룹과 동일한 단어)"  와 매칭됨을 의미한다.     \1은 정규식의 그룹중 첫번째 그룹을 의미
m=p.search(" Paris in the the spring")
print(m.group())

p=re.compile(r"(?P<name>\w+)\s+(?P<number>(?P<youngilyoung>\d+)[-]\d+[-]\d+)")   # ?P<>  구문을 그룹 앞에 붙임으로써 명명이 가능하다.
m=p.search("park 010-1234-5125")
print(m.group("name"),m.group("number"),m.group("youngilyoung"))

p = re.compile(r'(?P<name>\b\w+)\s+(?P=name)')   # 문자열재참조시  \1이 아닌 ?p=~~ 로도 재참조시킬 수 있다.
m=p.search(" Paris in the the spring")
print(m.group())



