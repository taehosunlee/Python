d=[]
for i in range(10) :
    string=input().split()
    d.append(string)



for i in range(10) :
    for j in range(10) :
        d[i][j]=str(d[i][j])

x=1
y=1

for j in range(100) :
    if d[x][y] =="0" :
        d[x][y]="9"
        if d[x][y+1] =="1" :
            x+=1
        else : 
            y+=1
    elif d[x][y] =="2" :
        d[x][y] = "9"
        break
            



for i in range(10) :
    print(" ".join(d[i]))