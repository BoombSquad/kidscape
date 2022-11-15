import pygame

from models.key import Key


class Demon():

  def __init__(self, position):
    self.position_X = position[0]
    self.position_Y = position[1]
    self.sprite = pygame.image.load("assets/images/demon/demon-sprite-front.png")
    self.stateSpeed = 0.015
    self.acc = 0.1
    self.chasing = False
    self.stepsWalked = 0
    self.direction = "LEFT"
    self.walkLeftSprites = []
    # self.walkLeftSprites.append(pygame.image.load("assets/images/kid/kid-sprite-left-9.png"))
    self.walkLeftState = 0

    self.walkRightSprites = []
    # self.walkRightSprites.append(pygame.image.load("assets/images/kid/kid-sprite-right-9.png"))
    self.walkRightState = 0

    self.walkUpSprites = []
    # self.walkUpSprites.append(pygame.image.load("assets/images/kid/kid-sprite-back-9.png"))
    self.walkUpState = 0
    
    self.walkDownSprites = []
    # self.walkDownSprites.append(pygame.image.load("assets/images/kid/kid-sprite-front-9.png"))
    self.walkDownState = 0


    self.hitbox = pygame.Rect(self.position_X, self.position_Y, 50, 60)
    self.chasingBox = pygame.Rect(self.position_X, self.position_Y, 150, 150)
   
 
  def update(self, screen, position):
    self.position_X = position[0]
    self.position_Y = position[1]
    
    coordinates = (self.hitbox.topleft[0]+5, self.hitbox.topleft[1])
    self.hitbox = pygame.Rect(self.position_X, self.position_Y, 50, 60)

    self.chasingBox = pygame.Rect(self.position_X-70, self.position_Y-60, 200, 200)
    pygame.draw.rect(screen, (255,0,0), self.chasingBox, 1)
    
    screen.blit(self.sprite, coordinates)

  def checkCollision(self, level):
      for obstacle in level.obstacles:
          if self.hitbox.colliderect(obstacle.hitbox):
            if type(obstacle) == Key:
                return False
      return False
  
  def isChasing(self, game):
    if game.kid.hitbox.colliderect(self.chasingBox):
      return True
    return False

  def setSpriteDirection(self, direction):
      self.direction = direction
      pass
    #   if direction == "UP":
    #       if self.walkUpState >= len(self.walkUpSprites):
    #           self.walkUpState = 0
    #       self.sprite = self.walkUpSprites[int(self.walkUpState)]
    #       self.walkUpState += self.stateSpeed
    #   if direction == "DOWN":
    #       if self.walkDownState >= len(self.walkDownSprites):
    #           self.walkDownState = 0
    #       self.sprite = self.walkDownSprites[int(self.walkDownState)]
    #       self.walkDownState += self.stateSpeed
    #   if direction == "RIGHT":
    #       if self.walkRightState >= len(self.walkRightSprites):
    #           self.walkRightState = 0
    #       self.sprite = self.walkRightSprites[int(self.walkRightState)]
    #       self.walkRightState += self.stateSpeed
    #   if direction == "LEFT":
    #       if self.walkLeftState >= len(self.walkLeftSprites):
    #           self.walkLeftState = 0
    #       self.sprite = self.walkLeftSprites[int(self.walkLeftState)]
    #       self.walkLeftState += self.stateSpeed