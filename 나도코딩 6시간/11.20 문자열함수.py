# '문자열 처리함수'

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())  #python 문자열의 0번 문자가 대문자인가? True.
print(len(python))  # python 문자길이
print(python.replace("Python","Java")) # Python 을 Java로 바꾸기

index1 = python.index("n")  # python 이란 변수에서,  n이란 문자가 몇번째에 위치해있는지 알려준다.

print(index1)

index2 = python.index("n", index1 + 1)  # "n" 이후에 온 구간은 Start 지점을 의미하며, 해당 지점 이후에 있는 n을 찾는다.

print(index2)

index3 = python.index("n", 6)  # "n" 이후에 온 구간은 Start 지점을 의미하며, 해당 지점 이후에 있는 n을 찾는다.

print(index3)


print(python.find("n"))  # find와 index는 거의 유사하다.  몇번째에 있는지 찾아냄
# 다른 점은,  아래 Java를 찾을 경우처럼

print(python.find("Java"))   #  못찾아서  -1로 나옴.  -1로 나오고 아래 쭉 이어짐.
# print(python.index("Java"))  #  없기때문에 아예 ERR를 내버림. 그래서, 이후 함수들이 실행안되고 끝나버림

print("hi")

print(python.count("n"))  # n이 몇번 등장하는지 알려줌