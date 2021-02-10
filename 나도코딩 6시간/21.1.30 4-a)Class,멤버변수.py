
# Starcraft
# 마린 : 공격 유닛, 군인.  총을 쓸 수 있음

name = "마린" #유닛 name
hp = 40 # 유닛 체력
damage = 5 #유닛 공격력

print("{} 유닛이 생성되었습니다.".format(name))
print("체력은 {0}, 공격력 {1}\n".format(hp,damage))

# 탱크 : 시즈모드 존재.  일반 모드 / 시즈 모드

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛이 생성되었습니다.".format(tank_name))
print("체력은 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{} 유닛이 생성되었습니다.".format(tank2_name))
print("체력은 {0}, 공격력 {1}\n".format(tank2_hp,tank2_damage))



def attack(name, location, damage) : 
    print("{0} : {1} 방향으로 적군을 공격합니다.[공격력{2}]".format(name,location,damage))


attack(name,"1시",damage)
attack(tank_name,"1시",tank_damage)
attack(tank2_name,"1시",tank2_damage)

# 탱크 유닛을 수십개 만들건데 이렇게 일일이 만들 수 없다.  붕어빵 틀을 만들어 붕어빵 무한대로 만드는 게 클래스
# 클래스도 하나의 틀이고 서로 연관이 있는 변수와 함수의 집합


print("--------------------------------------------------")

class Unit : 
    def __init__(self,name,hp,damage) :
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력{1}".format(self.hp, self.damage))

marine1 = Unit("마린",40,5)
marine2 = Unit("마린",40,5)
tank = Unit("탱크",150,35)


# __init__ 에 대해서  : 파이썬에서 쓰이는 생성자 이다.
# 마린이라던지 탱크같은 개체가 생성될 때 쓰이는 것. 
# 이렇게 생성된 마린과 탱크는  Unit이란 Class의 instance라고 표현한다.
# __init__을 쓰려면 self는 빼고, 뒤에 나오는 갯수만큼의 변수를 입력해줘야한다.


print("--------------------2--------------")

#멤버 변수에 대해.
#멤버 변수는 Class 내에서의 변수.  name, hp, damage

# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wraith1= Unit("레이스",80,5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))  #멤버 변수를 외부에서 쓸 수 있다.

#프로토스의 다크아칸이 마인드컨트롤로 뺏었다고 해보자
wraith2 = Unit("빼앗은 레이스",80,5)
wraith2.clocking = True  

if wraith2.clocking == True : 
    print("{0} 는 현재 클로킹 상태입니다".format(wraith2.name)) 

# 클로킹변수는 저 위 def에 없지만, 외부에서 새로 추가할당해줌.  그러나 이 경우 할당해준 객체에만 적용이 되고
# 따로 할당해주지 않은 wraith1 등은 적용 안된다. ( wraith1 넣으면 에러남 )