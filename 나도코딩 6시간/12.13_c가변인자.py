# 2시간 44분째부터 보기

# 할 수 있는 언어가 많다.

def profile(name,age,lang1,lang2,lang3,lang4,lang5) : 
    print("이름 : {0}\t나이: {1}\t".format(name,age), end=" ") # 이 print문이 끝날 때, 줄바꿈 하지않고 " "로 끝낸다(이어서 써짐)
    print(lang1,lang2,lang3,lang4,lang5)

profile("유재석",20,"Python","Java","C","C++","C#") # 6개 알아도 5개밖에 못적음.
profile("김태호",25,"Python","Swift","","","") #2개밖에 모르는데, 뒤에 3개도 입력해줘야해서 번거로움.


def profile(name,age,*language) :
    print("이름 : {0}\t나이: {1}\t".format(name,age), end=" ")
    for lang in language :
        print(lang, end=" ")
    print() #줄바꿈을 위해 넣음.


profile("유재석",20,"Python","Java","C","C++","C#","Minitab")
profile("김태호",25,"Python","Swift") 


# 이런식으로 서로 다른 갯수의 변수를 넣어줄 때는, 가변인자.  *로 시작하는 가변인자를 통해 나타낼 수 있음.

