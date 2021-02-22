import re


# 기존
p=re.compile(".+:")
m=p.search("http://google.com")
print(m.group())  # http:


# 긍정형 전방탐색 (?=...) 의 형태이며 ...전까지 찾는다.
p=re.compile(".+(?=:)")   # .+ 검색,  : 전까지.
m=p.search("http://google.com")
print(m.group())  # http


# 부정형 전방탐색 
# 예를 들어 파일이름.확장자  를 나타내는 정규식 .*[.].*$ 이 있다고 치자
# 근데 .bat 파일 빼고 검색하고싶다.
# .*[.][^b].*$  --> 이러면 ba bae 도 다 걸러짐
# .*[.]([^b]..|.[^a].|..[^t])$  --> 이러면 .ct  같이 2개짜리 확장자는 못찾아냄.
# .*[.]([^b].?.?|.?[^a].?|.?.?[^t])$  --> 이러면 걸러짐.  근데  bat뿐만 아니라 exe도 거르라고 한다면? 너무 복잡해짐.

# .*[.](?!bat$).*$  --> 부정형으로  bat확장자 제외
# .*[.](?!bat$|exe$).*$  --> 부정형으로  bat,exe 확장자 제외





# 추가 메서드 (sub,subn )
#1) sub : 문자열 바꾸기.     sub(매개변수,문자열)
p=re.compile('(blue|white|red)')
m=p.sub('color','blue socks and red shous')
n=p.sub('color','blue socks and red shous', count=1)  # 1번만 바꾸게 함.
print(m)
print(n)

#2) subn : sub와 비슷하지만 결과를 튜플로 돌려줌
mn=p.subn('color','blue socks and red shous')
print(mn)


# sub 사용시 참조구문 사용하기.
p=re.compile(r'(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)')
reverse=p.sub('\g<phone> \g<name>', 'park 010-5125-7289 and it was not matched')   # p.를 넣는 순간 문자열에서 이미 매칭되는거 뽑음.  sub에서 매개변수에 맞게 치환시킴.
                                                            # 단, matching되는 것들만 나타내는 것이 아닌 매칭이 안되는 것들도 같이 나타내긴 한다.  매칭되는것들을 치환시킨채.
reverse2=p.sub('2 \g<2> \g<1> ', 'park 010-5125-7289')
print(reverse)
print(reverse2)


# sub 메서드의 매개변수로 함수 넣기.
def hexrepl(m) :
    value=int(m.group())
    return hex(value)

p=re.compile(r'\d+')
func=p.sub(hexrepl,'call 65490 for printing, 49152 for user code.')
print(func)



##### Greedy vs Non-Greedy #######

# Non-Greedy 문자인 ? 을 사용하면 *의 탐욕을 제한할 수 있다.
# non-greedy 문자인 ?는 *?, +?, ??, {m,n}? 와 같이 사용할 수 있다. 가능한 한 최소한의 반복을 수행하도록 도와준다.

s='<html><head><title>Title</title>'
print(len(s))  #32
print(re.match('<.*>',s).span())  # (0, 32)
print(re.match('<.*>',s).group())    # <html><head><title>Title</title>

# <.*> : <html>을 기대했으나  *는 매우 탐욕스러워서 처음의 <와  끝의 >을 가져갔다.  결국 문자열을 모두 소비해버림.

print(re.match('<.*?>',s).span())   # (0, 6)
print(re.match('<.*?>',s).group())  # <html>
