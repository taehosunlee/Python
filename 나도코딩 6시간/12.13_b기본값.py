'''
def profile(name,age,main_lang) :
    print("이름 :{0}\t 나이 :{1} \t주 사용 언어 :{2}"\
        .format(name,age,main_lang))  ## \는 줄바꿈.  두 문장이 하나의 문장으로 처리됨.

profile("유재석",20,"파이썬")
profile("김태호",25,"자바")
'''

# 같은 학교 같은 학년 같은 반 같은 수업.  --> 모두 동일할 경우 반복해서 써줄 필요 없다

def profile(name,age=17,main_lang="파이썬") :  # profile 함수가 호출될 때, age, main_lang이 입력받지 않았을 때, 기본값 입력
    print("이름 :{0}\t 나이 :{1} \t주 사용 언어 :{2}"\
        .format(name,age,main_lang)) 


profile("유재석")
profile("김태호")
profile("지민석",23,"자바")

def profile2(name,age,main_lang) :
    print(name,age,main_lang)

profile2(name="유재석",main_lang="파이썬",age=20)  #순서 바꿔도 가능

profile2(main_lang="자바",age=25,name="김태호")