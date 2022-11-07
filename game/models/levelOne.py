import pygame
from models.key import Key
from models.levelTwo import LevelTwo
from models.obstacle import Obstacle

class LevelOne():
    def __init__(self):
        self.background = None
        self.speed = 0.5
        self.obstacles = []
        self.remainingKeys = []
        self.openedDoor = False
        self.door = None

    def createObstacles(self, screen):

        bedSprite = pygame.image.load("assets/images/obstacles/bed.png")
        plantSprite = pygame.image.load("assets/images/obstacles/plant.png")
        deskSprite = pygame.image.load("assets/images/obstacles/desk.png")
        wardrobeSpirte = pygame.image.load("assets/images/obstacles/wardrobe.png")
        verticalWallSprite = pygame.image.load("assets/images/obstacles/vertical-wall.png")
        horizontalWallSprite = pygame.image.load("assets/images/obstacles/horizontal-wall.png")
        firePlaceSprite = pygame.image.load("assets/images/obstacles/fireplace.png")
        leftChairSprite = pygame.image.load("assets/images/obstacles/leftChair.png")
        rightChairSprite = pygame.image.load("assets/images/obstacles/rightChair.png")
        couchSprite = pygame.image.load("assets/images/obstacles/couch.png")
        sinkSprite = pygame.image.load("assets/images/obstacles/sink.png")
        glassesSprite = pygame.image.load("assets/images/obstacles/glasses.png")
        winesSprite = pygame.image.load("assets/images/obstacles/wines.png")
        tableSprite = pygame.image.load("assets/images/obstacles/table.png")
        doorSprite = pygame.image.load("assets/images/obstacles/door-closed.png")

        self.background = pygame.image.load("assets/images/backgrounds/level-one-with-obstacles.jpg")

        bedroomBed = Obstacle((158,121), bedSprite)
        bedroomLeftPlant = Obstacle((18, 9), plantSprite)
        bedroomRightPlant = Obstacle((287, 10), plantSprite)
        bedroomDesk = Obstacle((263,110), deskSprite)
        bedroomWardrobe = Obstacle((18,103), wardrobeSpirte)
        bedroomRightWall = Obstacle((331,0), verticalWallSprite)
        bedroomBottomLeftWall = Obstacle((16,264), horizontalWallSprite)
        bedroomBottomRightWall = Obstacle((227,264), horizontalWallSprite)
        roomFireplace = Obstacle((555,9), firePlaceSprite)
        roomLeftChair = Obstacle((528,169), leftChairSprite)
        roomRightChair = Obstacle((709,170), rightChairSprite)
        roomCouch = Obstacle((593,237), couchSprite)
        roomLeftPlant = Obstacle((357,11), plantSprite)
        roomRightPlant = Obstacle((889,11), plantSprite)
        kitchenLeftWall = Obstacle((938,0), verticalWallSprite)
        kitchenBottomLeftWall = Obstacle((938,272), horizontalWallSprite)
        kitchenBottomRightWall = Obstacle((1145,272), horizontalWallSprite)
        kitchenTable = Obstacle((1043,151), tableSprite)
        kitchenSink = Obstacle((1017,62), sinkSprite)
        kitchenWines = Obstacle((962,24), winesSprite)
        kitchenGlasses = Obstacle((1165,24), glassesSprite)
        self.door = Obstacle((1265,443), doorSprite)
        

        self.obstacles.append(bedroomBed)
        self.obstacles.append(bedroomLeftPlant)
        self.obstacles.append(bedroomRightPlant)
        self.obstacles.append(bedroomDesk)
        self.obstacles.append(bedroomWardrobe)
        self.obstacles.append(bedroomRightWall)
        self.obstacles.append(bedroomBottomLeftWall)
        self.obstacles.append(bedroomBottomRightWall)
        self.obstacles.append(roomFireplace)
        self.obstacles.append(roomLeftChair)
        self.obstacles.append(roomRightChair)
        self.obstacles.append(roomCouch)
        self.obstacles.append(roomLeftPlant)
        self.obstacles.append(roomRightPlant)
        self.obstacles.append(kitchenLeftWall)
        self.obstacles.append(kitchenBottomLeftWall)
        self.obstacles.append(kitchenBottomRightWall)
        self.obstacles.append(kitchenTable)
        self.obstacles.append(kitchenSink)
        self.obstacles.append(kitchenWines)
        self.obstacles.append(kitchenGlasses)
        self.obstacles.append(self.door)
        
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