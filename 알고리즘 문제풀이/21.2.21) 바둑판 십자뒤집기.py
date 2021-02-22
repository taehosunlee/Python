lst=[]
for i in range(19) :
    string=input().split()
    lst.append(string)




n=int(input())
for i in range(n) :
    x,y = input().split()   # x=1  y=1
    for j in range(19) :
        if lst[int(x)-1][j]=="0" :   # lst[0][0~18]
            lst[int(x)-1][j]="1"
        else :
            lst[int(x)-1][j]="0"
    for k in range(19) :
        if lst[k][int(y)-1]=="0" :
            lst[k][int(y)-1]="1"
        else : 
            lst[k][int(y)-1]="0"



for i in range(19) :
    for j in range(19) :
        lst[i][j]=str(lst[i][j])


for i in range(19) :
    print(" ".join(lst[i]))