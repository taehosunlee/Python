print("Python","Java") #띄어쓰기 됨
print("Python"+"Java") #띄어쓰기 안됨
print("Python","Java",sep=",") # seq 넣으면 그 사이에 뭘 넣을지 선택할 수 있음
print("Python","Java","JavaScript",sep=" vs ") # seq 넣으면 그 사이에 뭘 넣을지 선택할 수 있음  seperation

print("Python","Java",sep=",", end="?") # end : 문장의 끝부분을 "?"로 바꿔달라.  줄바꿈 대신.
print("무엇이 더 재밌을까요?")

import sys
print("Python","Java", file=sys.stdout) #표준 출력으로 처리
print("Python","Java", file=sys.stderr) #표준 에러로 처리

#시험 성적
scores = {"수학":0, "영어":50, "코딩":100} #key와 value를 쌍으로 튜플로 보내줌
for subject , score in scores.items() : # 2개의 변수로 적용.subject, score. Key : subejct Value : score
    #print(subject, score)
    print(subject.ljust(8),str(score).rjust(4),sep=":") #왼쪽정렬, 8개의 공간을 만들어 왼쪽정렬 #오른쪽정렬. 4칸 만들어서

#은행 대기 순번표
# 001, 002, 003, ...

for num in range(1,21) :
    print("대기번호 : " + str(num).zfill(3)) #zfill : null에 0을 채우는거.


answer = input("아무 값이나 입력하세요 : ")
print(type(answer))  # 숫자 입력해도 str 이 됨. int가 아니라.
#즉, 사용자 입력 값은 항상 str로 받는다.
print("입력하신 값은 " + answer + "입니다")