import pygame
from models.demon import Demon
from models.key import Key
from models.obstacle import Obstacle

class LevelTwo():
    def __init__(self):
        self.initialKidPosition = [80,400]
        self.fase = 2
        self.background = pygame.image.load("assets/images/backgrounds/level-two-background.jpg")
        self.speed = 0.2
        self.obstacles = []
        self.remainingKeys = []
        self.openedDoor = False
        self.door = None
        self.demon = Demon((1000, 300))

    def createObstacles(self, screen):

        self.door = Obstacle((1265,443), pygame.image.load("assets/images/obstacles/door-closed.png"))

        key2 = Key((1200, 400))
        self.remainingKeys.append(key2)

        self.obstacles.append(self.door)
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