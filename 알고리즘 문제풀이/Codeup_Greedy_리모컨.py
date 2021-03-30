a,b =input().split()
a=int(a)
b=int(b)



c=abs(b-a)

count=0
count+=c//10  # 10의자리 빼고.
c=c-(10*count)  # c 재정의.  0~9까지의 수.

if c==0 : 
    pass

else :
    if c<4 :
        count+=c

    elif c== 4 :
        count+=2

    elif 4<c<8 : 
        count+=1
        count+=c%5


    else :
        c= 10-c
        count+=1
        count+=c



print(count)