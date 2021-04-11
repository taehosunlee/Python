## 답지 보고 품.


n,m = map(int,input().split())

room=[]

for i in range (n) :
    a=input()
    a=list(a)
    room.append(a)

s,t = map(int,input().split())

s=s-1


import sys

confirm2 = ['X']*m

for i in range (s,t-1) :
    if room[i] == confirm2 :    ## s부터 t-1까지  내가 예약하려는 날 중 XXXXXXXXXXXXX 가 있으면 -1보내고 BREAK.
        print('-1')
        sys.exit()


def greedy(index) :           ## 방을 0~m까지 돌면서,  각 방에서 가장 많이 머물 수 있는 방을 고름. 
                              ## 만약 n번째 방에서 3일을 버틸 수 있다고 하면, 3일을 건너 뛰고 4일째부터의 방 탐색하면됨.
    maxx=0
    for i in range (0,m) :  # 0~m번째 방에서
        day=0
        for j in range (index,t-1) :  # index(초기엔 s가 될 것임.)째 날~ t-1 까지 돌리는데  
            if room[j][i] =="O" :     # O인 것을 발견할 때마다 머물 수 있는 날 +1
                day+=1                
            else : break              # X 나오면 break(해당 방은 끝난거임).  그래서 해당 방에서 몇 날 머물 수 있나 chk
        if maxx<day :                 # 만약, 기존까지의 방을 체크했을 때  신규 방에서 머물 날이  기존 방들보다 높을 때
            maxx=day                  # 그 방에서 머무는 날이 max가 된다.
    
    return maxx                       # index 날(처음엔 s) 를 체크했을 때, 각 방에서 몇일간 머물 수 있는지 chk해준 값을 return시켜줌.


cnt =-1                               #밑의 while문에서 cnt는 +=1로 시작할건디,  첨부터 옮기는건 아니므로 -1로  상쇄시켜줌.

    
while s<t-1 :                         # s~t-1까지 chk하는데,
    cnt+=1                            #  cnt는 0부터 시작.
    s+= greedy(s)                     # 만약 s=2 , t=10이라면   2일부터 9일까지 방을 사용하는 것이므로 room[1]~room[8]까지 chk해야한다.
                                      # room[1]에서  각 방 별 머물 수 있는 날을 고른 후, 최대 3일 가능하면  room[4]로 시작하고, cnt는 +1한다.  (cnt=1 방을 옮긴 횟수)
                                      # 그 후 room[4]에서 4일 가능하면 room[8]로 이동하고 cnt+1 시킨다  (cnt=2 방을 옮긴 횟수)
                                      # 마지막 날인 room[8]에서 쉴 수 있는 방 1개 있으므로,  거기서 쉬면 된다.
    
print(cnt)
        
