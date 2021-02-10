# 집합 (set)
# 중복안됨, 순서없음  --> sample, shuffle 사용불가능.

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

print(java)
print(python)

# 교집합 ( java와 python 모두 할 수 있는 사람)
print(java & python)
print(java.intersection(python))

# 합집합 (java나 python 할 수 있는 사람)
print(java | python)
print(java.union(python))

# 차집합 ( java - python )
print( java - python)
print(java.difference(python))

# python 을 할 줄 아는 사람이 들어남.
python.add("김태호")

print(python)

# java을 까먹었어요.
java.remove("김태호")

print(java)