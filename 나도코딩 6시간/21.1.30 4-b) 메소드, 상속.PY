# 일반 유닛
class Unit : 
    def __init__(self,name,hp,damage) :
        self.name = name
        self.hp = hp
        # self.damage = damage ##메딕은 데미지 필요없으므로 삭제. 위의 변수에서도 삭제


# 공격 유닛
class AttackUnit() :
    def __init__(self,name,hp,damage) :
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력{1}".format(self.hp, self.damage))

    def attack(self, location) :
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name,location, self.damage))

    def damaged(self, damage) : 
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))

        if self.hp <=0 :
            print("{0} : 파괴되었습니다".format(self.name))

        ## 셀프는 자기 자신을 의미하며, 클래스 내에서 메소드 앞에는 항상 self를 적어준다고 기억하자.



firebat1 = AttackUnit("파이어뱃",50,16)
firebat1.attack("5시")  #self는 따로 변수 안줘도 된다.

#공격 2번 받음
firebat1.damaged(25)
firebat1.damaged(25)



# 메딕 : 의무병. 공격불가. 일반 유닛
# 일반 유닛과 어택유닛 모두 name, hp 항목 쓰고있다.  중복됨. 이 경우 ""😎상속""을 사용 가능
# UNIT Class의 내용을 상속받아 Attackunit에서 사용

########################상속####################
# 일반 유닛
class Unit : 
    def __init__(self,name,hp) :
        self.name = name
        self.hp = hp


# 공격 유닛
class AttackUnit(Unit) :
    def __init__(self,name,hp,damage) :
        Unit.__init__(self,name,hp)  ## Unit 상속받음
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력{1}".format(self.hp, self.damage))

    def attack(self, location) :
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name,location, self.damage))

    def damaged(self, damage) : 
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))

        if self.hp <=0 :
            print("{0} : 파괴되었습니다".format(self.name))


firebat1 = AttackUnit("파이어뱃",50,16)
firebat1.attack("5시") 

#공격 2번 받음
firebat1.damaged(25)
firebat1.damaged(25)