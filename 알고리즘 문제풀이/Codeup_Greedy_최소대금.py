# p1=int(input())
# p2=int(input())
# p3=int(input())
# j1=int(input())
# j2=int(input())


# lst_p=[]
# lst_j=[]
# lst_p.append(p1)
# lst_p.append(p2)
# lst_p.append(p3)
# lst_j.append(j1)
# lst_j.append(j2)

# lst_p.sort()
# lst_j.sort()


# price=lst_p[0]+lst_j[0]
# price= price*1.1

# print("%.1f" %price)

###################################################################################

# 그리디_동전문제 : 
# 1352원 지불할 때 동전 최소한의 갯수

coins=[500,100,50,10]
value=1352
coins_num=[]

for coin in coins :
    count=value//coin
    value=value-(coin*count)
    coins_num.append(count)

print(coins_num)

## 인터넷에서 퍼온 코드

# 동전 지불 문제
# 동전 종류, 지불할 돈

coins = [10, 50, 100, 500] # 동전 종류
coins.sort(reverse=True)
toPay = 1352 # 지불할 돈

# normal way

result = {x: 0 for x in coins}  # 딕셔너리 형태로 만든다.

value = toPay

for coin in coins:
	coin_count = value // coin
	value -= coin * coin_count
	result[coin] = coin_count   # 키와 value를 매칭시켜줌.

print(value)
print(result)