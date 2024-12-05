from pygame import *
wn = display.set_mode((700,500))
display.set_caption("Назва гри")

fon = transform.scale( image.load("фондля гр 1.jpg"),(700,500))
fon1 = transform.scale( image.load("фон2.jpg"),(700,500))
class Player(sprite.Sprite):
    def __init__(self,x,y,image_p,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(image_p),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        wn.blit(self.image,(self.rect.x,self.rect.y))
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y>0:
            self.rect.y -= 5
        if keys[K_s] and self.rect.y<400:
            self.rect.y += 5
        if keys[K_d] and self.rect.x<600:
            self.rect.x += 5
        if keys[K_a] and self.rect.x>0:
            self.rect.x -= 5


fps = 60
clock = time.Clock()
x = 100
y = 350
lvl1 = 1
lvl2 = 0
player = Player(100,350,"гравець1.png",100,100)
door = Player(600,300,"двері.webp",200,300)

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
    if lvl1:
        wn.blit(fon,(0,0))
        door.draw()
    if lvl2:
        wn.blit(fon1,(0,0))

    player.draw()
    player.update()

    if sprite.collide_rect(player,door):
        lvl1 = 0
        lvl2 = 1
        player.rect.x = 100
        player.rect.y = 350
    display.update()
    clock.tick(fps)
