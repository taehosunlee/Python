# 프로그램 상에서 우리가 사용하는 데이터를 파일상태로 저장
# 누군가가 그 파일을 받아 피클을 이용해, 코딩화 가능


import pickle
profile_file = open("profile.pickle","wb")  #wb : write, 바이널 type.   pickle은 따로 인코딩타입 설정 안해줘도 됨.
profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩aa"]}

# print(profile)

# pickle을 이용해 이 데이터를 파일에 쓸 것.

pickle.dump(profile, profile_file)  #profile의 정보를 file에 저장.

profile_file.close()



profile_file = open("profile.pickle","rb")

profile=pickle.load(profile_file) #file에 있는 정보를 profile에 불러옴

print(profile)
profile_file.close()


