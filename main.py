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


kni_l_s_rect = kni_le_sta_img.get_rect()
kni_l_s_rect.x = WIDTH // 2
kni_l_s_rect.y = HEIGHT // 2

kni_r_s_rect = kni_ri_sta_img.get_rect()
kni_r_s_rect.x = WIDTH // 2
kni_r_s_rect.y = HEIGHT // 2


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
            elif event.key == pg.K_a:
                move_left = True

        elif event.type == pg.KEYUP:
            if event.key == pg.K_d:
                move_right = False
            elif event.key == pg.K_a:
                move_left = False


    if move_right:
        if kni_r_s_rect.x + kni_ri_sta_img.get_rect().width + speed < WIDTH:
            kni_r_s_rect.x += speed
    elif move_left:
        if kni_l_s_rect.x - speed > 0:
            kni_l_s_rect.x -= speed


    surface.fill(WHITE)
    if move_right:
        surface.blit(kni_ri_sta_img, kni_r_s_rect)
    elif move_left:
        surface.blit(kni_le_sta_img, kni_l_s_rect)


    if kni_r_s_rect.x + kni_ri_sta_img.get_rect().width + speed < WIDTH:
        surface.blit(kni_ri_sta_img, kni_r_s_rect)
    else:
        kni_l_s_rect.x = WIDTH - kni_ri_sta_img.get_rect().width
        surface.blit(kni_ri_sta_img, kni_l_s_rect)

    pg.display.update()
    clock.tick(FPS)


















