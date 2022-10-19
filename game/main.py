import pygame, sys
from models.button import Button
from models.kid import Kid
from models.obstacle import Obstacle

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")
BGP = pygame.image.load("assets/play-background.jpg")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    position = [640,260]
    previousPosition = [640,260]
    KID = Kid(position)
    bed = Obstacle((370,320),"assets/bed.png")
    
    while True:
        speed = 0.2
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BGP, (0, 0))

        '''
        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        test = [bed]
        
        if not KID.checkCollision(test):
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_LEFT] and position[0] >= 32:
                KID.setSpriteDirection("LEFT")
                previousPosition[0] = position[0]
                position[0] -= speed

            elif keys_pressed[pygame.K_RIGHT] and position[0] <= 1248:
                KID.setSpriteDirection("RIGHT")
                previousPosition[0] = position[0]
                position[0] += speed

            elif keys_pressed[pygame.K_UP] and position[1] >= 70:
                KID.setSpriteDirection("UP")
                previousPosition[1] = position[1]
                position[1] -= speed

            elif keys_pressed[pygame.K_DOWN] and position[1] <= 680:
                KID.setSpriteDirection("DOWN")
                previousPosition[1] = position[1]
                position[1] += speed

        if KID.checkCollision(test):
            position[0] = previousPosition[0]
            position[1] = previousPosition[1]

        bed.update(SCREEN)
        #See Hitbox
        #pygame.draw.rect(SCREEN,(255,255,255),bed.hitbox, 1)
        
        KID.update(SCREEN, position)
        
        #See Hitbox
        pygame.draw.rect(SCREEN,(255,255,255),KID.hitbox, 1)
        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_TEXT1 = get_font(45).render("This is the OPTIONSssssss screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        OPTIONS_RECT1 = OPTIONS_TEXT1.get_rect(center=(640, 360))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        SCREEN.blit(OPTIONS_TEXT1, OPTIONS_RECT1)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("KID SCAPE", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(None, pos=(640, 250), 
                            text_input="JOGAR", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(None, pos=(640, 400), 
                            text_input="INSTRUÇÕES", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(None, pos=(640, 550), 
                            text_input="SAIR", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
