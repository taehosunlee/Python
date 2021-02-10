# 건물을 만들 것.


'''
class Unit : 
    def __init__(self,name,hp,speed) :   ## 😀😀스피드 추가
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self,location) :
        print("[지상유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도:{2}]".format(self.name, location, self.speed))


# 공격 유닛

class AttackUnit(Unit) :
    def __init__(self,name,hp,speed,damage) :
        Unit.__init__(self,name,hp,speed) 
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


# 드랍쉽 : 공중유닛, 수송기. 공격x
# 레이스 : 공중유닛, 공격o


# 날아서 공격가능한 발키리 만들기.

class Flyable : 
    def __init__(self, flying_speed) :
        self.flying_speed = flying_speed

    def fly(self, name, location) :
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit , Flyable) : 
    def __init__(self,name,hp,damage,flying_speed) :
        AttackUnit.__init__(self, name, hp, 0, damage) ## 지상유닛은 공중스피드가 0
        Flyable.__init__(self, flying_speed)

    ##연산자 오버라이딩😁😁😁😁😁
    def move(self, location) : 
        print("[공중유닛 이동]")
        self.fly(self.name,location)   ##여기서의 move는 Unit class의 move와는 다르다.  자식 class 내에서 새롭게 정의한 것.


# 건물

class BuildingUnit(Unit) :
    def __init__(self,name,hp,location) : 
        #Unit.__init__(self,name,hp,0)
        super().__init__(name,hp,0)  ## 슈퍼로 나타낼 수도 있는데, self 빼고쓰고, 괄호 해줘야한다. 그리고 다중상속 안된다★★★★
        self.location = location
 '''


# Pass : 아무것도 안하고 일단 넘어가라는 명령어
def game_Start() :
    print("[알림] 게임이 시작됩니다")

def game_over() : 
    pass

game_Start()
game_over()



# Super : self 빼고쓰고, 괄호 해줘야한다. 그리고 다중상속 안된다★★★★

class Unit : 
    def __init__(self) :
        print("Unit 생성자")

class Flyable :
    def __init__(self) :
        print("Flyable 생성자")

class FlyableUnit(Unit,Flyable) : 
    def __init__(self) : 
        # super().__init__()   # 앞에 오는 Unit만 상속받는다.
        Unit.__init__(self)
        Flyable.__init__(self)


dropship = FlyableUnit()