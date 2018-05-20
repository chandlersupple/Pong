import pygame
import random
import colorsys
from pygame.locals import *

pygame.init()

master = pygame.display.set_mode((1000,500))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)

player_y = 0
bot_y = 0
toss = 1

class Ball:
    def __init__(self):
        global toss
        self.x = 500
        self.y = 250
        self.x_add = (5 * toss)
        self.y_add = -1
        self.dirx = 1
        self.diry = 1
            
    def move(self):
        global ball_y
        global ball_x
        global player_y
        global bot_y
            
        if (self.y <= 10):
            self.diry = self.diry * (-1)
        if (self.y >= 490):
            self.diry = self.diry * (-1)
        if (self.x <= 30 and self.y <= player_y + 100 and self.y >= player_y):
            self.dirx = self.dirx * (-1)
            self.x_add = random.randint(3, 7)
            self.y_add = random.randint(-7, -3)
        if (self.x >= 970 and self.y <= bot_y + 100 and self.y >= bot_y):
            self.dirx = self.dirx * (-1)
            self.x_add = random.randint(3, 7)
            self.y_add = random.randint(-7, -3)
            
        ball_y = self.y
        ball_x = self.x
        self.x = self.x + (self.dirx * self.x_add)
        self.y = self.y + (self.diry * self.y_add)
        ball = pygame.draw.circle(master, white, (self.x, self.y), 10, 0)
        
class Player:
    def __init__(self):
        self.x = 20
        self.y = random.randint(100, 400)
        
    def move_player(self):
        global player_y
        player_y = self.y
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]: self.y = self.y - 2
        if pressed[pygame.K_s]: self.y = self.y + 2
        
        if ((self.y + 100) >= 500):
            self.y = 400
        if (self.y <= 0):
            self.y = 0
            
        paddle = pygame.draw.rect(master, white, (self.x, self.y, 10, 100), 0)
            
class Bot:
    def __init__(self):
        self.x = 970
        self.y = random.randint(100, 400)
        
    def move_bot(self):
        global ball_y
        global bot_y
        bot_y = self.y
        if ((self.y + 50) - ball_y > 1):
            self.y = self.y - 2
        if ((self.y + 50) - ball_y < -1):
            self.y = self.y + 2
            
        if ((self.y + 100) >= 500):
            self.y = 400
        if (self.y <= 0):
            self.y = 0
            
        bot_paddle = pygame.draw.rect(master, white, (self.x, self.y, 10, 100), 0)
        
ball = Ball()
bot = Bot()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    master.fill(black)     
    
    for draw in range (0, 15):
        pygame.draw.rect(master, white, (490, -100 + (80 * draw), 10, 40), 0)
    
    ball.move()
    player.move_player()
    bot.move_bot()
    
    if (ball_x >= 1000):
        ball = Ball()
        toss = -1
    if (ball_x <= 0):
        ball = Ball()
        toss = 1
        
    pygame.display.flip()
    clock.tick(50)
