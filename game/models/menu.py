
import pygame, sys
from models.button import Button
from models.game import Game
from models.level import Level

menu_surface = pygame.display.set_mode((1280, 720))
BG = pygame.image.load("assets/images/backgrounds/Background.png")
pause_background = pygame.image.load("assets/images/backgrounds/pause.png")

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

    def main_menu(self):
        pygame.display.set_caption("Menu")
        while True:
            menu_surface.blit(BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(100).render("KID SCAPE", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            PLAY_BUTTON = Button(None, pos=(640, 250), 
                                text_input="JOGAR", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(None, pos=(640, 400), 
                                text_input="INSTRUÇÕES", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(None, pos=(640, 550), 
                                text_input="SAIR", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            menu_surface.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
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
                                text_input="BACK", font=self.get_font(75), base_color="Black", hovering_color="Green")

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