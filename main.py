import pygame as pg

pg.init()
width = 1024
height = 800
surface = pg.display.set_mode((width, height))

clock = pg.time.Clock()
pg.font.init()

text_font = pg.font.SysFont('Arial', 30)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    surface.fill('#FFFFFF')


    clock.tick(60)
    pg.display.update()





















