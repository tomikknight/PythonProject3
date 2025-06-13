import pygame as pg
from random import *

pg.init()
pg.font.init()
clock = pg.time.Clock()


width = 1200
height = 800
white = (255, 255, 255)
black = (0, 0, 0)
green = (34, 177, 76)
yellow = (255, 242, 0)
FPS = 60
FONT = pg.font.SysFont('Arial', 35)
surface = pg.display.set_mode((width, height))



knight_img = pg.image.load('knight/knight_stand.png')
knight_rect = knight_img.get_rect()
knight_rect.x = width // 2
knight_rect.y = height // 2

move_left = False
move_right = False
move_up = False
move_down = False
speed = 5

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                move_right = True
            elif event.key == pg.K_a:
                move_left = True
            elif event.key == pg.K_w:
                move_up = True
            elif event.key == pg.K_s:
                move_down = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_d:
                move_right = False
            elif event.key == pg.K_a:
                move_left = False
            elif event.key == pg.K_w:
                move_up = False
            elif event.key == pg.K_s:
                move_down = False


    surface.fill(white)


    if move_left and knight_rect.x > 0:
        knight_rect.x -= speed
    if move_right and knight_rect.x + knight_rect.width < width:
        knight_rect.x += speed
    if move_up and knight_rect.y > 0:
        knight_rect.y -= speed
    if move_down and knight_rect.y + knight_rect.height < height:
        knight_rect.y += speed


    surface.blit(knight_img, knight_rect)


    clock.tick(FPS)
    pg.display.update()



















