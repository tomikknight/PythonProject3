import pygame as pg
from random import randint


pg.init()
pg.font.init()
clock = pg.time.Clock()


WIDTH, HEIGHT = 1800, 1000
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 177, 76)
YELLOW = (255, 242, 0)
FPS = 60
FONT = pg.font.SysFont('Arial', 35)
surface = pg.display.set_mode((WIDTH, HEIGHT))


kni_le_sta_img = pg.image.load('knight/left/knight_stand_l.png')
kni_ri_sta_img = pg.image.load('knight/right/knight_stand_r.png')


current_sprite = kni_ri_sta_img
sprite_rect = current_sprite.get_rect()
sprite_rect.x = WIDTH // 2
sprite_rect.y = HEIGHT // 2

speed = 6

move_left = False
move_right = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                move_right = True
                current_sprite = kni_ri_sta_img
            elif event.key == pg.K_a:
                move_left = True
                current_sprite = kni_le_sta_img

        elif event.type == pg.KEYUP:
            if event.key == pg.K_d:
                move_right = False
                current_sprite = kni_le_sta_img
            elif event.key == pg.K_a:
                move_left = False
                current_sprite = kni_ri_sta_img


    if move_right:
        if sprite_rect.x + current_sprite.get_rect().width + speed < WIDTH:
            sprite_rect.x += speed
    elif move_left:
        if sprite_rect.x - speed > 0:
            sprite_rect.x -= speed


    surface.fill(WHITE)
    surface.blit(current_sprite, sprite_rect)


    if sprite_rect.x + current_sprite.get_rect().width + speed < WIDTH:
        surface.blit(current_sprite, sprite_rect)
    else:
        sprite_rect.x = WIDTH - current_sprite.get_rect().width
        surface.blit(current_sprite, sprite_rect)

    pg.display.update()
    clock.tick(FPS)


















