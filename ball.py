import pygame

#class for the ball
class Ball:
    def __init__(self, game):
        self.screen = game.screen

          #initial position
        self.x = 400
        self.y = 500
        
        #set radius and color
        self.radius = 15
        self.color = game.BLACK

        #set speed
        self.speed_x = 4
        self.speed_y = -4

    #movement of the ball, including collisions
    def move(self, paddle, bricks):
        self.x += self.speed_x
        self.y += self.speed_y

        self.wall_collision()
        self.paddle_collision(paddle)
        self.brick_collision(bricks)

    def wall_collision(self):
        # Left wall
        if self.x - self.radius <= 0:
            self.speed_x *= -1

        # Right wall
        if self.x + self.radius >= 800:
            self.speed_x *= -1

        # Top wall
        if self.y - self.radius <= 0:
            self.speed_y *= -1

    def paddle_collision(self, paddle):
        if (
            self.y + self.radius >= paddle.y
            and self.y - self.radius <= paddle.y + paddle.height
            and self.x + self.radius >= paddle.x
            and self.x - self.radius <= paddle.x + paddle.width
            and self.speed_y > 0
        ):
            self.speed_y *= -1

    def brick_collision(self, bricks):
        for brick in bricks[:]:

            if (
                self.x + self.radius >= brick.x
                and self.x - self.radius <= brick.x + brick.width
                and self.y + self.radius >= brick.y
                and self.y - self.radius <= brick.y + brick.height
            ):

                brick_center_x = brick.x + brick.width / 2
                brick_center_y = brick.y + brick.height / 2

                dx = self.x - brick_center_x
                dy = self.y - brick_center_y

                if abs(dx) > abs(dy):
                    self.speed_x *= -1
                else:
                    self.speed_y *= -1

                bricks.remove(brick)
                break
    
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)