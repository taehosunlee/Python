#while : 5번 손님을 불렀는데 안오면 버림.  반복을 하는데, 어떤 조건까지만 반복.

customer = "토르"
index = 5
while index >= 1 : 
    print("{0}, 커피가 준비되었습니다".format(customer))
    index -= 1
    if index ==0 :
        print ("커피는 폐기처분되었습니다.")




# customer = "아이언맨"
# while True :
#     print("{0}, 커피가 준비되었습니다. 호출{1}회.".format(customer,index))
#     index +=1   # 무한루프,  ctrl+c로 종료.

    

customer = "토르"
person = "Unknown"

while person != customer :
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")

    if person == customer :
        print("커피를 받아가세요")