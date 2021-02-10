# 애완동물 소개하기
hobby = "산책"
name = "해피"
age = 2
is_adult = age>=3
animal = "강아지"


print ( "우리집 " +animal+" 는 " +name + "에요")
hobby = "공놀이"  #여기서 hobby 가 산책->공놀이로 바뀜
# print (name+ "는 " +str(age)+"살이고 " +hobby+ "하는 것을 좋아해요")
# print (name, "는 " ,str(age)+"살이고 " ,hobby, "하는 것을 좋아해요")
print (name, "는 " ,age, "살이고 " ,hobby, "하는 것을 좋아해요")  # --> 콤마써서 띄어쓰기 추가됨.  /  str(age)  str 안써도 됨
# print (name+ "는 어른일까요?  " + str(is_adult) )   -> + 대신 ,를 쓰는 경우  str(숫자,판단) 에서 str 안써도 된다.
# 그리고, ,를 쓰면   띄어쓰기 하나가 자동 추가된다
print (name+ "는 어른일까요?  " , is_adult )

'''주석 처리 여러문장 동시에 하기
주석 한꺼번에 달기 : ctrl + / 하면 다 # 걸림.
'''

print ("주석처리 끝")


station = "사당"
print (station, "행 열차가 들어오고 있습니다")
station = "신도림"
print (station, "행 열차가 들어오고 있습니다")
station = "인천공항"
print (station, "행 열차가 들어오고 있습니다")