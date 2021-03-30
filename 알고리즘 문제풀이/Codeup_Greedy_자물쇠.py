import sys

n=int(input())
lst=[]
result2=input().split()
result=[]

for sc in result2 :   # 결과값 
    sc=int(sc)
    result.append(sc)



for i in range (1,n+1) :   # 초기값 ( 1,2,3,4..,10 )
    lst.append(i)





def press_left(i) :  # 왼쪽으로 밀기.  i는 몇칸
    global lst
    lst2=lst[0:i]
    lst=lst[i:n]
    lst=lst+lst2


def overs(p,q) :
    global lst
    lst3=lst[p:q]
    lst4=lst[0:p]
    lst5=lst[q:n]
    lst3.reverse()
    lst=lst4+lst3+lst5

lst1=lst  # lst1 : 변경하기 전


for i in range (1,n) :
    lst=lst1  # 변경하기 전의 lst를 가져옴.
    press_left(i)
    lst2=lst  # 한번 밀고난 후의 lst
    for j in range(0,n-1) :
        for k in range (j+1,n) :
            lst=lst2  # lst 초기화해주기.
            overs(j,k)
            lst3=lst  # lst3는 한번밀고, 뒤집은 후의 list
            for l in range (1,n) :
                lst=lst3
                press_left(l)
                if lst==result : 
                    print(i)
                    print(j+1,k)
                    print(l)
                    sys.exit()


                else : pass