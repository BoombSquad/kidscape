import pygame
from models.demon import Demon
from models.key import Key
from models.obstacle import Obstacle  

class LevelThree():
    def __init__(self):
        self.levelX = 20
        self.levelY = 120
        self.fase = 2
        self.speed = 0.2
        self.obstacles = []
        self.remainingKeys = []
        self.openedDoor = False
        self.door = None
        self.demon = None

    def createObstacles(self, screen):
        self.demon = Demon((600, 300), (1000,1000))
        self.background = pygame.image.load("assets/images/backgrounds/level-three-with-obstacles.jpg")

        self.obstacles.append(Obstacle((137,0), pygame.image.load("assets/images/obstacles/vertical-wall.png")))
        self.obstacles.append(Obstacle((137,275), pygame.image.load("assets/images/obstacles/vertical-wall.png")))
        self.obstacles.append(Obstacle((496,156), pygame.image.load("assets/images/obstacles/vertical-wall.png")))
        self.obstacles.append(Obstacle((871,156), pygame.image.load("assets/images/obstacles/vertical-wall.png")))
        self.obstacles.append(Obstacle((1107,0), pygame.image.load("assets/images/obstacles/vertical-wall.png")))
        self.obstacles.append(Obstacle((1107,276), pygame.image.load("assets/images/obstacles/vertical-wall.png")))
        
        self.obstacles.append(Obstacle((153,276), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((377,276), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((137,552), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((257,552), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((377,552), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((497,552), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((497,433), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((617,433), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((631,156), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((751,156), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((887,275), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((871,433), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((767,552), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((887,552), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))
        self.obstacles.append(Obstacle((1003,552), pygame.image.load("assets/images/obstacles/horizontal-wall.png")))

        self.obstacles.append(Obstacle((159,11), pygame.image.load("assets/images/obstacles/plant.png")))
        self.obstacles.append(Obstacle((827,170), pygame.image.load("assets/images/obstacles/plant.png")))
        self.obstacles.append(Obstacle((890,294), pygame.image.load("assets/images/obstacles/plant.png")))
        self.obstacles.append(Obstacle((1065,11), pygame.image.load("assets/images/obstacles/plant.png")))

        self.obstacles.append(Obstacle((159,236), pygame.image.load("assets/images/obstacles/skull.png")))
        self.obstacles.append(Obstacle((519,394), pygame.image.load("assets/images/obstacles/skull.png")))
        self.obstacles.append(Obstacle((835,84), pygame.image.load("assets/images/obstacles/skull.png")))

        self.obstacles.append(Obstacle((1264,84), pygame.image.load("assets/images/obstacles/door-closed.png")))

        key1 = Key((153, 512))
        key2 = Key((435, 236))
        key3 = Key((557, 394)) 
        key4 = Key((892, 236))

        self.obstacles.append(key1)
        self.obstacles.append(key2)
        self.obstacles.append(key3)
        self.obstacles.append(key4)
        
        # self.remainingKeys.append(key1)
        # self.remainingKeys.append(key2)
        # self.remainingKeys.append(key3)
        # self.remainingKeys.append(key4)

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
        return 0