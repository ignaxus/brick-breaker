#import modules
import pygame
import sys

#import other classes
from ball import Ball
from paddle import Paddle

#class for the game
class Game:
    def __init__(self):
        pygame.init()

        self.width = 800
        self.height = 600

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Brick Breaker")

        self.clock = pygame.time.Clock()

        #add all other classes
        self.ball = Ball(self)
        self.paddle = Paddle(self)

    #enable user to quit   
    def check_event(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     sys.exit()
    
    #update the position of all elements
    def update_position(self):
        self.paddle.move()
        self.ball.move(self.paddle)
    
    #update all element in the screen
    def update_screen(self):
        self.screen.fill(self.WHITE)
        self.ball.draw()
        self.paddle.draw()
        pygame.display.update()
        self.clock.tick(60)
    
    #main loop of the game
    def run(self):
        while True:
            self.check_event()
            self.update_position()
            self.update_screen()

#start running the game
if __name__ == "__main__":
     game=Game()
     game.run()