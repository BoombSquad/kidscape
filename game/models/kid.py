import pygame

class Kid():
    def __init__(self, position):
        self.lives = 3
        self.position_X = position[0]
        self.position_Y = position[1]
        self.sprite = pygame.image.load("assets/kid-sprite-front.png")
        
        
        self.walkLeftSprites = []
        self.walkLeftSprites.append(pygame.image.load("assets/kid-sprite-left.png"))
        self.walkLeftSprites.append(pygame.image.load("assets/kid-sprite-left-2.png"))
        self.walkLeftSprites.append(pygame.image.load("assets/kid-sprite-left-3.png"))
        self.walkLeftSprites.append(pygame.image.load("assets/kid-sprite-left-4.png"))
        self.walkLeftSprites.append(pygame.image.load("assets/kid-sprite-left-5.png"))
        self.walkLeftSprites.append(pygame.image.load("assets/kid-sprite-left-6.png"))
        self.walkLeftSprites.append(pygame.image.load("assets/kid-sprite-left-7.png"))
        self.walkLeftSprites.append(pygame.image.load("assets/kid-sprite-left-8.png"))
        self.walkLeftSprites.append(pygame.image.load("assets/kid-sprite-left-9.png"))
        self.walkLeftState = 0
    
        self.walkRightSprites = []
        self.walkRightSprites.append(pygame.image.load("assets/kid-sprite-right.png"))
        self.walkRightSprites.append(pygame.image.load("assets/kid-sprite-right-2.png"))
        self.walkRightSprites.append(pygame.image.load("assets/kid-sprite-right-3.png"))
        self.walkRightSprites.append(pygame.image.load("assets/kid-sprite-right-4.png"))
        self.walkRightSprites.append(pygame.image.load("assets/kid-sprite-right-5.png"))
        self.walkRightSprites.append(pygame.image.load("assets/kid-sprite-right-6.png"))
        self.walkRightSprites.append(pygame.image.load("assets/kid-sprite-right-7.png"))
        self.walkRightSprites.append(pygame.image.load("assets/kid-sprite-right-8.png"))
        self.walkRightSprites.append(pygame.image.load("assets/kid-sprite-right-9.png"))
        self.walkRightState = 0
        
        
        self.rect = self.sprite.get_rect(center = (self.position_X, self.position_Y))
    

    def isAlive(self):
        if self.lives <= 0:
            return False
        else:
            return True
    
    def update(self, screen, position):
        self.position_X = position[0]
        self.position_Y = position[1]
        self.rect = self.sprite.get_rect(center = (self.position_X, self.position_Y))
        screen.blit(self.sprite, self.rect)
    
    
    def setSpriteDirection(self, direction):
        if direction == "UP":
            self.sprite = pygame.image.load("assets/kid-sprite-back.png")
        if direction == "DOWN":
            self.sprite = pygame.image.load("assets/kid-sprite-front.png")
        if direction == "RIGHT":
            if self.walkRightState >= len(self.walkRightSprites):
                self.walkRightState = 0
            self.sprite = self.walkRightSprites[int(self.walkRightState)]
            self.walkRightState += 0.015
        if direction == "LEFT":
            if self.walkLeftState >= len(self.walkLeftSprites):
                self.walkLeftState = 0
            self.sprite = self.walkLeftSprites[int(self.walkLeftState)]
            self.walkLeftState += 0.015