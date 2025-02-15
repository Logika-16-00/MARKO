from pygame import *
wn = display.set_mode((700,500))
display.set_caption("Лабіринт")

fon = transform.scale( image.load("background.jpg"),(700,500))



mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

font.init()
font1 = font.Font(None,70)
font2 = font.Font(None,20)
win = font1.render('You win',1,(23,250,3))
lose = font1.render('You lose',1,(250,1,9))


money = mixer.Sound("money.ogg")
kick = mixer.Sound("kick.ogg")
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

class Wall(sprite.Sprite):
    def __init__(self,color,x,y,size_x,size_y):
        super().__init__()
        self.color = color
        self.size_x = size_x
        self.size_y = size_y
        self.wall = Surface((self.size_x,self.size_y))
        self.wall.fill(self.color)

        self.rect = self.wall.get_rect()
        self.rect.x = x
        self.rect.y = y

    def wall_draw(self):
        wn.blit(self.wall,(self.rect.x,self.rect.y))

color = (0,4,0)
wall1 = Wall(color,0,0,700,10)
wall2 = Wall(color,0,700-10,700,10)
wall3 = Wall(color,0,0,10,600)
wall4 = Wall(color,700-10,0,10,700)
wall5 = Wall(color,300,120,10,700)
wall6 = Wall(color,430,0,10,300)
wall7 = Wall(color,570,120,10,700)
wall8 = Wall(color,120,0,10,380)
wall9 = Wall(color,10,490,700,10)
wall10 = Wall(color,120,380,70,10)
wall11 = Wall(color,240,120,70,10)
hero = Player(20,50,"hero.png",90,90,5,3)
enemy = Player(400,300,"cyborg.png",90,90,6,0)
gold = Player(590,405,"treasure.png",75,75,0,0)
dx = 3
while True:
    for e in event.get():
        if e.type == QUIT:
            quit()

    enemy.rect.x += dx
    if enemy.rect.x>490 or enemy.rect.x<300:
        dx *= -1
    wn.blit(fon,(0,0))
    hero.draw()
    hero.update()
    enemy.draw()
    gold.draw()
    wall1.wall_draw()
    wall2.wall_draw()
    wall3.wall_draw()
    wall4.wall_draw()
    wall5.wall_draw()
    wall6.wall_draw()
    wall7.wall_draw()
    wall8.wall_draw()
    wall9.wall_draw()
    wall10.wall_draw()
    wall11.wall_draw()
    
    


    if sprite.collide_rect(hero,enemy):
        kick.play()
        wn.blit(lose,(250,225))
        hero.rect.x = 20
        hero.rect.y=50

    walls = [wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11]
    for wall in walls:
        if sprite.collide_rect(wall,hero):  
            wn.blit(lose,(250,225))
            hero.rect.x = 20
            hero.rect.y=50
            
    if sprite.collide_rect(hero,gold):
        money.play()
        wn.blit(win,(250,225))
        
        


  
    display.update()
    clock.tick(fps)
