import pygame, sys
from models.demon import Demon
import random
from models.kid import Kid
from models.levelOne import LevelOne
from models.levelTwo import LevelTwo
from models.levelThree import LevelThree

SCREEN = pygame.display.set_mode((1280, 720))
directions = ["RIGHT", "LEFT", "UP", "DOWN"]
clock = pygame.time.Clock()

class Game():

    def __init__(self, menu, level=LevelThree()):
        self.playerName = 'Teste'
        self.menu = menu
        self.kidPosition =[level.levelX,  level.levelY]
        self.previousPosition = [80,130]
        self.kid = Kid(self.kidPosition)
        self.demonPosition = [0,0]
        self.demonPreviousPos = self.demonPosition
        self.demonDirection = "left"
        self.level = level
        self.level.createObstacles(SCREEN)
        self.time = 0

    def main(self):
        while self.kid.isAlive():
            if len(self.level.remainingKeys) == 0:
                self.level.openDoor()
                if self.level.checkDoorCollision(self.kidPosition):
                    nextLevel = self.level.getNextLevel()
                    if nextLevel == 0:
                        self.menu.victory(SCREEN, self.kid.points, self.playerName)
                    self.kid.points += 20
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
                    self.kid.points -= 10
                    self.kidPosition[0] = self.level.levelX
                    self.kidPosition[1] = self.level.levelY
                else: 
                    self.kidPosition[0] = self.previousPosition[0]
                    self.kidPosition[1] = self.previousPosition[1]
            
            self.level.update(SCREEN)
            
            if self.level.fase == 2:

                if self.level.demon.isChasing(self):

                    self.level.demon.acc = 3
                    if self.kidPosition[0] > self.demonPosition[0]:
                        self.demonPosition[0] += self.level.demon.acc
                    if self.kidPosition[0] < self.demonPosition[0]:
                        self.demonPosition[0] -= self.level.demon.acc
                    if self.kidPosition[1] > self.demonPosition[1]:
                        self.demonPosition[1] += self.level.demon.acc
                    if self.kidPosition[1] < self.demonPosition[1]:
                        self.demonPosition[1] -= self.level.demon.acc
                else:
                    self.level.demon.acc = 3
                    self.demonPosition[0] = self.level.demon.position_X
                    self.demonPosition[1] = self.level.demon.position_Y

                    self.demonPreviousPos[0] = self.demonPosition[0]
                    self.demonPreviousPos[1] = self.demonPosition[1]
                    randomic = random.randint(0, 999)
                    if randomic % 99 == 0 :
                        if self.level.demon.direction == "LEFT" and self.level.demon.stepsWalked < 6:
                            self.level.demon.stepsWalked += 1
                            if self.demonPosition[0] >= 18:
                                self.demonPosition[0] -= self.level.demon.acc
                            
                        elif self.level.demon.direction == "RIGHT" and self.level.demon.stepsWalked < 6:
                            self.level.demon.stepsWalked += 1
                            if self.demonPosition[0] <= 1236:
                                self.demonPosition[0] += self.level.demon.acc

                        elif self.level.demon.direction == "UP" and self.level.demon.stepsWalked < 6:
                            self.level.demon.stepsWalked += 1
                            if self.demonPosition[1] >= 70:
                                self.demonPosition[1] -= self.level.demon.acc

                        elif self.level.demon.direction == "DOWN" and self.level.demon.stepsWalked < 6:
                            self.level.demon.stepsWalked += 1
                            if self.demonPosition[1] <= 650:
                                self.demonPosition[1] += self.level.demon.acc

                        if self.level.demon.stepsWalked >= 6:
                            self.level.demon.setSpriteDirection(directions[random.randint(0,3)])
                            self.level.demon.stepsWalked = 0

                self.level.demon.update(SCREEN, self.demonPosition)
                #pygame.draw.rect(SCREEN,(255,255,255), self.level.demon.hitbox, 1)
            
            self.kid.update(SCREEN, self.kidPosition)
            
            self.time = int((pygame.time.get_ticks()))
            #See Hitbox
            #pygame.draw.rect(SCREEN,(255,255,255),self.kid.hitbox, 1)
            pygame.display.update()
        points = int(self.kid.points - self.time/1000)
        f = open("leaderboard.txt", "a")
        print(f)
        f.write(self.playerName+"-"+str(points))
        f.close()
        self.menu.victory(SCREEN, self.kid.points, self.playerName)
        # self.menu.game_over(SCREEN, points)