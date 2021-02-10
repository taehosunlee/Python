#부모 클래스에서 정의한 연산자 말고, 자식 class에서 정의한 연산자를 쓰고 싶을 때
# 메소드를 새롭게 정의해서 쓸 수 있는데 이를 오버라이딩이라고 한다.

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


# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐",80,10,20)

# 배틀크루저 : 공중 유닛, 체력 high, 공격력 high
battlecruiser = FlyableAttackUnit("배틀크루저",500,25,3)

vulture.move("11시")
battlecruiser.fly(battlecruiser.name,"9시")

## 이 경우 fly, move를 계속 번갈아 써줘야하기에 복잡하다. 메소드 오버라이딩 통해서 합쳐주기.

print("-------------------")
vulture.move("11시")
battlecruiser.move("9시")