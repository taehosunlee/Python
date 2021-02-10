#반복문 내에서 사용가능. 선생님이 교실에서 학생들에게 책을 읽으라고 시킴.
#출석번호 1~xx.

'''continue를 만났을 때는 더이상 그 다음문장을 실행하지 않고, 위로올라가
반복문 실행. break를 만나면 끝내버람.'''

absent = [2,3] # 2번 5번 결석함. --> 책을 읽힐 수 없음.
nobook = [7] #책을 깜빡했음.
for student in range(1,11) :      #출석번호 1~10까지 있음.
    if student in absent : 
        continue   # continue를 만나게 되면은 밑으로 내려가지 않고,
                    # 위로 다시 올라가서 다음 번호 실행한다.
    elif student in nobook : 
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break  # break는 끝낸다.
    print("{0}, 책을 읽어봐".format(student))


