from pygame import *
from random import *
wn = display.set_mode((500,500))
fon = transform.scale( image.load("background.png"),(500,500))
display.set_caption("Змійка")
game = 1
finish = 0
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
snakepos  = [ [x_snake, y_snake]]

lose_sound = False
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

            del snakepos[0]
        if snakepos[0][0] >= ds_width or snakepos[0][1] <=0:
            wn.blit(text_lose,(150,225))
            mixer_music.pause()
            finish =1 
            # walls.play(1)
                
                
            
        if snakepos[0][1] >= ds_height or snakepos[0][1] <=0:
            wn.blit(text_lose,(150,225))

            finish =1 


            lose_sound = True


            walls.play()
            mixer_music.pause()
        if snakepos[0][0] >= ds_width or snakepos[0][0] <=0:
            wn.blit(text_lose,(150,225))

            finish =1 


            lose_sound = True


            walls.play()
            mixer_music.pause()
      
        if catch == 0:
            wn.blit(text_lose,(150,225))

            finish =1 


            lose_sound = True


            walls.play()
            mixer_music.pause()
            

            
        if start_game:
                for i in range(len(snakepos)-1, 0, -1):
                    snakepos[i] = snakepos[i-1][:]
                snakepos[0][0] += x_change
                snakepos[0][1]  += y_change
    if snakepos[0][1]  >= ds_height or snakepos[0][1] <=0:
            wn.blit(text_lose,(125,225))
    if snakepos[0][0]  >= ds_width or snakepos[0][0] <=0:
            wn.blit(text_lose,(125,225))
    if catch < 0:
            wn.blit(text_lose,(150,225))

    display.update()
    clock.tick(fps)