import pygame
from models.levelThree import LevelThree
from models.demon import Demon
from models.key import Key
from models.obstacle import Obstacle

class LevelTwo():
    def __init__(self):
        self.levelX = 80
        self.levelY = 400
        self.fase = 2
        self.background = pygame.image.load("assets/images/backgrounds/level-two-background.jpg")
        self.speed = 0.2
        self.obstacles = []
        self.remainingKeys = []
        self.openedDoor = False
        self.door = None

    def createObstacles(self, screen):
        self.demon = Demon((1000, 300), (400,400))
        self.background = pygame.image.load("assets/images/backgrounds/level-two-with-obstacles.jpg")

        self.obstacles.append(Obstacle((628,0), pygame.image.load("assets/images/obstacles/vertical-wall.png")))
        self.obstacles.append(Obstacle((960,0), pygame.image.load("assets/images/obstacles/vertical-wall.png")))
        self.obstacles.append(Obstacle((347,403), pygame.image.load("assets/images/obstacles/vertical-wall.png")))
        self.obstacles.append(Obstacle((960,403), pygame.image.load("assets/images/obstacles/vertical-wall.png")))
        
        self.obstacles.append(Obstacle((628,276), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((856,276), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((362,403), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((482,403), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((721,403), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((841,403), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))

        self.obstacles.append(Obstacle((648,11), pygame.image.load("assets/images/obstacles/plant.png")))
        self.obstacles.append(Obstacle((913,11), pygame.image.load("assets/images/obstacles/plant.png")))
        self.obstacles.append(Obstacle((367,423), pygame.image.load("assets/images/obstacles/plant.png")))
        self.obstacles.append(Obstacle((913,423), pygame.image.load("assets/images/obstacles/plant.png")))

        self.obstacles.append(Obstacle((715,17), pygame.image.load("assets/images/obstacles/fireplace.png")))

        self.obstacles.append(Obstacle((750,162), pygame.image.load("assets/images/obstacles/table.png")))

        self.obstacles.append(Obstacle((648,238), pygame.image.load("assets/images/obstacles/skull.png")))
        self.obstacles.append(Obstacle((371,541), pygame.image.load("assets/images/obstacles/skull.png")))
        self.obstacles.append(Obstacle((964,632), pygame.image.load("assets/images/obstacles/skull.png")))

        self.obstacles.append(Obstacle((1264,84), pygame.image.load("assets/images/obstacles/door-closed.png")))

        key1 = Key((373, 631))
        key2 = Key((916, 108))
        key3 = Key((1218, 631))

        self.obstacles.append(key1)
        self.obstacles.append(key2)
        self.obstacles.append(key3)
        
        self.remainingKeys.append(key1)
        self.remainingKeys.append(key2)
        self.remainingKeys.append(key3)

        for obstacle in self.obstacles:
            screen.blit(obstacle.sprite, obstacle.hitbox)

    def update(self, screen):
        screen.blit(self.background, (0,0))
        if self.openedDoor:
            screen.blit(pygame.image.load("assets/images/obstacles/door.png"), (1264,84))

        for key in self.remainingKeys:
            screen.blit(key.sprite, key.hitbox)
        
    def checkDoorCollision(self, position):
        return position[0] >= 1235 and position[1] >= 84 and position[1] <= 178

    def openDoor(self):
        self.openedDoor = True

    def getNextLevel(self):
        return LevelThree()