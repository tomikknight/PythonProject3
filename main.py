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

kni_le_sta_img = pg.image.load('images/knight/left/knight_stand_l.png').convert_alpha()
kni_ri_sta_img = pg.image.load('images/knight/right/knight_stand_r.png').convert_alpha()
floor_img = pg.image.load('images/no knight/floor/floor1.png')
floor2_2img = pg.image.load('images/no knight/floor/floor2_2.png')
floor2_1img = pg.image.load('images/no knight/floor/floor2_1.png')
floor2_3img = pg.image.load('images/no knight/floor/floor2_3.png')

# как это работает - есть функция scale, при помощи которой мы изменяем размеры спрайта. Мы указываем в функции
# в качестве ширины ширину экрана, в качестве высоты - высоту, которая была.
# можно сохранить пропорцию, чтобы при изменении ширины изменить и высоту, для этого необходимо пересчитать высоту
# и в 25-ой строке вместо floor_height вписать высоту.

current_sprite = kni_ri_sta_img
sprite_rect = current_sprite.get_rect()
sprite_rect.x = WIDTH // 2.05
sprite_rect.y = HEIGHT // 10

floor_rect = floor_img.get_rect()
floor_rect.x = 200
floor_rect.y = HEIGHT - floor_img.get_rect().height + 85

floor2_1rect = floor2_1img.get_rect()
floor2_1rect.x = -530
floor2_1rect.y = HEIGHT - floor2_1img.get_rect().height + 70

floor2_3rect = floor2_3img.get_rect()
floor2_3rect.x = -100
floor2_3rect.y = HEIGHT - floor2_3img.get_rect().height + 67

floor2_2rect = floor2_2img.get_rect()
floor2_2rect.x = 0
floor2_2rect.y = HEIGHT - floor2_2img.get_rect().height + 67

speed = 6

move_left = False
move_right = False
jump = False
lives = 5

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
                current_sprite = kni_ri_sta_img
            elif event.key == pg.K_a:
                move_left = False
                current_sprite = kni_le_sta_img

    if move_right:
        if sprite_rect.x + current_sprite.get_rect().width + speed < WIDTH:
            sprite_rect.x += speed
    elif move_left:
        if sprite_rect.x - speed > 0:
            sprite_rect.x -= speed

    surface.fill(WHITE)

    surface.blit(floor2_3img, floor2_3rect)
    surface.blit(floor2_2img, floor2_2rect)
    surface.blit(floor2_1img, floor2_1rect)
    surface.blit(floor_img, floor_rect)

    surface.blit(current_sprite, sprite_rect)


    pg.display.update()
    clock.tick(FPS)
























