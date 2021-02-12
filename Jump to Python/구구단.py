# 구구단


class gugu :
    def __init__(self) :
        pass

    def multi(self,val):
        result=[]
        for i in range(1,10) :
            result.append(int(val)*i)
        return result


val=input("단을 입력하세요 : ")

gu=gugu()
print(gu.multi(val))


# 1000 미만의 3의 배수 및 5의 배수의 총합

# 3의 배수 list

result3 =[]
result5 =[]
for i in range (1,1000) :
    if 3*i <=1000 :
        k=3*i
        result3.append(k)
    else : break

for i in range (1,1000) :
    if 5*i <=1000 :
        r=5*i
        result5.append(r)
    else : break

result3=set(result3)
result5=set(result5)
result=result3|result5
result=list(result)
result.sort()

print(len(result))
sum=0

for i in range(len(result)):
    sum+=result[i]

print(sum)




## 답지##

result=0
for i in range(1,1001) :
    if i%3 ==0 or i%5 ==0 :
        result+=i

print(result)


## 페이지.  총 게시물 수 & 1페이지에 들어갈 게시물 수

total = int(input("총 게시물 수 입력 : "))
sub = int(input("1페이지에 들어갈 게시물 수 : "))


if total%sub==0 :
    page = int(total/sub)
else : page = (total//sub)+1

print(page)
