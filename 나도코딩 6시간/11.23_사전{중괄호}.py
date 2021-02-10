#1:31:50 부터 보기.

# 목욕탕 캐비넷 생각,  3번 키를 유재석씨가 받는다 :  중복 불가, 1:1매칭

cabinet = {3:"유재석",100:"김태호"}  # cabinet에는 2개의 키가 들어가있음.

print(cabinet[3]+" "+cabinet[100])

print(cabinet.get(3))
'print(cabinet[5]) # ERR 뜨면서 안됨.  나, None이라고 뜨면서 이어진다.
print(cabinet.get(5, "사용가능")) # 5라는 값에 대해서 가져오려고 하며,  없으면 뒤의 "사용가능"을 가져온다.

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3" : "유재석" , "B-100" : "조세호"}  # 숫자뿐만 아니라 문자로도 가능.

print(cabinet["A-3"])  #유재석
print(cabinet["B-100"]) #조세호

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"  # A-3 : 유재석 -> 김종국
cabinet["C-20"] = "정형돈" # C-20 -> 정형돈5라는 키가 없기때문.'
print(cabinet.get(5)) # 5라는 키가 없으


# 간 손님
print(cabinet)

del cabinet["A-3"]
print(cabinet)

# key 들만 출력.
print(cabinet.keys()) # (dict_keys(['B-100', 'C-20']))

# value들만 출력.
print(cabinet.values()) #dict_values(['조세호', '정형돈'])

# key, value 모두 출력
print(cabinet.items())


# 목욕탕 폐점
cabinet.clear()
print(cabinet)



a = {1:"a", 2:["b","c"]}
print(a[2])