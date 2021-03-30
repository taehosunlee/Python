import sys

n,m = map(int,input().split())

room=[]

for i in range (n) :
    a=input()
    a=list(a)
    room.append(a)


s,t = map(int,input().split())

s=s-1

#s<t<=n+1

confirm2 = ['X']*m

for i in range (s,t-1) :
    if room[i] == confirm2 :
        print('-1')
        sys.exit()




confirm= [0]*m
result= [[0 for j in range(m)] for i in range(n-1)]

for i in range (s,t-1) :
    for j in range (0,m) :
        if room[i][j] ==  room[i+1][j] == 'O' :
            result[i][j] = 1
        else :
            pass


for i in result :
    if i==confirm :
        result.remove(i)
for i in result :
    if i==confirm :
        result.remove(i)


leng=len(result)

for i in range (leng-1) :
    for j in range (m) :
        if result[i][j] ==1 and result[i+1][j] != 1 :
            result[i][j]=0
        else : pass

move=0

for i in result :
    if i == confirm :
        move+=1

print(move)

