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


# 적 enemy 캐릭터
enemy=pygame.image.load('C:\\Users\\Tae_Min_Love\\Desktop\\Phython Work Space\\.vscode\\pygame_basic\\enemy.png')
enemy_size = enemy.get_rect().size 
enemy_width = enemy_size[0] 
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width /2) - (enemy_width/2)
enemy_y_pos = (screen_height/2) - (enemy_height/2)



#### 텍스트 넣기
# 1. 폰트정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성

# 총 시간 넣기
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴



# 이벤트 루프 
running = True #게임이 진행중인지 확인 

while running :  #게임이 진행중이면 계속 실행.
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수 설정


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
    
    character_x_pos += to_x * dt  
    character_y_pos += to_y * dt  
 

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


    # 충돌 처리
    character_rect = character.get_rect() 
                                          
    character_rect.left = character_x_pos 
    character_rect.top = character_y_pos  

    enemy_rect = enemy.get_rect() 
    enemy_rect.left = enemy_x_pos 
    enemy_rect.top = enemy_y_pos  

    # 충돌 체크

    if character_rect.colliderect(enemy_rect) :
        print("충돌 했어요")
        running = False


    # 타이머 집어넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  #milisecond라서 나눠줌.  초 단위로 표시.

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255)) # render : 표시하는 것.   render 출력할 글자, Antialiace(항상 트루), 색깔(rgb)

    if total_time - elapsed_time <= 0 :
        print("time out")
        running=False


    # 화면표현

    screen.blit(background, (0,0))  # 배경그리기
    screen.blit(character, (character_x_pos,character_y_pos)) # 캐릭터 그려주기.
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos)) # 적 그려주기
    screen.blit(timer, (10,10))

    pygame.display.update()

# 종료 전 잠시 대기
pygame.time.delay(2000) #2초정도 대기



# pygame 종료
pygame.quit()