from pygame import *
from random import *


window = display.set_mode((700, 500))
display.set_caption('بؤقفىوتن غتع')



background = transform.scale(image.load('stol.jpg'), (700, 500))




class GameSprite(sprite.Sprite):
    def __init__(self, pl_image, pl_x, pl_y, pl_speed, gs_x, gs_y):
        super().__init__()
        self.image = transform.scale(image.load(pl_image), (gs_x, gs_y))
        self.speed = pl_speed
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))




class Player(GameSprite):
    def __init__(self, pl_image, pl_x, pl_y, pl_speed, gs_x, gs_y):
        super().__init__(pl_image, pl_x, pl_y, pl_speed, gs_x, gs_y)
    
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.x -= self.speed
        if key_pressed[K_s] and self.rect.y < 620:
            self.rect.x += self.speed

    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.x -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 620:
            self.rect.x += self.speed



pl1 = Player('palka.png', 50, 395, 3, 60, 90)
pl2 = Player('palka.png', 450, 395, 3, 60, 90)

shar = GameSprite('shar.png', 100, 50, 2, 50, 50)


b = 0


while b < 5:

    

    pl1.update_l()
    pl1.reset()
    pl2.update_r()
    pl1.reset()

    shar.update()
    shar.reset()




    display.update()