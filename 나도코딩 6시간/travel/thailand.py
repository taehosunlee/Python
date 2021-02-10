class ThailandPackage : 
    def detail (self) : 
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")


# trp = ThailandPackage()
# trp.detail()


# trp를 타이패키지 클래스에 종속시킴.  그럼 타이패키지 내의 함수들을 사용 가능.
# trp.detail() 을 통해  detail함수를 사용.



# 실제 패키지나 모듈을 만들 때는, 그 모듈이 잘 작동하나 테스트를 해봐야한다.

if __name__ == "__main__" :  # name(~~.py)이 메인(~~.py)이면, Thailand 모듈을 직접 실행한다.
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할때만 실행돼요.")
    trip_to = ThailandPackage()
    trip_to.detail()
else :
    print("Thailand 외부에서 모듈 호출")