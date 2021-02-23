# #1번
# a="a:b:c:d"
# b=a.split(":")
# print("#".join(b))

# #2번
# a={"A":90,"B":80}
# a["C"]=70
# print(a["C"])
# print(a)

# #4번
# A=[20,55,67,82,45,33,90,87,100,25]
# summ=0
# for i in A :
#     if i>=50 :
#         summ+=i

# print(summ)


# #5번 피보나치 함수
# a=[0,1]
# n=int(input("n수를 입력하시오 : "))

# for i in range(1,n) :
#     b=a[i]+a[i-1]
#     if b<=n :
#         a.append(b)
#     else : break
# print(a)

# # 5번 답지
# def fib(n) : 
#     if n==0 : return 0
#     elif n==1 : return 1
#     else : 
#         return fib(n-2)+fib(n-1)
    
# for i in range (10) :
#     print(fib(i))


# 6번 숫자의 총합 구하기
# numbers=input("합을 구할 숫자입력 : ").split(",")
# summ=0
# print(numbers)
# for number in numbers :
#     summ+=int(number)

# print(summ)


# # 7번 구구단 구하기
# class gugu :

#     def multi(self,val):
#         result=[]
#         for i in range(1,10) :
#             result.append(int(val)*i)
#         return result


# val=input("단을 입력하세요 : ")

# gu=gugu()
# print(gu.multi(val))


# 8번 역순바꾸기.(파일 내 내용. pickle dump로 했더니 이상한 문자도 포함되버림.)
# f=open("C:\doit\\abc.txt", 'r')
# lines = f.readlines()
# print(lines)

# lines_new = []
# for i in range(len(lines)) :
#     line = lines[len(lines)-i-1]
#     lines_new.append(line)

# print(lines_new)

# import pickle
# f_new = open("C:\doit\\abc.txt", "wb")
# pickle.dump(lines_new,f_new)
# f_new.close()


# sys 참조하여 바꾸기.(cmd로.  IDLE로 파일 새로 만듬)
# import sys

# src = sys.argv[1]
# dst = sys.argv[2]

# f=open(src, 'r')
# lines = f.readlines()
# f.close()

# lines_new = []
# for i in range(len(lines)) :
#     line = lines[len(lines)-i-1]
#     lines_new.append(line)

# f= open(dst,'w')
# for i in lines_new :
#     f.write(i)
# f.close()


# 답지 *여기선 ab.txt로 함
# f= open('C:\doit\\ab.txt', 'r')
# lines = f.readlines()
# f.close()

# print(lines)
# lines.reverse()  # 읽은 라인을 역순으로 정렬
# print(lines)

# f= open('C:\doit\\ab.txt', 'w')
# for line in lines :
#     line=line.strip() # 포함되어있는 줄바꿈 문자 제거
#     f.write(line)
#     f.write("\n")
# f.close()


# 9번 문제
# f=open("C:\doit\9thproblem.txt",'r')
# lines=f.readlines()
# f.close()
# print(lines)
# print(len(lines))
# summ=0
# for line in lines :
#     line= line.strip()
#     summ+=int(line)

# avg=(summ/len(lines))

# f=open("C:\doit\9th_p_result.txt",'w')
# f.write(str(avg))
# f.close()


# # 10번 문제
# try : 
#     lst=input("숫자들을 입력하세요.").split(",")
#     howto=str(input("sum,multi 중 선택하세요."))
#     class Calculator : 
        
#         def __init__(self) :
#             pass

#         def sum(self) :
#             result=0
#             for i in lst :
#                 result+=int(i)
#             return result
#         def multi(self) :
#             result=1
#             for i in lst :
#                 result*=int(i)
#             return result

#     cal=Calculator()

#     if howto == "sum" :
#         print(cal.sum())
#     elif howto =="multi" :
#         print(cal.multi())
#     else : print("잘못된 수식 입력")
# except Exception : print("숫자 잘못 입력.  ,로 나눠서 입력하세요")




# # 13번 문제  연속 홀수시 -, 연속 짝수시 * 붙이기.
# num = input("숫자를 입력하세요 : ")
# num_list = []
# for i in range (len(num)) :
#     num_list.append(str(num[i]))

            
# def dashinsert() : 
#     global num_list  ## 글로벌!! 함수에 ()  에 아무것도 안들어갔으므로, global 변수 사용필요
#     for i in range (len(num_list)) :
#         if i==0 : pass
#         elif int(num_list[i]) %2 ==0 and int(num_list[i-1])%2==0 :
#             num_list[i-1]=str(num_list[i-1]+"*")
#         elif int(num_list[i]) %2 ==1 and int(num_list[i-1])%2 ==1 :
#             num_list[i-1]=str(num_list[i-1]+"-")
#         else : pass

#     num_list = "".join(num_list)
#     return num_list

# print(dashinsert())

        

# # 14번 문제.  문자열 압축하기.

# num = "aaabbccccabaaa"

# result=[]
# i=0
# cnt=1
# while i<len(num)-1 :
#     if num[i]==num[i+1] :
#         cnt+=1
#         i+=1
#         if i==len(num)-1 :
#             result.append(num[i-1])
#             result.append(str(cnt))
#     elif num[i]!=num[i+1] :
#         result.append(num[i])
#         result.append(str(cnt))
#         cnt=1
#         i+=1

# l=len(num)-1
# if num[l] != num[l-1] :
#     result.append(num[l])
#     result.append(str(1))

# result="".join(result)
# print(result)

# # 답지
# def textcompress(s) :
#     _c = ""
#     cnt = 0  # 0은 False,  1부턴 True
#     result=""
#     for c in s :
#         if c!=_c :
#             _c=c
#             if cnt :
#                 result +=str(cnt)  # 처음 0일땐, False라 측정안됨.  이후엔  이전 alphabet의 갯수 입력.(cnt+=1 로 쌓아둔거를 입력.)
#             result += c  # 새로 나온 문자 넣어줌.
#             cnt=1 # cnt 초기화.  
#         else : 
#             cnt+=1
    
#     if cnt : result+=str(cnt)
#     return result

# print(textcompress("aaabbccccabaaa"))


# 15번 _ Duplicate numbers : 0~9의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0~9 모든숫자를 한번씩만 사용했는지 알아보는 함수.

# def confirm(num) :
#     num_list=[] 
#     if len(num) != 10 :
#         print("0~9를 한번씩만 사용하세요_1")
#     else : 
#         for i in range (len(num)) :
#             num_list.append(str(num[i]))
#         num_list=set(num_list)
        
#         if len(num_list) != 10 :
#             print("0~9를 한번씩만 사용하세요_2")
#         else : print("입력값 : " + num)


# confirm("0123456789")
# confirm("01234")
# confirm("6789012345")
# confirm("0120123224")

# # 15번 답지
# def chkDupNum(s) :
#     result=[]
#     for num in s :
#         if num not in result : 
#             result.append(num)  # 중복되는지 검사.
#         else : 
#             return False  # 중복시 False
#     return len(result) == 10  # 총 길이 10인지 검사.

# print(chkDupNum("0123456789"))
# print(chkDupNum("01234"))
# print(chkDupNum("6789012345"))
# print(chkDupNum("012322456777"))

# 16번 모스부호 해독 # 실패, 답지 봄.
# HE SLEEPS EARLY  .... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--

# def release(mos) : 
#     result = []
#     dic = {".-" : "A" , "-..." : "B" , "-.-." : "C", "." : "E" , "..-." : "F" ,\
#          "--." : "G" , "...." : "H", ".." : "I" , ".---" : "J" , '-.-' : 'K', '.-..' : 'L' , \
#         '--' : 'M' , '-.' : 'N' , '---': 'O' , '.--.' : 'P' , '--.-' : 'Q' , '.-.' : 'R', '...' : 'S', '-' : 'T' , '..-' : 'U' ,\
#              '...-' : 'V', '.--' : 'W' , '-..-' : 'X','-.--':'Y', '--..' : 'Z'}
#     for word in mos.split("  ") : 
#         for alphabet in word.split(" ") : 
#             result.append(dic[alphabet])
#         result.append(" ")
#     print("".join(result))
            

# release(".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--")
    




# # #19 그루핑

# data='''
# park 010-9999-9988
# kim 010-9909-7789
# lee 010-8789-7768
# '''

# import re

# p=re.compile('(\w+\s\d+[-]\d+[-])\d+')
# m=p.sub('\g<1>****',data)
# print(m)



#20 전방탐색

import re

data='''
kim@daum.net
lee@naver.com
park@kbc.co.kr
'''

p=re.compile('.*[@].*[.](?=com$|net$).*$')

print(p.search('kim@daum.net'))
print(p.search('lee@naver.com'))
print(p.search('park@kbc.co.kr'))