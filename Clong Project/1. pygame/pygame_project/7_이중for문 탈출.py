balls=[1,2,3,4]
weapons=[11,22,3,44]

for ball_idx,ball_val in enumerate(balls) : 
    print("ball : ", ball_val)
    for weapon_idx,weapon_val in enumerate(weapons) : 
        print("weapon : ", weapon_val)

        if ball_val==weapon_val :  # 충돌 체크
            print("공과 무기가 충돌")
            break # --> weapon에 대한 for만 탈출하고 ball에 대해선 계쏙 돈다.





# 이중 for 탈출하는 방법, 트릭

for ball_idx,ball_val in enumerate(balls) : 
    print("ball : ", ball_val)
    for weapon_idx,weapon_val in enumerate(weapons) : 
        print("weapon : ", weapon_val)

        if ball_val==weapon_val :  # 충돌 체크
            print("공과 무기가 충돌")
            break # --> weapon에 대한 for만 탈출하고 ball에 대해선 계쏙 돈다.

    else :
        continue  

    print("바깥 for 문 break")
    break

## for 도 else를 쓸 수 있다.  for 문 동작가능한 내용이 있으면 for문 돌고,  for문 동작할게 없어지면 else 돈다.
## else 를 continue로 해두면  ball의 for문도 계속 돌게된다.
## 다만  break가 발생하여 for~else 구문 전체를 탈출하게되는거고 그래서 else 밑의 print, break도 실행하며  ball for문도 나오게 되는 것이다.