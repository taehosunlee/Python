# 모듈들을 모아둔 것. 모듈의 집합
# 폴더 만들어서 진행. travel 


# import travel.thailand  ## import 뒤에 오는 부분은 항상.  모듈이나 패키지만 가능.  class나 함수는 불가능
# trp_to = travel.thailand.ThailandPackage()
# trp_to.detail


# import travel.thailand.ThailandPackage()  ## 이렇게 사용은 불가능하다. class 못들어오므로
# trp_to = travel.thailand.ThailandPackage()
# trp_to.detail

# from travel.thailand import ThailandPackage  ## 이렇게 사용은 가능하다. 해당 패키지, 모듈에서 Class,함수 import 가능
# trp_to = ThailandPackage()
# trp_to.detail()

# from travel import vietnam  ## 이렇게 사용은 가능하다. 해당 패키지, 모듈에서 Class,함수 import 가능
# trp_to = vietnam.VietnamPackage()
# trp_to.detail()


# from random import *
from travel import *
trp_to = vietnam.VietnamPackage()  # 이러면 오류난다. 왜? *을 쓴다는 것은 travel이라는 패키지에 있는 모든것을 가져오겠다는 건데, 우리가 실제로는 개발자가 이 문법 상에서
                                   # 공개 범위를 설정해줘야한다.  원하는 것은 공개 ,원하지 않는 것은 비공개로.   __ini__을 열어서 수정해주자(수정 전엔 아무것도 없었음)
                                   # __all__ = ["vietnam"]  이라고 써준 후, vietnam 가져온다
trp_t = thailand.ThailandPackage() # 타일랜드도 정의해준 뒤 에러 안난다.
trp_to.detail()
trp_t.detail()







# 실제 패키지나 모듈을 만들 때는, 그 모듈이 잘 작동하나 테스트를 해봐야한다.
# 해당 모듈로 들어가 if__name~~ 문 사용


# 