import pygame

class Obstacle():
    def __init__(self, position, spritePath):
        self.position_X = position[0]
        self.position_Y = position[1]
        self.sprite = pygame.image.load(spritePath)
        self.hitbox = self.sprite.get_rect(center = (self.position_X, self.position_Y))

    def update(self, screen):
        screen.blit(self.sprite, self.hitbox)