#컴퓨터에 있는 파일을 열어서 안의 내용을 불러올수도,  쓸 수도 있음

#score_file을 열고(open),  쓰고,  닫기
score_file = open("score.txt","w",encoding="utf8") #"w" 덮어쓴다. #utf8 : utf8 정의 안해주면 한글을 이상한 문자로 나타낸다. "w"는 write의 의미
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

#score_file에 추가하기
score_file = open("score.txt", "a", encoding="utf8")  #"a"는 append. 추가.  "w"으로 하면 덮어쓰기가 됨
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")  #줄바꿈 따로 해줘야한다.
score_file.close()

#score.txt 불러오기
score_file=open("score.txt", "r", encoding="utf8")  #"r"  Reading
print(score_file.read())
score_file.close()

# 만약 한줄씩 불러와서 수정하고싶으면?
score_file=open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") #줄별로 읽기동작 수행. 한 줄 읽고 커서는 다음줄로 이동
print(score_file.readline()) #줄바꿈 안하려면 end="" 붙이기.
print(score_file.readline())
print(score_file.readline())
score_file.close()

print("----------1---------")
# 몇 줄인지 모를땐?(남의 파일 읽어올때)
score_file=open("score.txt", "r", encoding="utf8")
while True :  # 무한루프. 반복문 계속 실행
    line = score_file.readline() #line이란 변수를 만들어, score file 한줄씩 불러오기.
    if not line :  #읽어온 내용이 없으면 반복문 폭파
        break
    print(line, end="") # line 내용 있으면 print
score_file.close()

print("\n-------------------")
score_file=open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 모든 line을 list형태로 저장
for line in lines :
    print(line)
score_file.close()

print(lines)2