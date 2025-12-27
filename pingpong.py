from pygame import *
from time import time as timer
from random import randint
init()

window = display.set_mode((700, 500))
window.fill((200, 255, 255))
display.set_caption('Space shooter')
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_d] and self.rect.y < 400:
            self.rect.y += self.speed

platform = player('racket.png', 5, 200, 30, 100, 5)
platform2 = player('racket.png', 665, 250, 30, 100, 5)
ball = GameSprite('tenis_ball.png', 350, 250, 35, 35, 3)

game = True
finish = False
x = 5
y = 5
font = font.Font(None, 70)
win1 = font.render('Player 1 win!', True, (0, 200, 0))
win2 = font.render('Player 2 win!', True, (0, 200, 0))

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        window.fill((200, 255, 255))
        ball.rect.x += x
        ball.rect.y += y
        if ball.rect.y >= 475 or ball.rect.y <= 25:
            y *= -1
        if sprite.collide_rect(platform, ball) or sprite.collide_rect(platform2, ball):
            x *= -1
        if ball.rect.x > 690:
            window.blit(win1, (200, 220))
        if ball.rect.x < 10:
            window.blit(win2, (200, 220))
        platform.update()
        platform2.update2()
        platform.reset()
        platform2.reset()
        ball.reset()
    display.update()
    clock.tick(60)

    