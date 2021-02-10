# 리스트 []  --> sample, shuffle 사용가능.

# 지하철 칸별로 10명, 20명, 30명

subway1 = 10
subway2 = 20
subway3 = 30  #  이것들을 하나의 연속적인 공간으로 묶는 법

subway = [10,20,30]

print(subway)

subway = ["유재석","조세호","박명수"]

print(subway)
print(subway[0])

# 조세호씨가 몇 번째 칸에 타고있는지?

print(subway.index("유재석")+1) #index는 0부터 시작

# 다음 정류자에서, 하하가 탔다

subway.append("하하")  #  append : 리스트에 추가.  항상 맨 뒤에 붙음.

print(subway)

# 정형돈씨를 유재석/조세호 사이에 태우기.

subway.insert(1,"정형돈")  #  정형돈을 index 1의 위치에 넣기.

print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄

print(subway.pop())  # 맨 끝에 있는 사람 빼고,  뺀 사람 보여줌. 빼는거 print에 있어도 먹음.
print(subway)  #남은 사람 보여준다

print(subway.pop())
print(subway) 

print(subway.pop())  
print(subway)  


# 같은 이름의 사람이 몇 명 있는지 확인하기
subway.append("유재석")
print(subway)

print(subway.count("유재석"))





num_list = [5,2,4,1,3]

#순서 뒤집기 (reverse)
num_list.reverse()

print(num_list)

#정렬하기 (sort)
num_list.sort()

print(num_list)


#모두 지우기 (clear)

num_list.clear()
print(num_list)


# 다양한 자료형 함께 사용 (str,num,f)

mix_list = ["조세호",20,True]
num_list = [5,2,4,1,3]

print(mix_list)

# 리스트 확장 (extend)
num_list.extend(mix_list)
print(mix_list)
print(num_list)