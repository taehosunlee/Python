# 리스트와 다르게 내용 변경이나 추가 불가능.  할 수 있는게 많진 않은데, 속도가 리스트보다 빠름


menu = ("돈까스" , "치즈까스")

print(menu[0])
print(menu[1])

name = "김종국"
age = 20
hobby = "코딩"

print(name,age,hobby)

(name,age,hobby) = ("김종국",20,"코딩")  # 튜플을 이용해 한꺼번에 변수 넣어줄 수 있음.
print(name, age, hobby)
