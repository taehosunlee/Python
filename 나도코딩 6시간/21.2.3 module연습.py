# 모듈은 내가 쓰려는 모듈과 같은 폴더거나, 파이썬라이브러리들이 모여있는 폴더에서 사용 가능.
# 필요한 것들끼리 묶음처럼 잘 만들어진 파일
# 자동차를 하나 만들어놓고, 필요에 따라 바퀴라던지 부품이라던지 갈 수 있듯이,  모듈도 자동차와 같음
# 모듈은 확장자가 .py이다.


# 극장이 있는데, 현금만 받는다. 잔돈을 안바꿔준다.
# 우리가 미리, 극장에 가기 전에 가격을 미리 알 수 있는 모듈을 만들어보자.

#######################################################################################################

#1)
# import theater_module

# theater_module.price(3) #3명이서 영화 보러 갔을 때 가격
# theater_module.price_soldier(4)

#2)
# import theater_module as mv  # 별명 씌워주기.
# mv.price_soldier(5)


#3)
# from theater_module import *  # theater module을 그냥 쓰겠다.
# price_soldier(5)

#4)
# from theater_module import price, price_morning # 시어터 모듈에서 함수를 선택적으로 가져오겠다.
# price(5)
# price_morning(2)
# # 솔져만 사용 불가

from theater_module import price_soldier as price  # price soldier 만 가져오고, price로 하겠다.
price(3)  #3명 군인이 됨.
