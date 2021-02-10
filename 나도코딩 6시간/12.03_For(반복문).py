# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")
# # .... 1000팀이 되었다.   다 쓸 수 없으니 반복문으로 만들어준다.

for waiting_no in [0,1,2,3,4] :   # 이 list 내의 0~4가 wating_no에 하나씩 들어간다. 순차적으로.
    print("대기번호 : {0}".format(waiting_no)) 


for waiting_no in range(1,6) :    #randrange()와 비슷.  1부터 6미만까지의 수.
    print("대기번호 : {0}".format(waiting_no)) 



starbucks = ["아이언맨","토르","그루트"]
for customer in starbucks : 
    print("{0}, 커피가 준비되었습니다".format(customer))




# 한줄 for.
# 출석번호가 1,2,3,4 앞에 100을 붙이기로 함. 101,102,103,104

students = [1,2,3,4,5]
print(students)

students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
print(students)
students = [len(i) for i in students]
print(students)


# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)