import pygame

pygame.init() # 1) 파이게임 초기화

# 화면크기 설정
screen_width = 480 
screen_height = 640 
screen=pygame.display.set_mode((screen_width,screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름


# FPS (초당 프레임수)
clock = pygame.time.Clock()


# 배경 이미지 불러오기
background=pygame.image.load('C:\\Users\\Tae_Min_Love\\Desktop\\Phython Work Space\\.vscode\\pygame_basic\\background.png')


# 캐릭터(스프라이트) 불러오기
character=pygame.image.load('C:\\Users\\Tae_Min_Love\\Desktop\\Phython Work Space\\.vscode\\pygame_basic\\character.png')
character_size = character.get_rect().size 
character_width = character_size[0] 
character_height = character_size[1]
character_x_pos = (screen_width /2) - (character_width/2)
character_y_pos = (screen_height) - (character_height)


#이동할 좌표
to_x = 0
to_y = 0


# 이동 속도
character_speed = 0.5


# 이벤트 루프 
running = True #게임이 진행중인지 확인 

while running :  #게임이 진행중이면 계속 실행.
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수 설정

# 캐릭터가 100 만큼 이동을 해야함
# 10 fps : 1초 동안에 10번 동작 -> 1번에 10만큼 이동 필요
# 20 fps : 1초 동안에 20번 동작 -> 1번에 5만큼 이동 필요
# 프레임에 따라 이동속도가 달라지면 안되기때문에, 보정을 해줘야한다!   x += to_x * dt 해줌.



    # print("fps : "+str(clock.get_fps())) 현재 프레임 보는 법

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_LEFT : 
                to_x -= character_speed

            elif event.key == pygame.K_RIGHT :
                to_x += character_speed

            elif event.key == pygame.K_UP :
                to_y -= character_speed

            elif event.key == pygame.K_DOWN :
                to_y += character_speed
        
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT : 
                to_x=0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN : 
                to_y=0
    
    character_x_pos += to_x * dt  ## 프레임에 상관없이 속도 동일하게 맞춰주기!  * dt
    character_y_pos += to_y * dt  ## 프레임에 상관없이 속도 동일하게 맞춰주기!  * dt
 

    # 가로 경계값 처리
    if character_x_pos <0 : 
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width : 
        character_x_pos = screen_width-character_width

    # 세로 경계값 처리
    if character_y_pos <0 : 
        character_y_pos = 0
    elif character_y_pos > screen_height-character_height :
        character_y_pos = screen_height-character_height



    screen.blit(background, (0,0))  # 배경그리기
    screen.blit(character, (character_x_pos,character_y_pos)) # 캐릭터 그려주기.

    pygame.display.update()



# pygame 종료
pygame.quit()