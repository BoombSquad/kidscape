
import pygame, sys
from models.button import Button

menu_surface = pygame.display.set_mode((1280, 720))
BG = pygame.image.load("assets/images/backgrounds/Background.png")

class Menu():

    def __init__(self):
        pass

    def get_font(self, size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/fonts/font.ttf", size)

    def main_menu(self):
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

        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            menu_surface.fill("white")

            OPTIONS_TEXT = self.get_font(45).render("This is the OPTIONS screen.", True, "Black")
            OPTIONS_TEXT1 = self.get_font(45).render("This is the OPTIONSssssss screen.", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
            OPTIONS_RECT1 = OPTIONS_TEXT1.get_rect(center=(640, 360))
            menu_surface.blit(OPTIONS_TEXT, OPTIONS_RECT)
            menu_surface.blit(OPTIONS_TEXT1, OPTIONS_RECT1)

            OPTIONS_BACK = Button(image=None, pos=(640, 460), 
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

            pygame.display.update()

    def play():
        pass