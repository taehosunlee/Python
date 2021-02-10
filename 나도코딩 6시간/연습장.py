
# 결과창 지우기 cls






from random import * # random library 쓴다.
# print(random()) # 0.0~1.0 미만의 임의의 값 생성
# print(random() * 10) # 0.0~10.0 미만의 임의의 값 생성
# print(int(random() * 10))  # 0~10 미만의 임의의 정수 생성
# print(int(random() * 10))  # 0~10 미만의 임의의 정수 생성
# print(int(random() * 10))  # 0~10 미만의 임의의 정수 생성
# print(int(random() * 10)+1)  # 1~10 이하의 임의의 정수 생성
# print(int(random() * 10)+1)  # 1~10 이하의 임의의 정수 생성
# print(int(random() * 10)+1)  # 1~10 이하의 임의의 정수 생성


'''
lst = set(range(1,21))

print(lst)

jumin = input("주민번호를 입력하세요 : ")

sex = int(jumin[7])

if sex==1 :
    print("성별은 남자입니다.")
    print("생년월일은 " + jumin[0:6]+ "입니다")
elif sex==2 : 
    print("성별은 여자입니다.")
    print("생년월일은 " + jumin[0:6]+ "입니다")



color = input("색을 입력하세요 : ")
age = input("나이를 입력하세요 : ")
print( "나는 {1}살이며, {0}색을 좋아해요".format(color, age) )
'''

# h = 60
# print (h + "살")



# 일반 유닛
class Unit : 
    def __init__(self,name,hp) :
        self.name = name
        self.hp = hp
        # self.damage = damage ##메딕은 데미지 필요없으므로 삭제. 위의 변수에서도 삭제


# 공격 유닛
class AttackUnit(Unit) :
    def __init__(self,name,hp,damage) :
        Unit.__init__(self,name,hp)
        self.damage = damage

    def attack(self, location) :
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name,location, self.damage))

    def damaged(self, damage) : 
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))

        if self.hp <=0 :
            print("{0} : 파괴되었습니다".format(self.name))



