from pygame import *
from random import *
wn = display.set_mode((500,500))
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
ds_width = 500
ds_height = 500
food_x = round(randint(0,400)/10)*10 
food_y = round(randint(0,400)/10)*10
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
        draw.rect(wn,(12,240,2),[x_snake,y_snake,10,10])
        draw.rect(wn,(222,10,2),[food_x,food_y,10,10])
        if x_snake == food_x and y_snake == food_y:
            food_x = round(randint(0,400)/10)*10 
            food_y = round(randint(0,400)/10)*10
        if x_snake >= ds_width or x_snake <=0:
            finish =1 
        if y_snake >= ds_height or y_snake <=0:
            finish =1 
        if start_game:
            x_snake += x_change
            y_snake += y_change
    display.update()
    clock.tick(fps)