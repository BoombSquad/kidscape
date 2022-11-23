import pygame
from models.key import Key
from models.levelTwo import LevelTwo
from models.obstacle import Obstacle

class LevelOne():
    def __init__(self):
        self.fase = 1
        self.levelX = 80  
        self.levelY= 130
        self.background = None
        self.speed = 0.2
        self.obstacles = []
        self.remainingKeys = []
        self.openedDoor = False
        self.door = None

    def createObstacles(self, screen):

        self.background = pygame.image.load("assets/images/backgrounds/level-one-with-obstacles.jpg")
        self.obstacles.append(Obstacle((1265,443), pygame.image.load("assets/images/obstacles/door-closed.png")))
        self.obstacles.append(Obstacle((1165,24), pygame.image.load("assets/images/obstacles/glasses.png")))
        self.obstacles.append(Obstacle((962,24), pygame.image.load("assets/images/obstacles/wines.png")))
        self.obstacles.append(Obstacle((1017,62), pygame.image.load("assets/images/obstacles/sink.png")))
        self.obstacles.append(Obstacle((1043,151), pygame.image.load("assets/images/obstacles/table.png")))
        self.obstacles.append(Obstacle((593,237), pygame.image.load("assets/images/obstacles/couch.png")))
        self.obstacles.append(Obstacle((709,170), pygame.image.load("assets/images/obstacles/rightChair.png")))
        self.obstacles.append(Obstacle((528,169), pygame.image.load("assets/images/obstacles/leftChair.png")))
        self.obstacles.append(Obstacle((555,9), pygame.image.load("assets/images/obstacles/fireplace.png")))
        self.obstacles.append(Obstacle((1145,272), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((938,272), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((227,264), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((16,264), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((938,0),  pygame.image.load("assets/images/obstacles/vertical-wall.png")))
        self.obstacles.append(Obstacle((331,0), pygame.image.load("assets/images/obstacles/vertical-wall.png")))
        self.obstacles.append(Obstacle((18,103),  pygame.image.load("assets/images/obstacles/wardrobe.png")))
        self.obstacles.append(Obstacle((263,110), pygame.image.load("assets/images/obstacles/desk.png")))
        self.obstacles.append(Obstacle((889,11), pygame.image.load("assets/images/obstacles/plant.png")))
        self.obstacles.append(Obstacle((357,11), pygame.image.load("assets/images/obstacles/plant.png")))
        self.obstacles.append(Obstacle((287, 10), pygame.image.load("assets/images/obstacles/plant.png")))
        self.obstacles.append(Obstacle((18, 9), pygame.image.load("assets/images/obstacles/plant.png")))
        self.obstacles.append(Obstacle((158,121), pygame.image.load("assets/images/obstacles/bed.png")))
        
        key = Key((1221, 229))
        self.remainingKeys.append(key)
        self.obstacles.append(key)
        
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
        return LevelTwo()