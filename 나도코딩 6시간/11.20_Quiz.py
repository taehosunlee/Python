'''
Quiz. 사이트별로 비밀번호를 만들어주는 프로그램을 만드시오.

예) http://naver.com
규칙1 : http://부분은 제외할 것. => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자갯수 + 글자 내 'e' 갯수 + "!" 로 구성
                (nav)              (5)         (1)            (!)

예) 생성된 비번 : nav51!
'''


Site = "http://www.naver.com"

Index1 = len("http://")
Index2 = Site.index(".")
Index3 = Site.index(".",Index2+1)

print(Index1)
print(Index2)
print(Index3)
print(Site[Index1:Index3])
print(Site[Index2+1:Index3])

Site2 = Site[Index2+1:Index3]
Site3 = Site2[:3]
len2 = len(Site2)
ne = Site.count("e")
k = "!"

print(Site3)
print(len2)

print( "비밀번호는 " +str(Site3)+str(len2)+str(ne)+str(k)+" 입니다")




############ 방법2(해답)

url = "http://naver.com"
my_str = url.replace("http://","")   #규칙1
my_str = my_str[:my_str.index(".")]  #규칙2
# my_str을  처음부터~  .이 나오기 전까지로 끊음.

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print("{0}의 비밀번호는 {1} 입니다" .format(url,password))

