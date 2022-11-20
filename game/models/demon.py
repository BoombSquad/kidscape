import pygame

from models.key import Key


class Demon():

  def __init__(self, position, chaseBox):
    self.position_X = position[0]
    self.position_Y = position[1]
    self.sprite = pygame.image.load("assets/images/demon/ghost-front.png")
    self.stateSpeed = 0.015
    self.acc = 3
    self.chasing = False
    self.stepsWalked = 0
    self.direction = "LEFT"
    self.walkLeftSprites = []
    self.walkLeftSprites.append(pygame.image.load("assets/images/demon/ghost-left.png"))
    self.walkLeftState = 0

    self.walkRightSprites = []
    self.walkRightSprites.append(pygame.image.load("assets/images/demon/ghost-right.png"))
    self.walkRightState = 0

    self.walkUpSprites = []
    self.walkUpSprites.append(pygame.image.load("assets/images/demon/ghost-back.png"))
    self.walkUpState = 0
    
    self.walkDownSprites = []
    self.walkDownSprites.append(pygame.image.load("assets/images/demon/ghost-front.png"))
    self.walkDownSprites.append(pygame.image.load("assets/images/demon/ghost-chase.png"))
    self.walkDownState = 0

    self.hitbox = self.sprite.get_rect(topleft = (self.position_X, self.position_Y))
    #self.hitbox = pygame.Rect(self.position_X, self.position_Y, 30, 44)
    self.chasingBox = pygame.Rect(self.position_X, self.position_Y, 150, 150)
    self.chasignBoxSize = chaseBox
   

  def update(self, screen, position):
    self.position_X = position[0]
    self.position_Y = position[1]
    
    coordinates = (self.hitbox.topleft[0], self.hitbox.topleft[1])
    self.hitbox = pygame.Rect(self.position_X, self.position_Y, 38, 44)

    self.chasingBox = pygame.Rect(self.position_X, self.position_Y, self.chasignBoxSize[0], self.chasignBoxSize[1])
    self.chasingBox.center = self.hitbox.center
    #pygame.draw.rect(screen, (255,0,0), self.chasingBox, 1)
    
    screen.blit(self.sprite, coordinates)

  def checkCollision(self, level):
      for obstacle in level.obstacles:
          if self.hitbox.colliderect(obstacle.hitbox):
            if type(obstacle) == Key:
                return False
            else:
              return True
      return False
  
  def isChasing(self, game):
    if game.kid.hitbox.colliderect(self.chasingBox):
      self.setSpriteDirection("CHASE")
      return True
    elif self.direction == "CHASE":
      self.setSpriteDirection("LEFT")
    return False

  def setSpriteDirection(self, direction):
      self.direction = direction
      if direction == "UP":
    #      if self.walkUpState >= len(self.walkUpSprites):
    #           self.walkUpState = 0
            self.sprite = self.walkUpSprites[0]
    #       self.sprite = self.walkUpSprites[int(self.walkUpState)]
    #       self.walkUpState += self.stateSpeed
      if direction == "DOWN":
    #       if self.walkDownState >= len(self.walkDownSprites):
    #           self.walkDownState = 0
            self.sprite = self.walkDownSprites[0]
    #       self.sprite = self.walkDownSprites[int(self.walkDownState)]
    #       self.walkDownState += self.stateSpeed
      if direction == "RIGHT":
    #       if self.walkRightState >= len(self.walkRightSprites):
    #           self.walkRightState = 0
            self.sprite = self.walkRightSprites[0]
    #       self.sprite = self.walkRightSprites[int(self.walkRightState)]
    #       self.walkRightState += self.stateSpeed
      if direction == "LEFT":
    #       if self.walkLeftState >= len(self.walkLeftSprites):
    #           self.walkLeftState = 0
            self.sprite = self.walkLeftSprites[0]
    #       self.sprite = self.walkLeftSprites[int(self.walkLeftState)]
    #       self.walkLeftState += self.stateSpeed
      if direction == "CHASE":
            self.sprite = self.walkDownSprites[1]
            