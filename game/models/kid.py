import pygame

class Kid():
    def __init__(self, position):
        self.lives = 3
        self.position_X = position[0]
        self.position_Y = position[1]
        self.sprite = pygame.image.load("assets/kid-sprite-front.png")
        self.rect = self.sprite.get_rect(center = (self.position_X, self.position_Y))
        self.state = 1
    
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
            self.sprite = pygame.image.load("assets/kid-sprite-right.png")
        if direction == "LEFT":
            #if self.state == 1:
                self.sprite = pygame.image.load("assets/kid-sprite-left.png")
                #self.state = 2    
            #elif self.state == 2: 
                #self.sprite = pygame.image.load("assets/kid-sprite-right.png")
                #self.state = 1