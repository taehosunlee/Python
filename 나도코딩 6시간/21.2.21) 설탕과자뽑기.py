h,w = input().split()
h=int(h) # 세로
w=int(w) # 가로
n= int(input())  # 막대 갯수




node= [["0" for j in range(w)] for i in range(h)]

for i in range(n) :
    l,d,x,y = input().split()
    x=int(x)-1
    y=int(y)-1
    l=int(l)   # 막대 길이
    d=int(d)   # 가로 : 0 , 세로 : 1
    
    if d==0 :
        for i in range(l) :
            if node[x][y+i]=="0" :
                node[x][y+i]="1"
            else : pass
    else :
        for i in range(l) :
            if node[x+i][y]=="0" :
                node[x+i][y]="1"
            else : pass





for i in range(h) :
    for j in range(w) :
        node[i][j]=str(node[i][j])


for i in range(h) :
    print(" ".join(node[i]))