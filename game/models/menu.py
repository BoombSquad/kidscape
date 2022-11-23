
import pygame, sys
from models.player import Player
from models.button import Button
from models.game import Game
from pygame import mixer

menu_surface = pygame.display.set_mode((1280, 720))
BG = pygame.image.load("assets/images/backgrounds/Background.png")
pause_background = pygame.image.load("assets/images/backgrounds/pause.png")

mixer.init()
backgroundSound = pygame.mixer.Sound("../game/assets/sounds/background.wav")
backgroundSound.set_volume(0.1)
backgroundSound.play(-1)

class Menu():

    def __init__(self):

        pygame.init()
        # self.game = Game(self)
        self.game = Game(self)

    def get_font(self, size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/fonts/font.ttf", size)

    def pause(self, game_surface):
        game_surface.blit(pause_background, (0,0))
        while True:                   
            
            PAUSE_MOUSE_POS = pygame.mouse.get_pos()

            PAUSE_TEXT = self.get_font(100).render("PAUSE", True, "#b68f40")
            PAUSE_RECT = PAUSE_TEXT.get_rect(center=(640, 100))

            RESUME_BUTTON = Button(None, pos=(640, 350), 
                                text_input="CONTINUAR", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            MENU_BUTTON = Button(None, pos=(640, 500), 
                                text_input="MENU", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            menu_surface.blit(PAUSE_TEXT, PAUSE_RECT)

            for button in [RESUME_BUTTON, MENU_BUTTON]:
                button.changeColor(PAUSE_MOUSE_POS)
                button.update(game_surface)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if RESUME_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                        self.play()
                    if MENU_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                        self.main_menu()
            
            pygame.display.update()

    def game_over(self, game_surface, points):
        if(points < 0):
            points = - points
        game_surface.blit(pause_background, (0,0))

        base_font = pygame.font.Font("assets/fonts/font.ttf", 32)
        user_text = ''
        input_rect = pygame.Rect(490, 300, 300, 60)
        color_active = pygame.Color('#d6dcd3')
        color_passive = pygame.Color('#d6dcd3')
        color = color_passive
        active = False

        while True:                   
            
            PAUSE_MOUSE_POS = pygame.mouse.get_pos()

            GAME_OVER_TEXT = self.get_font(100).render("GAME OVER", True, "#b68f40")
            GAME_OVER_RECT = GAME_OVER_TEXT.get_rect(center=(640, 150))

            POINTS = Button(None, pos=(640, 500), 
                                text_input=str(points), font=self.get_font(75), base_color="#d7fcd4", hovering_color="#d7fcd4")
            MENU_BUTTON = Button(None, pos=(640, 600), 
                                text_input="MENU", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            menu_surface.blit(GAME_OVER_TEXT, GAME_OVER_RECT)

            for button in [POINTS, MENU_BUTTON]:
                button.changeColor(PAUSE_MOUSE_POS)
                button.update(game_surface)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if MENU_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                        f = open("leaderboard.txt", "a")
                        if(user_text == ''):
                            user_text = "Player unknown"
                        if(user_text.__contains__(';')):
                            user_text = user_text.replace(';','')
                        f.write(user_text+":"+ str(points)+';\n')
                        f.close()
                        self.main_menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(PAUSE_MOUSE_POS):
                        active = True
                    else:
                        active = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        if user_text.__len__() < 9:
                            user_text += event.unicode
                        else:
                            pass
            if active:
                color = color_active
            else:
                color = color_passive
            
            pygame.draw.rect(menu_surface, color, input_rect)
            text_surface = base_font.render(user_text, True, (255, 255, 255))
            menu_surface.blit(text_surface, (input_rect.x+5, input_rect.y+5))
            input_rect.w = max(100, text_surface.get_width()+10)
            pygame.display.update()

    def victory(self, game_surface, points):
        if(points < 0):
            points = -points
        
        game_surface.fill((0,0,0))

        base_font = self.get_font(32)
        user_text = ''
        input_rect = pygame.Rect(490, 300, 300, 60)
        color_active = pygame.Color('#d6dcd3')
        color_passive = pygame.Color('#d6dcd3')
        color = color_passive
        active = False

        while True:                   
            
            PAUSE_MOUSE_POS = pygame.mouse.get_pos()

            VITORIA_TEXT = self.get_font(100).render("VITORIA", True, "#b68f40")
            VITORIA_RECT = VITORIA_TEXT.get_rect(center=(640, 150))

            POINTS = Button(None, pos=(640, 450), 
                                text_input=str(points), font=self.get_font(75), base_color="#d7fcd4", hovering_color="#d7fcd4")
            MENU_BUTTON = Button(None, pos=(640, 600), 
                                text_input="MENU", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            menu_surface.blit(VITORIA_TEXT, VITORIA_RECT)

            for button in [POINTS, MENU_BUTTON]:
                button.changeColor(PAUSE_MOUSE_POS)
                button.update(game_surface)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if MENU_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                        f = open("leaderboard.txt", "a")
                        if(user_text == ''):
                            user_text = "Player unknown"
                        if(user_text.__contains__(';')):
                            user_text = user_text.replace(';','')
                        f.write(user_text+":"+ str(points)+';\n')
                        f.close()
                        self.main_menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(PAUSE_MOUSE_POS):
                        active = True
                    else:
                        active = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        if user_text.__len__() < 9:
                            user_text += event.unicode
                        else:
                            pass
            if active:
                color = color_active
            else:
                color = color_passive
            
            pygame.draw.rect(menu_surface, color, input_rect)
            text_surface = base_font.render(user_text, True, (255, 255, 255))
            menu_surface.blit(text_surface, (input_rect.x+5, input_rect.y+5))
            input_rect.w = max(100, text_surface.get_width()+10)
            pygame.display.update()           

    def main_menu(self):
        self = Menu()
        soundOn = pygame.image.load("../game/assets/images/sound-on.png")
        soundOff = pygame.image.load("../game/assets/images/sound-off.png")
        leaderboard = pygame.image.load("../game/assets/images/leaderboard.png")

        sound = soundOn
        #self.game = Game(self)
        pygame.display.set_caption("Menu")
        while True:
            menu_surface.blit(BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(100).render("KID ESCAPE", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            PLAY_BUTTON = Button(None, pos=(640, 250), 
                                text_input="JOGAR", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(None, pos=(640, 420), 
                                text_input="INSTRUÇÕES", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            MUSIC_BUTTON = Button(image=sound, pos=(1200, 640), text_input= None,
                                 font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            LEADERBOARD = Button(image=leaderboard, pos=(80, 640), text_input= None,
                                 font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(None, pos=(640, 570), 
                                text_input="SAIR", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            menu_surface.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, MUSIC_BUTTON, LEADERBOARD]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(menu_surface)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.play()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.options()
                    if MUSIC_BUTTON.checkForInput(MENU_MOUSE_POS):
                        if sound == soundOff:
                            sound = soundOn
                            backgroundSound.set_volume(0.1)
                        else:
                            sound = soundOff
                            backgroundSound.set_volume(0)
                    if LEADERBOARD.checkForInput(MENU_MOUSE_POS):
                        self.leaderboard()

                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    def options(self):

        pygame.display.set_caption("Instrucoes")
        while True:
        
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            menu_surface.fill("white")

            HEADER = self.get_font(45).render("Instrucoes", True, "Black")
            OPTIONS = self.get_font(35).render("Use as setas para se movimentar", True, "Black")
            UP = self.get_font(35).render(" \u2191 para andar para cima", True, "Black")
            RIGHT = self.get_font(35).render(" \u2192 para andar para direita", True, "Black")
            DOWN = self.get_font(35).render(" \u2193 para andar para baixo", True, "Black")
            LEFT = self.get_font(35).render(" \u2190 para andar para esquerda", True, "Black")

            HEADER_RECT = HEADER.get_rect(center=(640, 60))
            OPTIONS_RECT = OPTIONS.get_rect(center=(640, 120))
            UP_RECT = UP.get_rect(center=(640, 260))
            RIGHT_RECT = RIGHT.get_rect(center=(640, 360))
            DOWN_RECT = DOWN.get_rect(center=(640, 460))
            LEFT_RECT = LEFT.get_rect(center=(640, 560))

            menu_surface.blit(HEADER, HEADER_RECT)
            menu_surface.blit(OPTIONS, OPTIONS_RECT)
            menu_surface.blit(UP, UP_RECT)
            menu_surface.blit(RIGHT, RIGHT_RECT)
            menu_surface.blit(DOWN, DOWN_RECT)
            menu_surface.blit(LEFT, LEFT_RECT)

            OPTIONS_BACK = Button(image=None, pos=(640, 660), 
                                text_input="VOLTAR", font=self.get_font(75), base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(menu_surface)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        self.main_menu()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.main_menu()

            pygame.display.update()

    def play(self):
        pygame.display.set_caption("Jogo")
        self.game.main()

    def leaderboard(self):
        menu_surface.blit(BG, (0, 0))

        topFive = []
        pygame.draw.rect(menu_surface, (255,255,255), pygame.Rect(240, 150, 800, 400), 4)
        r = open("leaderboard.txt", "r")
        games = r.readlines()
        scoreBoard = []
        
        for playerScore in games:
            playerScore = playerScore.replace('\n', '')
            playerScore = playerScore.replace(';', '')
            selectedPlayerScore = playerScore.split(':')
            scoreBoard.append(Player(selectedPlayerScore))
        scoreBoard = sorted(scoreBoard, key= lambda self : self.sortPoints(), reverse=True)
        for i in range(5):
            if  i >= scoreBoard.__len__():
                topFive.append(Player(("?????","0000")))
            else: 
                topFive.append(scoreBoard[i])


        while True:                   
            PAUSE_MOUSE_POS = pygame.mouse.get_pos()
            
            
            LEADERBOARD = self.get_font(50).render("CLASSIFICAÇÃO", True, "#b68f40")
            LEADERBOARD_RECT = LEADERBOARD.get_rect(center=(640, 80))
            menu_surface.blit(LEADERBOARD, LEADERBOARD_RECT)


            MENU_BUTTON = Button(None, pos=(640, 640), text_input="MENU", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            
            PLAYER_ONE_NAME = self.get_font(15).render("1 : "+topFive[0].name, True, "#b68f40")
            PLAYER_ONE_NAME_RECT = PLAYER_ONE_NAME.get_rect(topleft=(360, 220))
            PLAYER_ONE_POINTS = self.get_font(15).render(str(topFive[0].points), True, "#b68f40")
            PLAYER_ONE_POINTS_RECT = PLAYER_ONE_POINTS.get_rect(topright=(900, 220))

            PLAYER_TWO_NAME = self.get_font(15).render("2 : "+topFive[1].name, True, "#b68f40")
            PLAYER_TWO_NAME_RECT = PLAYER_TWO_NAME.get_rect(topleft=(360, 280))
            PLAYER_TWO_POINTS = self.get_font(15).render(str(topFive[1].points), True, "#b68f40")
            PLAYER_TWO_POINTS_RECT = PLAYER_TWO_POINTS.get_rect(topright=(900, 280))

            PLAYER_THREE_NAME = self.get_font(15).render("3 : "+topFive[2].name, True, "#b68f40")
            PLAYER_THREE_NAME_RECT = PLAYER_THREE_NAME.get_rect(topleft=(360, 340))
            PLAYER_THREE_POINTS = self.get_font(15).render(str(topFive[2].points), True, "#b68f40")
            PLAYER_THREE_POINTS_RECT = PLAYER_THREE_POINTS.get_rect(topright=(900, 340))

            PLAYER_FOUR_NAME = self.get_font(15).render("4 : "+topFive[3].name, True, "#b68f40")
            PLAYER_FOUR_NAME_RECT = PLAYER_FOUR_NAME.get_rect(topleft=(360, 400))
            PLAYER_FOUR_POINTS = self.get_font(15).render(str(topFive[3].points), True, "#b68f40")
            PLAYER_FOUR_POINTS_RECT = PLAYER_FOUR_POINTS.get_rect(topright=(900, 400))

            PLAYER_FIVE_NAME = self.get_font(15).render("5 : "+topFive[4].name, True, "#b68f40")
            PLAYER_FIVE_NAME_RECT = PLAYER_FIVE_NAME.get_rect(topleft=(360, 460))
            PLAYER_FIVE_POINTS = self.get_font(15).render(str(topFive[4].points), True, "#b68f40")
            PLAYER_FIVE_POINTS_RECT = PLAYER_FIVE_POINTS.get_rect(topright=(900, 460))

            menu_surface.blit(PLAYER_ONE_NAME, PLAYER_ONE_NAME_RECT)
            menu_surface.blit(PLAYER_ONE_POINTS, PLAYER_ONE_POINTS_RECT) 

            menu_surface.blit(PLAYER_TWO_NAME, PLAYER_TWO_NAME_RECT)
            menu_surface.blit(PLAYER_TWO_POINTS, PLAYER_TWO_POINTS_RECT)

            menu_surface.blit(PLAYER_THREE_NAME, PLAYER_THREE_NAME_RECT)
            menu_surface.blit(PLAYER_THREE_POINTS, PLAYER_THREE_POINTS_RECT)

            menu_surface.blit(PLAYER_FOUR_NAME, PLAYER_FOUR_NAME_RECT)
            menu_surface.blit(PLAYER_FOUR_POINTS, PLAYER_FOUR_POINTS_RECT)

            menu_surface.blit(PLAYER_FIVE_NAME, PLAYER_FIVE_NAME_RECT)
            menu_surface.blit(PLAYER_FIVE_POINTS, PLAYER_FIVE_POINTS_RECT)

            for button in [MENU_BUTTON]:
                button.changeColor(PAUSE_MOUSE_POS)
                button.update(menu_surface)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if MENU_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                        self.main_menu()
            
            pygame.display.update()

        