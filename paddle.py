import pygame

class Paddle:
    def __init__(self, game):
        self.screen = game.screen

        #set the size and color of the paddle
        self.width = 80
        self.height = 8
        self.color = game.BLACK

        #original position
        self.x = 360
        self.y = 570

        #set speed
        self.speed = 8

    #control the movement of paddle when keys are pressed
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.x += self.speed

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

