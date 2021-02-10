'''
Quiz]표준 체중을 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) x 키(m) x 22
여자 : 키(m) x 키(m) x 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
        *함수명 : std_weight
        *전달값 : 키(height) , 성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시

(출력예제)
키 175cm의 남자의 표준 체중은 67.38kg 입니다.
'''

# ## 시도1 실패 ##
# height = int(input("키를 입력하세요"))
# gender = input("성별을 입력하세요(남자or여자)")

# def std_weight(height,gender) : 
#     if gender == "남자" :
#         std_weight = height*height*22
#         print("당신의 적정 체중은 {0}kg 입니다".format(std_weight))
#         return std_weight
#     elif gender =="여자" :
#         std_weight = height*height*21
#         print("당신의 적정 체중은 {0}kg 입니다".format(std_weight)
#         return std_weight
#     else :
#         print("성별을 다시 입력하세요. 남자 OR 여자")


# std_weight = std_weight(height,gender)

## 시도 2  ## 소수점 2째자리만 나타내야함.
# height = int(input("키를 입력하세요 : "))
# gender = input("성별을 입력하세요(남자or여자) : ")


# def std_weight(height,gender) : 
#     if gender == "남자" : 
#         std_weight = height*height*22/10000
#         print("키 {0}cm의 {1}의 표준 체중은 {2}kg 입니다".format(height,gender,std_weight))
#         return std_weight
#     elif gender == "여자" : 
#         std_weight = height*height*21/10000
#         print("키 {0}cm의 {1}의 표준 체중은 {2}kg 입니다".format(height,gender,std_weight))
#         return std_weight
#     else :
#         print("입력이 잘못됐습니다.")


# std_weight = std_weight(height,gender)


## 시도 3  ## 소수점 2째자리만 나타내야함_성공!
height = int(input("키를 입력하세요 : "))
gender = input("성별을 입력하세요(남자or여자) : ")

def std_weight(height,gender) : 
    if gender == "남자" : 
        std_weight2 = height*height*22/100
        std_weight = round(std_weight2)/100
        print("키 {0}cm의 {1}의 표준 체중은 {2}kg 입니다".format(height,gender,std_weight))
        return std_weight
    elif gender == "여자" : 
        std_weight2 = height*height*21/100
        std_weight = round(std_weight2)/100
        print("키 {0}cm의 {1}의 표준 체중은 {2}kg 입니다".format(height,gender,std_weight))
        return std_weight
    else :
        print("입력이 잘못됐습니다.")


std_weight = std_weight(height,gender)


'''

##########답지##############
def std_weight(height, gender) : #키 : m단위 (실수), gender : "남자"or "여자"
    if gender == "남자" : 
        return height*height*22
    else : 
        return height*height*21

height = 175 #cm 단위
gender = "남자"
weight = round(std_weight(height/100, gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))

#소수점 둘째자리 까지 나타내려면?
print(round(3.141597,2))
'''