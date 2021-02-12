# 복잡한 문자열 처리

# 주민번호를 포함하고있는 텍스트가 있다.
# 주민번호 뒷자리를 모두 **처리하고싶다.


# 1) 예제

data=\
"""
Lee 920707-1234567
Kim 901023-1234567
"""

result=[]
for line in data.split("\n") :  # 줄로 나누고
    word_result=[]
    for word in line.split(" ") :  # 띄어쓰기로 나눈다.
        if len(word)==14 and word[:6].isdigit() and word[7:].isdigit() :
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result)) # 띄어쓰기로 나눈거 합치기.

print("\n".join(result))


# 1-1) 예제, 정규식 사용하기.

import re

data=\
"""
Lee 920707-1234567
Kim 901023-1234567
"""

pat = re.compile("(\d{6})[-]\d{7}") #해당 형식을 찾는다, 앞 6자리를 group1으로 묶는다.
print(pat.sub("\g<1>-*******",data,count=1))  # 해당 문자열들을 치환. count=1 붙임으로써 한번만 치환.





# match 의 결과로 match 객체 또는 None을 돌려주기에, 보통 하기처럼 사용함.
'''
import re
p=re.compile(정규표현식)
m-p.match("조사할 문자열")
if m :
    print('Match Found : ',m.group())
else :
    print('Not Matched')

'''

# match : 문자열 처음부터 검색
# search : 문자열 전부를 검색. 해당하는게 있으면 match시킴
# findall : 정규식과 매칭하는 모든 것을 리스트 형태로 뽑아줌

p=re.compile('[a-z]+')
result = p.findall("life is too short")
print(result) # ['life','is','too','short']
