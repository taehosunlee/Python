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
character_size = character.get_rect().size 
character_width = character_size[0] 
character_height = character_size[1]
character_x_pos = (screen_width /2) - (character_width/2)
character_y_pos = (screen_height) - (character_height)


#이동할 좌표
to_x = 0
to_y = 0




# 이벤트 루프 
running = True #게임이 진행중인지 확인 

while running :  #게임이 진행중이면 계속 실행.
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

        if event.type == pygame.KEYDOWN : # 키를 누르면
            if event.key == pygame.K_LEFT : # 왼쪽이동
                to_x -= 0.7
            elif event.key == pygame.K_RIGHT :
                to_x += 0.7
            elif event.key == pygame.K_UP :
                to_y -= 0.7
            elif event.key == pygame.K_DOWN :
                to_y += 0.7
        
        if event.type == pygame.KEYUP : #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT : # 방향키를 왼쪽 or 오른쪽으로 누르다가 떼면은
                to_x=0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN : # 방향키를 위쪽 or 아래쪽으로 누르다가 떼면은
                to_y=0
    
    character_x_pos += to_x
    character_y_pos += to_y


    # 가로 경계값 처리
    if character_x_pos <0 : #왼쪽보다 더 나가면
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width : #오른쪽 끝으로 가면
        character_x_pos = screen_width-character_width

    # 세로 경계값 처리
    if character_y_pos <0 : #위쪽보다 더 나가면
        character_y_pos = 0
    elif character_y_pos > screen_height-character_height : #아래 끝으로 가면
        character_y_pos = screen_height-character_height



    screen.blit(background, (0,0))  # 배경그리기
    screen.blit(character, (character_x_pos,character_y_pos)) # 캐릭터 그려주기.

    pygame.display.update()



# pygame 종료
pygame.quit()