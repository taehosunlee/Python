f= open("C:\doit\새파일.txt", 'w')
for i in range(1,11) :
    data= "%d번째 줄입니다\n" %i
    f.write(data)
f.close()



#프로그램의 외부에 저장된 파일을 읽는 여러 방법
# 1. readline 함수 사용

f=open("c:\doit\새파일.txt",'r')
while True :
    line = f.readline()
    if not line :
        break
    print(line)
f.close()

print("-"*50)


# 2. readlines 함수 사용
f=open("c:\doit\새파일.txt",'r')
lines=f.readlines()
for line in lines :
    print(line)
f.close()



# 파일에 추가하는 방법
f=open("c:\doit\새파일.txt",'a')
f.write("새 추가 문장입니다")
f.close()



print("-"*25+"With문"+"-"*25)

### with 문과 함께 사용하기.###
# 기존까진 파일을 열고, 직접 닫아줘야했다. 이 열고 닫는것을 자동으로 해주는 것이
# with문이다.

with open("test1.txt",'w') as f :
          f.write("Life is too short, So you must learn Python")




### pickle ###  dump("내용","파일"), load("파일")
# 프로그램 상에서 우리가 사용하는 데이터를 파일상태로 저장
# 누군가가 그 파일을 받아 피클을 이용해, 코딩화 가능

import pickle
f = open("profile.pickle","wb")  #wb : write, 바이널 type.   pickle은 따로 인코딩타입 설정 안해줘도 됨.
profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩aa"]}

# print(profile)

# pickle을 이용해 이 데이터를 파일에 쓸 것.

pickle.dump(profile, f)  #profile의 정보를 f(profile.pickle)에 저장.

f.close()



f = open("profile.pickle","rb")

profile=pickle.load(f) #file에 있는 정보를 profile에 불러옴

print(profile)
f.close()



# sys 모듈로 매개변수 주기.
# 이 파일을 DOS로 실행한 뒤 매개변수 주면 print(i)가 된다.

import sys
args=sys.argv[1:]
for i in args :
    print(i.upper(), end=' ')


    

## read로 파일 전체 읽어온다음에, 파일 안의 내용 바꾸기.
## 이 경우 꼭 read()로 해야함. readline은 list형태로 저장하기 때문에 안된다.

with open('test.txt', 'r') as f :
    body=f.read()


body3=body.replace("Java","Python")

print(body3)

with open('test.txt', 'w') as f : 
    f.write(body3)
