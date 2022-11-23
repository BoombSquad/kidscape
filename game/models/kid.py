import pygame

from models.key import Key
from models.levelTwo import LevelTwo

class Kid():
    def __init__(self, position):
        self.lives = 3
        self.position_X = position[0]
        self.position_Y = position[1]
        self.sprite = pygame.image.load("assets/images/kid/kid-sprite-front.png")
        
        self.walkLeftSprites = []
        self.walkLeftSprites.append(pygame.image.load("assets/images/kid/kid-sprite-left.png"))
        self.walkLeftSprites.append(pygame.image.load("assets/images/kid/kid-sprite-left-2.png"))
        self.walkLeftSprites.append(pygame.image.load("assets/images/kid/kid-sprite-left-3.png"))
        self.walkLeftSprites.append(pygame.image.load("assets/images/kid/kid-sprite-left-4.png"))
        self.walkLeftSprites.append(pygame.image.load("assets/images/kid/kid-sprite-left-5.png"))
        self.walkLeftSprites.append(pygame.image.load("assets/images/kid/kid-sprite-left-6.png"))
        self.walkLeftSprites.append(pygame.image.load("assets/images/kid/kid-sprite-left-7.png"))
        self.walkLeftSprites.append(pygame.image.load("assets/images/kid/kid-sprite-left-8.png"))
        self.walkLeftSprites.append(pygame.image.load("assets/images/kid/kid-sprite-left-9.png"))
        self.walkLeftState = 0
    
        self.walkRightSprites = []
        self.walkRightSprites.append(pygame.image.load("assets/images/kid/kid-sprite-right.png"))
        self.walkRightSprites.append(pygame.image.load("assets/images/kid/kid-sprite-right-2.png"))
        self.walkRightSprites.append(pygame.image.load("assets/images/kid/kid-sprite-right-3.png"))
        self.walkRightSprites.append(pygame.image.load("assets/images/kid/kid-sprite-right-4.png"))
        self.walkRightSprites.append(pygame.image.load("assets/images/kid/kid-sprite-right-5.png"))
        self.walkRightSprites.append(pygame.image.load("assets/images/kid/kid-sprite-right-6.png"))
        self.walkRightSprites.append(pygame.image.load("assets/images/kid/kid-sprite-right-7.png"))
        self.walkRightSprites.append(pygame.image.load("assets/images/kid/kid-sprite-right-8.png"))
        self.walkRightSprites.append(pygame.image.load("assets/images/kid/kid-sprite-right-9.png"))
        self.walkRightState = 0

        self.walkUpSprites = []
        self.walkUpSprites.append(pygame.image.load("assets/images/kid/kid-sprite-back.png"))
        self.walkUpSprites.append(pygame.image.load("assets/images/kid/kid-sprite-back-2.png"))
        self.walkUpSprites.append(pygame.image.load("assets/images/kid/kid-sprite-back-3.png"))
        self.walkUpSprites.append(pygame.image.load("assets/images/kid/kid-sprite-back-4.png"))
        self.walkUpSprites.append(pygame.image.load("assets/images/kid/kid-sprite-back-5.png"))
        self.walkUpSprites.append(pygame.image.load("assets/images/kid/kid-sprite-back-6.png"))
        self.walkUpSprites.append(pygame.image.load("assets/images/kid/kid-sprite-back-7.png"))
        self.walkUpSprites.append(pygame.image.load("assets/images/kid/kid-sprite-back-8.png"))
        self.walkUpSprites.append(pygame.image.load("assets/images/kid/kid-sprite-back-9.png"))
        self.walkUpState = 0
        
        self.walkDownSprites = []
        self.walkDownSprites.append(pygame.image.load("assets/images/kid/kid-sprite-front.png"))
        self.walkDownSprites.append(pygame.image.load("assets/images/kid/kid-sprite-front-2.png"))
        self.walkDownSprites.append(pygame.image.load("assets/images/kid/kid-sprite-front-3.png"))
        self.walkDownSprites.append(pygame.image.load("assets/images/kid/kid-sprite-front-4.png"))
        self.walkDownSprites.append(pygame.image.load("assets/images/kid/kid-sprite-front-5.png"))
        self.walkDownSprites.append(pygame.image.load("assets/images/kid/kid-sprite-front-6.png"))
        self.walkDownSprites.append(pygame.image.load("assets/images/kid/kid-sprite-front-7.png"))
        self.walkDownSprites.append(pygame.image.load("assets/images/kid/kid-sprite-front-8.png"))
        self.walkDownSprites.append(pygame.image.load("assets/images/kid/kid-sprite-front-9.png"))
        self.walkDownState = 0
        
        self.stateSpeed = 0.015

        self.hitbox = pygame.Rect(self.position_X, self.position_Y, 30, 30)

        self.points = 0

    

    def isAlive(self):
        if self.lives == 0:
            return False
        else:
            return True
    
    def update(self, screen, position):
        self.position_X = position[0]
        self.position_Y = position[1]
        self.hitbox = pygame.Rect(self.position_X, self.position_Y, 30, 30)
        coordinates = (self.hitbox.topleft[0], self.hitbox.topleft[1] - 24)
        screen.blit(self.sprite, coordinates)

    def checkCollision(self, level):
        for obstacle in level.obstacles:
            if self.hitbox.colliderect(obstacle.hitbox):
                if type(obstacle) == Key and level.remainingKeys.__len__() > 0:
                    level.obstacles.remove(obstacle)
                    level.remainingKeys.remove(obstacle)
                    self.points += 2500
                return True
            if level.fase != 1 and self.hitbox.colliderect(level.demon.hitbox):
                return True
        return False

    def isDemonCollision(self, level):
        if level.fase == 1:
            return False
        elif self.hitbox.colliderect(level.demon.hitbox):
            return True
            
    def setSpriteDirection(self, direction):
        if direction == "UP":
            if self.walkUpState >= len(self.walkUpSprites):
                self.walkUpState = 0
            self.sprite = self.walkUpSprites[int(self.walkUpState)]
            self.walkUpState += self.stateSpeed
        if direction == "DOWN":
            if self.walkDownState >= len(self.walkDownSprites):
                self.walkDownState = 0
            self.sprite = self.walkDownSprites[int(self.walkDownState)]
            self.walkDownState += self.stateSpeed
        if direction == "RIGHT":
            if self.walkRightState >= len(self.walkRightSprites):
                self.walkRightState = 0
            self.sprite = self.walkRightSprites[int(self.walkRightState)]
            self.walkRightState += self.stateSpeed
        if direction == "LEFT":
            if self.walkLeftState >= len(self.walkLeftSprites):
                self.walkLeftState = 0
            self.sprite = self.walkLeftSprites[int(self.walkLeftState)]
            self.walkLeftState += self.stateSpeed