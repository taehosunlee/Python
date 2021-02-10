from random import *

class Unit : 
    def __init__(self,name,hp,speed) : 
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self,location) :
        print("{0} : {1} 방향으로 이동합니다. [속도:{2}]".format(self.name, location, self.speed))

    def damaged(self, damage) : 
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <=0 :
            print("{0} : 파괴되었습니다".format(self.name))




# 공격 유닛
class AttackUnit(Unit) :
    def __init__(self,name,hp,speed,damage) :
        Unit.__init__(self,name,hp,speed) 
        self.damage = damage

    def attack(self, location) :
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name,location, self.damage))


# 공중 유닛
class Flyable : 
    def __init__(self, flying_speed) :
        self.flying_speed = flying_speed

    def fly(self, name, location) :
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit , Flyable) : 
    def __init__(self,name,hp,damage,flying_speed) :
        AttackUnit.__init__(self, name, hp, 0, damage) ## 지상유닛은 공중스피드가 0
        Flyable.__init__(self, flying_speed)

    def move(self, location) : 
        self.fly(self.name,location)   ##여기서의 move는 Unit class의 move와는 다르다.  자식 class 내에서 새롭게 정의한 것.




# 마린
class Marine(AttackUnit) : 
    def __init__(self) : 
        AttackUnit.__init__(self,"마린",40,1,5)

    def steampack(self) : ## 스팀팩 .체력 10 깎이며 이속,공속 증가.
        if self.hp>10 :
            self.hp -=10
            print("{0} : steampack을 사용합니다. (HP 10감소)".format(self.name))
        else :
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않았습니다".format(self.name))


# 탱크   seize모드 존재.  이동불가, 공격력 증가. 시즈모드 on/off는 전 탱크 동일하게 적용된다고 가정해보자.
class Tank(AttackUnit) :
    seize_developed = False # 시즈모드 개발여부

    def __init__(self) : 
        AttackUnit.__init__(self,"탱크",150,1,35)
        self.seize_mode = False

    def set_seize_mode(self) : 
        if Tank.seize_developed == False : 
            return # 시즈모드 미개발시 걍 나간다.

        # 현재 시즈모드가 아닐 때 -> 시즈모드
        if self.seize_mode == False :
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *=2
            self.seize_mode = True

        # 현재 시즈모드일 때 -> 시즈 풀림

        else :
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /=2
            self.seize_mode = False



class Wraith(FlyableAttackUnit) :
    def __init__(self) :
        FlyableAttackUnit.__init__(self,"레이스",80,20,5)
        self.clocked = False #클로킹모드 해제 중


    def clocking(self) :

        if self.clocked == True : #클로킹 모드이므로 클로킹 해제
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked =False
        
        else : #클로킹 모드 해제 -> 설정
            print("{0} : 클로킹 모드 설정합니다".format(self.name))
            self.clocked = True



def game_start() :
    print("[알림] 새로운 게임을 시작합니다.")

def game_over() :
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")



# 실제 게임 진행해보기

game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 =Tank()
t2 =Tank()

# 레이스 1기 생성
w1 = Wraith()


#유닛 일괄 관리 (list 만들기)
Attack_units = []
Attack_units.append(m1)
Attack_units.append(m2)
Attack_units.append(m3)
Attack_units.append(t1)
Attack_units.append(t2)
Attack_units.append(w1)

# 전군 이동

for unit in Attack_units :
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

# 공격 모드 준비 ( 마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹 )
for unit in Attack_units : 
    if isinstance(unit, Marine) : #지금 만들어진 객체가 어떤 class의 인스턴스 인지 확인하는 것
        unit.steampack()
    
    elif isinstance(unit, Tank) :
        unit.set_seize_mode()

    elif isinstance(unit,Wraith) :
        unit.clocking()


# 전군 공격
for unit in Attack_units :
    unit.attack("1시")

# 전군 피해
for unit in Attack_units :
    unit.damaged(randint(5,21)) # 피해 랜덤하게 받음. (5~20)

# 게임 종료
game_over()