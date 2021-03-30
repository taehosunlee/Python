import pygame
from random import *
#################################################################################################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init()

# 화면크기 설정
screen_width = 640 
screen_height = 480 
screen=pygame.display.set_mode((screen_width,screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("COLLISION") #게임 이름


# FPS (초당 프레임수)
clock = pygame.time.Clock()



#################################################################################################################################


# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

background=pygame.image.load('C:\\Users\\Tae_Min_Love\\Desktop\\Phython Work Space\\.vscode\\pygame_basic\\background3.png')
character=pygame.image.load('C:\\Users\\Tae_Min_Love\\Desktop\\Phython Work Space\\.vscode\\pygame_basic\\character2.png')
enemy = pygame.image.load('C:\\Users\\Tae_Min_Love\\Desktop\\Phython Work Space\\.vscode\\pygame_basic\\enemy2.png')


game_font = pygame.font.Font(None, 40) # 폰트 객체 생성
total_time = 60
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴


character_rect = character.get_rect()
character_size = character_rect.size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2 - character_width/2)
character_y_pos = (screen_height - character_height)

enemy_rect = enemy.get_rect()
enemy_size = enemy_rect.size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randint(0,screen_width-enemy_width)
enemy_y_pos = 0
enemy_speed = 6

to_x = 0
to_y = 0

speed = 0.5




running = True

while running : 
    dt = clock.tick(60) 

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_LEFT : 
                to_x -= speed

            elif event.key == pygame.K_RIGHT :
                to_x += speed
        
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT : 
                to_x=0


    # 케릭터 위치 정의
    character_x_pos += to_x * dt

    if character_x_pos <0 : 
        character_x_pos = 0

    elif character_x_pos > screen_width-character_width : 
        character_x_pos = screen_width-character_width

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height : 
        enemy_y_pos = 0
        enemy_x_pos = randint(0,screen_width-enemy_width)



    # 4. 충돌 처리

    character_rect = character.get_rect() 
                                          
    character_rect.left = character_x_pos 
    character_rect.top = character_y_pos  

    enemy_rect = enemy.get_rect() 
    enemy_rect.left = enemy_x_pos 
    enemy_rect.top = enemy_y_pos  

    if character_rect.colliderect(enemy_rect) :
        print("충돌 했어요")
        running = False


    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  #milisecond라서 나눠줌.  초 단위로 표시.

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255)) # render : 표시하는 것.   render 출력할 글자, Antialiace(항상 트루), 색깔(rgb)

    if total_time - elapsed_time <= 0 :
        print("time out")
        running=False


    # 5. 화면에 그리기

    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    screen.blit(timer,(10,10))

    pygame.display.update()

# 잠시 대기
pygame.time.delay(2000) #2초정도 대기

# pygame 종료
pygame.quit()