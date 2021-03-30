import pygame

pygame.init() # 1) 파이게임 초기화

# 화면크기 설정
screen_width = 480 
screen_height = 640 
screen=pygame.display.set_mode((screen_width,screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름


# 배경 이미지 불러오기
background=pygame.image.load('C:\\Users\\Tae_Min_Love\\Desktop\\Phython Work Space\\.vscode\\pygame_basic\\background.png')


# 캐릭터(스프라이트) 불러오기
character=pygame.image.load('C:\\Users\\Tae_Min_Love\\Desktop\\Phython Work Space\\.vscode\\pygame_basic\\character.png')
character_size = character.get_rect().size # 이미지의 크기를 구해옴. rect : 사각형 렉텡귤러
character_width = character_size[0] # 캐릭터 가로크기
character_height = character_size[1] # 캐릭터 세로크기
character_x_pos = (screen_width /2) - (character_width/2) # 캐릭터 가로위치.   화면 가로의 절반에 위치  빼주는 이유는 0,0이 맨왼쪽 맨위이기 때문.
character_y_pos = (screen_height) - (character_height) # 캐릭터 세로위치.     화면 맨 밑에 위치.




# 이벤트 루프 
running = True #게임이 진행중인지 확인 

while running :  #게임이 진행중이면 계속 실행.
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False 

    screen.blit(background, (0,0))  # 배경그리기
    screen.blit(character, (character_x_pos,character_y_pos)) # 캐릭터 그려주기.

    pygame.display.update() # 게임화면 업데이트



# pygame 종료
pygame.quit()