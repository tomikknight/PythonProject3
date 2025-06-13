import pygame as pg

pg.init()
width = 1024
height = 800
surface = pg.display.set_mode((width, height))
clock = pg.time.Clock()
kni = 'knight/knight_stand.png'
move_left1 = False
move_right1 = False
move_up1 = False
move_down1 = False
speed = 5



while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                move_left1 = True
            elif event.key == pg.K_RIGHT:
                move_right1 = True
            elif event.key == pg.K_UP:
                move_up1 = True
            elif event.key == pg.K_DOWN:
                move_down1 = True

        elif event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                move_left1 = False
            elif event.key == pg.K_RIGHT:
                move_right1 = False
            elif event.key == pg.K_UP:
                move_up1 = False
            elif event.key == pg.K_DOWN:
                move_down1 = False
    surface.fill(('#FFFFFF'))


    if move_left1 and kni > 0:
        kni -= speed
    elif move_right1 and kni + 40 < width:
        kni += speed
    elif move_up1 and kni > 0:
        kni -= speed
    elif move_down1 and kni + 70 < height:
        kni += speed



    clock.tick(60)
    pg.display.update()




















