import pygame
from models.obstacle import Obstacle

class Level():
    def __init__(self, level):
        self.level = level
        self.background = None
        self.speed = 0.4
        self.obstacles = []

    def update(self, screen):
        screen.blit(self.background, (0,0))

    def createObstacles(self):
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
        
        if self.level == 1:
            self.background = pygame.image.load("assets/images/backgrounds/level-one-background.jpg")


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
    
    def update(self, screen):
        screen.blit(self.background, (0,0))
        for obstacle in self.obstacles:
            screen.blit(obstacle.sprite, obstacle.hitbox)