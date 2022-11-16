import pygame, sys
from models.demon import Demon
import random
from models.kid import Kid
from models.levelOne import LevelOne
from models.levelTwo import LevelTwo

SCREEN = pygame.display.set_mode((1280, 720))
directions = ["RIGHT", "LEFT", "UP", "DOWN"]

class Game():

    def __init__(self, menu, level=LevelTwo()):
        self.menu = menu
        self.startPosition = [80,130]
        self.kidPosition = level.initialKidPosition
        self.previousPosition = [80,130]
        self.kid = Kid(self.kidPosition)
        self.demonPosition = [0,0]
        self.demonPreviousPos = self.demonPosition
        self.demonDirection = "left"
        self.level = level
        self.level.createObstacles(SCREEN)

    def main(self):
        
        while self.kid.isAlive():
        # while True:
            if len(self.level.remainingKeys) == 0:
                self.level.openDoor()
                if self.level.checkDoorCollision(self.kidPosition):
                    nextLevel = self.level.getNextLevel()
                    Game(self.menu, nextLevel).main()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.menu.pause(SCREEN)


            if not self.kid.checkCollision(self.level):
                keys_pressed = pygame.key.get_pressed()
                if keys_pressed[pygame.K_LEFT] and self.kidPosition[0] >= 18:
                    self.kid.setSpriteDirection("LEFT")
                    self.previousPosition[0] = self.kidPosition[0]
                    self.kidPosition[0] -= self.level.speed

                elif keys_pressed[pygame.K_RIGHT] and self.kidPosition[0] <= 1236:
                    self.kid.setSpriteDirection("RIGHT")
                    self.previousPosition[0] = self.kidPosition[0]
                    self.kidPosition[0] += self.level.speed

                elif keys_pressed[pygame.K_UP] and self.kidPosition[1] >= 70:
                    self.kid.setSpriteDirection("UP")
                    self.previousPosition[1] = self.kidPosition[1]
                    self.kidPosition[1] -= self.level.speed

                elif keys_pressed[pygame.K_DOWN] and self.kidPosition[1] <= 650:
                    self.kid.setSpriteDirection("DOWN")
                    self.previousPosition[1] = self.kidPosition[1]
                    self.kidPosition[1] += self.level.speed

            if self.kid.checkCollision(self.level):
                if self.kid.isDemonCollision(self.level):
                    self.kid.lives -= 1
                    self.kidPosition = self.startPosition
                    print(self.kid.lives)
                    print(self.startPosition)
                else: 
                    self.kidPosition[0] = self.previousPosition[0]
                    self.kidPosition[1] = self.previousPosition[1]
            
            self.level.update(SCREEN)
            
            if self.level.fase == 2:

                if self.level.demon.isChasing(self):

                    self.level.demon.acc = 0.1

                    if self.kidPosition[0] > self.demonPosition[0]:
                        self.demonPosition[0] += self.level.demon.acc
                    if self.kidPosition[0] < self.demonPosition[0]:
                        self.demonPosition[0] -= self.level.demon.acc
                    if self.kidPosition[1] > self.demonPosition[1]:
                        self.demonPosition[1] += self.level.demon.acc
                    if self.kidPosition[1] < self.demonPosition[1]:
                        self.demonPosition[1] -= self.level.demon.acc
                else:

                    self.demonPosition[0] = self.level.demon.position_X
                    self.demonPosition[1] = self.level.demon.position_Y

                    if not self.level.demon.checkCollision(self.level):
                        if random.randint(0, 999) % 509 == 0 :
                            if self.level.demon.direction == "LEFT" and self.level.demon.stepsWalked < 5:
                                self.level.demon.stepsWalked += 1
                                if self.demonPosition[0] >= 18:
                                    self.demonPreviousPos[0] = self.demonPosition[0]
                                    self.demonPosition[0] -= self.level.demon.acc
                                
                            elif self.level.demon.direction == "RIGHT" and self.level.demon.stepsWalked < 5:
                                self.level.demon.stepsWalked += 1
                                if self.demonPosition[0] <= 1216:
                                    self.demonPreviousPos[0] = self.demonPosition[0]
                                    self.demonPosition[0] += self.level.demon.acc

                            elif self.level.demon.direction == "UP" and self.level.demon.stepsWalked < 5:
                                self.level.demon.stepsWalked += 1
                                if self.demonPosition[1] >= 70:
                                    self.demonPreviousPos[1] = self.demonPosition[1]
                                    self.demonPosition[1] -= self.level.demon.acc

                            elif self.level.demon.direction == "DOWN" and self.level.demon.stepsWalked < 5:
                                self.level.demon.stepsWalked += 1
                                if self.demonPosition[1] <= 650:
                                    self.demonPreviousPos[1] = self.demonPosition[1]
                                    self.demonPosition[1] += self.level.demon.acc

                            if self.level.demon.stepsWalked >= 5:
                                self.level.demon.setSpriteDirection(directions[random.randint(0,3)])
                                self.level.demon.stepsWalked = 0

                            if self.level.demon.checkCollision(self.level):
                                self.demonPosition[0] = self.demonPreviousPos[0]
                                self.demonPosition[1] = self.demonPreviousPos[1]

                self.level.demon.update(SCREEN, self.demonPosition)
                pygame.draw.rect(SCREEN,(255,255,255), self.level.demon.hitbox, 1)
                # self.demonDirection = directions[random.randint(0,3)]
            
            self.kid.update(SCREEN, self.kidPosition)
            
            #See Hitbox
            pygame.draw.rect(SCREEN,(255,255,255),self.kid.hitbox, 1)
            pygame.display.update()