# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))   #  set : 중괄호

menu = list(menu) 

print(menu, type(menu))  # list : 대괄호
 
menu = tuple(menu)
print(menu, type(menu))  # tuple : 소괄호


menu = set(menu)

print(menu, type(menu))