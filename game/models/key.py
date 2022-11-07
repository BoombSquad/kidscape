import pygame

class Key():
    def __init__(self, position):
        self.position_X = position[0]
        self.position_Y = position[1]
        self.sprite = pygame.image.load("assets/images/key.png")
        self.hitbox = self.sprite.get_rect(topleft = (self.position_X, self.position_Y))
