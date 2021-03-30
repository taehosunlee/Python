import pygame

#################################################################################################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init()

# 화면크기 설정
screen_width = 480 
screen_height = 640 
screen=pygame.display.set_mode((screen_width,screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("COLLISION") #게임 이름


# FPS (초당 프레임수)
clock = pygame.time.Clock()

#################################################################################################################################


# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

running = True

while running : 
    dt = clock.tick(60) 

    # 2. 이벤트 처리 (키보드, 마우스 등)
    
    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기

    pygame.display.update()

# 잠시 대기
pygame.time.delay(2000) #2초정도 대기

# pygame 종료
pygame.quit()