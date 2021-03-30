k=int(input())  # 토핑 갯수
A,B = input().split()
A=int(A)  # 도우 가격
B=int(B)  # 토핑 가격
C=int(input()) # 도우 칼로리


toping=[]
pizza=[]

if k == 0 :
    toping.append(0)
    pizza.append(C/A)

else : 
    for i in range (k) :
        toping.append(int(input()))

    toping.sort()
    toping.reverse()

    Callorie = C
    num=0

    for i in toping :
        num+=1
        Callorie = Callorie+i
        price=A+(num*B)
        piz= Callorie/price
        pizza.append(int(piz//1))

pizza.sort(reverse=True)
print(pizza[0])
