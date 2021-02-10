def open_account() : # def 함수이름 적고, 함수 짜준다
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance,money) : #잔고가 얼마고, 입금할 금액이 얼만지.
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance+money  # 반환해주는 값. deposit(a,b) = a+b
    
def withdraw (balance, money) : #출금
    if balance >= money : #잔액이 출금보다 많으면,
        print("출금이 완료되었습니다. 잔액은{0}원 입니다.".format(balance-money))
        return balance - money
    else :
        print("출금이 완료되지 않았습니다. 잔액이 부족합니다.{0}원 남았습니다.".format(balance))
        return balance

balance = 0  #잔액
balance = deposit(balance, 1000)

balance= withdraw(balance,500)
balance= withdraw(balance,1000)


def withdraw_night(balance, money) : #저녁에 출금, 수수료 100원
    commission = 100 #수수료 100
    return commission, balance - money - commission   # 튜플 형태로  comission, balance 차례로 넣을 것.


balance = 0
balance = deposit(balance,3000)
commission, balance = withdraw_night(balance,500)   # 튜플 형태로 넣는다.

print( "수수료 {0}원이며, 잔액 {1}원 남았습니다".format(commission,balance))