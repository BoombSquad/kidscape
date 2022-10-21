import pygame

class Obstacle():
    def __init__(self, position, sprite):
        self.position_X = position[0]
        self.position_Y = position[1]
        self.sprite = sprite
        self.hitbox = self.sprite.get_rect(topleft = (self.position_X, self.position_Y))

    def update(self, screen):
        screen.blit(self.sprite, self.hitbox)