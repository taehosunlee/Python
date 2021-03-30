# 활용편 게임개발
# pip install pygame으로 라이브러리 다운받아주고.

import pygame

pygame.init() # 1) 파이게임 초기화. 반드시 필요

# 화면크기 설정
screen_width = 480 #가로크기
screen_height = 640 #세로크기
pygame.display.set_mode((screen_width,screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름


# 이벤트 루프 : 프로그램이 종료되지 않도록, 키다운하거나 마우스를 움직이거나 하는 동작들을 계속 탐지하는 이벤트루프가 돌고있어야 창이 안꺼진다
running = True #게임이 진행중인지 확인 

while running :  #게임이 진행중이면 계속 실행.  pygame 라이브러리를 사용할거면 아래 작성하는 문구들 필수. 
    for event in pygame.event.get() :  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT : # 창이 닫히는 이벤트가 발생했는가?
            running = False # 게임이 진행중이 아님.



# pygame 종료
pygame.quit()