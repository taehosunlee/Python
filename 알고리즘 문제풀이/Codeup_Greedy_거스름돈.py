coins=[50000,10000,5000,1000,500,100,50,10]
value=int(input())
coins_num=[]

for coin in coins :
    count=value//coin
    value=value-(coin*count)
    coins_num.append(count)

summ=0
for i in coins_num :
    summ+=i

print(summ)