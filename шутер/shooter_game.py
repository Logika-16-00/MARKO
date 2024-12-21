#Створи власний Шутер!

from pygame import *
from random import randint
wn = display.set_mode((700,500))
display.set_caption("shooter")

fps = 60
fon = transform.scale( image.load("galaxy.jpg"),(700,500))
finish = 0
clock = time.Clock()
mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()

class Player(sprite.Sprite):
    def __init__(self,x,y,image_p,size_x,size_y,speed,life):
        super().__init__()
        self.image = transform.scale(image.load(image_p),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.life = life

    def draw(self):
        wn.blit(self.image,(self.rect.x,self.rect.y))
    def update(self):
        keys = key.get_pressed()
        if keys[K_d] and self.rect.x<600:
            self.rect.x += 5
        if keys[K_a] and self.rect.x>0:
            self.rect.x -= 5
class Enemy(Player):
    def update(self):

        self.rect.y = self.speed
        if self.rect.y>500:
            self.rect.y = -10
game = 1
rocket = Player(310,360,"rocket.png",60,120,5,5)
monsters = sprite.Group()
for i in range(5):
    enemy = Enemy(randint(0,650),0,'ufo.png',65,60,randint(1,5),0)
    monsters.add(enemy)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = 0

    if not finish:
        wn.blit(fon,(0,0))
        rocket.draw()
        rocket.update()
        monsters.draw(wn)
    display.update()
    clock.tick(fps)
    
