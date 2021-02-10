# if 조건 : 
#    실행 명령문   #조건에 해당하면, 명령문이 실행됨.

# weather = input("오늘 날씨는 어때요? ")

# if weather == "비" or weather == "눈" :
#     print("우산을 챙기세요")
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요")
# else:
#     print("오늘은 준비물이 필요없어요")



temp = int(input("기온은 어때요? "))  # input은 항상 문자로 받는다.  그래서 숫자는 int로 감싸준다.  int : 정수
if 30<=temp :
    print("너무 더워요 나가지 마세요")
elif 10<=temp and temp <30 :
    print ("괜찮은 날씨에요")
elif 0<= temp and temp <10 :
    print("외투를 챙기세요")
else:
    print("너무 추워요 나가지 마세요")