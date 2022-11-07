import pygame
from models.key import Key
from models.obstacle import Obstacle

class LevelTwo():
    def __init__(self):
        self.background = pygame.image.load("assets/images/backgrounds/level-one-background.jpg")
        self.speed = 0.5
        self.obstacles = []
        self.remainingKeys = []
        self.openedDoor = False
        self.door = None

    def createObstacles(self, screen):

        key = Key((1221, 229))
        key2 = Key((1200, 400))
        self.remainingKeys.append(key)
        self.remainingKeys.append(key2)
        self.obstacles.append(key)
        self.obstacles.append(key2)
        
        for obstacle in self.obstacles:
            screen.blit(obstacle.sprite, obstacle.hitbox)

    def update(self, screen):
        screen.blit(self.background, (0,0))
        if self.openedDoor:
            screen.blit(pygame.image.load("assets/images/obstacles/door.png"), (1265,433))

        for key in self.remainingKeys:
            screen.blit(key.sprite, key.hitbox)
        
    def checkDoorCollision(self, position):
        return position[0] >= 1235 and position[1] >= 460 and position[1] <= 500

    def openDoor(self):
        self.openedDoor = True

    def getNextLevel(self):
        return 