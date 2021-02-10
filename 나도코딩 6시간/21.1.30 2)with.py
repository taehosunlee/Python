#지금까진 파일에 대한 작업을 할 때 파일을 열고 작업하고 파일을 닫았었는데

#with를 쓰면 좀 더 편하게 할 수 있다.

import pickle

with open("profile.pickle","rb") as profile_file :      # profile_file이란 함수로 file여는것을 저장함.
    print(pickle.load(profile_file))

# 따로 안닫아줘도 된다. with문 벗어나면 자동으로 끝남


with open("study.txt","w",encoding="utf8") as study_file :
    study_file.write("파이썬을 열심히 공부하고 있어요.\n")
    study_file.write("파이썬을 열심히 공부하고 있어요2\n")
    study_file.write("파이썬을 열심히 공부하고 있어요3\n")


with open("study.txt","r",encoding="utf8") as study_file :
    while True :
        line = study_file.readline()
        if not line :
            break
        print(line, end="")

        
with open("study.txt","r",encoding="utf8") as study_file :
    print(study_file.read())