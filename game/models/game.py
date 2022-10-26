import pygame, sys
from models.kid import Kid
from models.level import Level

SCREEN = pygame.display.set_mode((1280, 720))

class Game():

    def __init__(self, menu):
        self.menu = menu
        self.position = [80,130]
        self.previousPosition = [80,130]
        self.kid = Kid(self.position)

        self.level = Level(1)
        self.level.createObstacles()

    def main(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.menu.main_menu()
            
            if not self.kid.checkCollision(self.level.obstacles):
                keys_pressed = pygame.key.get_pressed()
                if keys_pressed[pygame.K_LEFT] and self.position[0] >= 18:
                    self.kid.setSpriteDirection("LEFT")
                    self.previousPosition[0] = self.position[0]
                    self.position[0] -= self.level.speed

                elif keys_pressed[pygame.K_RIGHT] and self.position[0] <= 1236:
                    self.kid.setSpriteDirection("RIGHT")
                    self.previousPosition[0] = self.position[0]
                    self.position[0] += self.level.speed

                elif keys_pressed[pygame.K_UP] and self.position[1] >= 70:
                    self.kid.setSpriteDirection("UP")
                    self.previousPosition[1] = self.position[1]
                    self.position[1] -= self.level.speed

                elif keys_pressed[pygame.K_DOWN] and self.position[1] <= 650:
                    self.kid.setSpriteDirection("DOWN")
                    self.previousPosition[1] = self.position[1]
                    self.position[1] += self.level.speed

            if self.kid.checkCollision(self.level.obstacles):
                self.position[0] = self.previousPosition[0]
                self.position[1] = self.previousPosition[1]

            #See Hitbox
            #pygame.draw.rect(SCREEN,(255,255,255),bed.hitbox, 1)
            
            self.level.update(SCREEN)
            self.kid.update(SCREEN, self.position)
            
            #See Hitbox
            #pygame.draw.rect(SCREEN,(255,255,255),KID.hitbox, 1)
            pygame.display.update()