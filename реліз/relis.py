from pygame import *
from random import *
wn = display.set_mode((500,500))
fon = transform.scale( image.load("background.png"),(500,500))
menu_fom = transform.scale( image.load("menu1.png"),(500,500))
display.set_caption("Змійка")



class Area():
    def __init__(self,x=0,y=0,width=10,height=10,color = None):
        self.rect = Rect(x,y,width,height)
        self.color = color

    def fill(self):
        draw.rect(wn,self.color,self.rect)

    def change_color(self,new_color):
        self.color = new_color

    def outline(self,thinkss,outcolor):
        draw.rect(wn,outcolor,self.rect,thinkss)
    
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
game = 1
finish = 1
x_snake = 300
y_snake = 300
start_game = 0
x_change = 0
y_change = 0 
fps = 10
clock = time.Clock()
mixer.init()
mixer.music.load("snake.ogg")
mixer.music.play()
walls = mixer.Sound("lose.ogg")
appel = mixer.Sound("ukus.ogg")
bubux = mixer.Sound("bomba.ogg")
catch = 1
font.init()
font1 = font.Font(None,30)
font2 = font.Font(None,80)
text_lose = font2.render('You lose!',True,(255,25,2))
ds_width = 500
ds_height = 500
food_x = round(randint(0,400)/10)*10 
food_y = round(randint(0,400)/10)*10

bomb_x = round(randint(0,400)/10)*10 
bomb_y = round(randint(0,400)/10)*10
width, height = 10,10


button_start = Area(150,164,200,75,(4,45,5))
button_start1 = Area(160,174,180,55,(4,245,5))
button_stop = Area(150,260,200,70,(4,45,5))
button_stop1 = Area(160,270,180,50,(4,245,5))
snakepos  = [ [x_snake, y_snake]]
menu = 1
lose_sound = False



lose_game = False
while game:
    wn.fill((0,0,0))
    for e in event.get():
        if e.type == QUIT:
            game = 0
        if e.type ==  KEYDOWN:
            if e.key == K_w:
                start_game = 1
                x_change = 0
                y_change = -10
            if e.key == K_s:
                start_game = 1
                x_change = 0
                y_change = 10
            if e.key == K_d:
                start_game = 1
                x_change = 10
                y_change = 0
            if e.key == K_a:
                start_game = 1
                x_change = -10
                y_change = 0
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
                x,y = e.pos
                if button_stop.collidepoint(x,y):
                     game= 0

                if button_start.collidepoint(x,y):
                     menu = 0
                     finish = 0
    if menu:
        wn.blit(menu_fom,(0,0))
        button_start.fill()
        button_start1.fill()
        button_stop.fill()
        button_stop1.fill()
        
         
    if not finish:
        label_catch = font1.render(f'Рахунок: {catch}',True,(255,255,255))
        wn.blit(fon,(0,0))

        for i in range(0, len(snakepos)):
            draw.rect(wn, (12,240,2), [snakepos[i], (width, height)])
            
        draw.rect(wn,(222,210,2),[bomb_x,bomb_y,10,10])
        draw.rect(wn,(222,10,2),[food_x,food_y,10,10])
        wn.blit(label_catch,(10,10))

        if snakepos[0][0] == food_x and snakepos[0][1]  == food_y:
            food_x = round(randint(0,400)/10)*10 
            food_y = round(randint(0,400)/10)*10
            appel.play()

            catch +=1
            
            snakepos.append(snakepos[-1][:])

        if snakepos[0][0] == bomb_x and snakepos[0][1]  == bomb_y:
            bomb_x = round(randint(0,400)/10)*10 
            bomb_y = round(randint(0,400)/10)*10
            bubux.play()
            catch -=1
            if not snakepos[0][0]:
                print(11111111111111111111111111)
                lose_game = 1

            else:
                print('hukgftryjuknv')
                mixer_music.pause()
                del snakepos[:1]
                if len(snakepos) == 0:
                    lose_game =1

        print(len(snakepos))
        if len(snakepos) != 0:
            if snakepos[0][0] >= ds_width or snakepos[0][1] <=0:
                wn.blit(text_lose,(150,225))
                mixer_music.pause()
                lose_sound = True
                lose_game =1 
                walls.play(1)
                
            if snakepos[0][1] >= ds_height or snakepos[0][1] <=0:
                wn.blit(text_lose,(150,225))
                lose_game =1 
                lose_sound = True
                walls.play()
                mixer_music.pause()

            if snakepos[0][0] >= ds_width or snakepos[0][0] <=0:
                wn.blit(text_lose,(150,225))

                lose_sound = True
                lose_game =1 
                lose_sound = True
                walls.play()
                mixer_music.pause()
      
            if catch == 0:
                catch += 1
                snakepos.append(snakepos[-1][:])
        
            if snakepos[0][0] >= ds_width or snakepos[0][0] <=0:
                wn.blit(text_lose,(150,225))
                mixer_music.pause()
                lose_game = 1
                lose_sound = True
                walls.play(1)
                    
            if snakepos[0][1] >= ds_height or snakepos[0][1] <=0:
                wn.blit(text_lose,(150,225))
                lose_game = 1
                lose_sound = True
                walls.play()
                mixer_music.pause()

            if snakepos == [0][0] and snakepos == [0][1]:
                wn.blit(text_lose,(150,225))
                lose_game = 1
                lose_sound = True
                mixer_music.pause()

            
            if start_game:
                    for i in range(len(snakepos)-1, 0, -1):
                        snakepos[i] = snakepos[i-1][:]
                    snakepos[0][0] += x_change
                    snakepos[0][1]  += y_change

            if snakepos[0][1]  >= ds_height or snakepos[0][1] <=0:
                 lose_game = 1

            if snakepos[0][0]  >= ds_width or snakepos[0][0] <=0:
                 lose_game = 1

            if catch < 0:
                 lose_game = 1
    if lose_game:
                    wn.blit(text_lose,(150,225))
                    finish = 1

    display.update()
    clock.tick(fps)