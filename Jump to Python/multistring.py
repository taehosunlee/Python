# multistring.py


print("="*50)
print("My program")
print("="*50)

a= "Life is too short"
print(len(a))


b = "You need python"
c=len(b)
print(c)
print(b[:3])
print(b[-1])
print(b[-3:])
print(b[:-3])



d=""
for i in range(0,7):
    d += str(b[i])
print(d)
print(b[:7])


x="Pithon"
'''
x[1]="y"

print(x) # 오류난다.

#문자열의 요소값은 바꿀 수 없다. immutable한 자료형.
'''

print(x[:1]+"y"+x[2:])


print("I ate %d apples" %3)
print("I want to eat %d %s" %(3,"oranges"))

print("-"*50)

print("%s jane" %"hi")  #%s 뒤에 숫자, 소수 등이와도 된다. 모두 문자열로 변환해서 나타내버림.
print("%10s jane" %"hi")
print("%-10s jane" %"hi")
print("%f" %3.4213432456)  #소수 그대로 6째자리까지 가져옴
print("%0.f" %3.4213432456)  #정수부분 가져옴.
print("%0.8f" %3.4213432456)  # 소수점 8자리까지
print("%10.4f" %3.4213432)  # 총 10칸 + 소수점 4자리




number = 10
days = "three"
print("I ate {number} apples. so i was sick for {day} days".format(number=70,day="three"))


print("-"*50)

print("{0:<10}".format("hi")) #왼쪽정렬 10칸
print("{0:>10}".format("hi")) #오른쪽정렬 10칸
print("{0:^10}".format("hi")) #가운데정렬 10칸

print("{0:!>10}".format("hi")) #오른쪽정렬 10칸, !로 채우기
print("{0:@^10}".format("hi")) #가운데정렬 10칸, @로 채우기

native=3.412591456
print("{0:10.6f}".format(native)) #10자리, 소수점6째자리까지.



print("{and}")
print("{{and}}".format())  # 중괄호를 포매팅 문자가 아닌 글자 그대로의 {}로 쓰고싶으면, {{}} 두개씩 쓰면 된다.


print("-"*50)


'''파이선 3.6부터는 f' 문자열 포매팅기능 사용가능하다'''
name="이태호"
age=30
print(f"나의 이름은 {name}입니다. 나이는 {age}입니다")


# format or f' 을 이용해서 "!!!Python!!!" 을 나타내보자.
print("{0:!^12}".format("Python"))
print(f"{'python':!^12}")   #'," 혼용해서 써야했음. f"{"python":!^12}" 이면 에러뜸

a = "Python"
print("{0:!^12}".format(a))
print(f"{a:!^12}")



q= "Python is really fun and easy"


print(q.find("d"))  # d의 위치 찾기. 잘못된거 입력되도 에러 안남
print(q.index("d"))  # d의 위치 찾기. 잘못된거 입력되면 러남
print(q.count("n"))

t='abcd'
print(",".join(t))  # t 각 문자들 사이에 ,를 넣는다.

y= ["a","b","c","d"]  # join   list에도 사용 가능
print(",".join(y))





# 공백 지우기
a= "   hi    "
print(a.lstrip()) #왼공백 지우기
print(a.rstrip()) #오른공백 지우기
print(a.strip()) #양쪽 공백 지우기



# 문자열 바꾸기
a = "Life is too short"
a=a.replace("Life", "Your leg")

print(a)


# 문자열 나누기
a= "Life is too short"
b= "A : B : C : D = 1 : 2 : 3 : 4"

a=a.split() # 공백으로 나눔 -> 리스트 됨
b=b.split(":") # :로 나눔 -> 리스트 됨

print(a)
print(b)
