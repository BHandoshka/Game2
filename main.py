import pygame as pg
import os
import sys

pg.init()

SIZE_WINDOW = WIDTH, HEIGHT = 1000, 500
# BG_COLOR (0, 128, 0)
FPS = 60
clock = pg.time.Clock()

screen = pg.display.set_mode(SIZE_WINDOW)

BG_image = pg.image.load('Image/stars.jpg')
BG = pg.transform.scale(BG_image, (WIDTH, HEIGHT))

images1 = []
path = 'Image/Bear'
for file_name in os.listdir(path):
    image = pg.image.load(path + os.sep + file_name)
    images1.append(image)

images2 = []
image = pg.image.load('Image/1.png')
images2.append(image)


class AnimateSprite(pg.sprite.Sprite):
    def __init__(self, x, y, img):
        pg.sprite.Sprite.__init__(self)
        self.images = img
        self.index = 0
        self.image = self.images[self.index]
        if self.images == images2:
            self.image = pg.transform.rotozoom(self.image, 0, 0.5)
            self.image = pg.transform.flip(self.image, False, False)  # x = |, y = --

            self.images[0] = self.image
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        # Анимация
        self.index += 0.1
        self.image = self.images[int(self.index % len(self.images))]
        self.rect = self.image.get_rect(center=self.rect.center)
        # if self is cat:
        self.rect.x += 1


bear = AnimateSprite(x=WIDTH // 2, y=HEIGHT // 2, img=images1)
cat = AnimateSprite(x=WIDTH // 2, y=HEIGHT // 2, img=images2)
sprites = pg.sprite.Group(bear, cat)
sprites.remove(cat)  # спрятаться
sprites.add(cat)  # показаться
bearW, bearH = bear.image.get_width(), bear.image.get_height()
catW, catH = cat.image.get_width(), cat.image.get_height()
# print(bearW, bearH, catW, catH)
K = bearH * 0.16

while True:
    for e in pg.event.get():  # e это event
        if e.type == pg.QUIT:
            sys.exit(0)

    cat.rect.y = bear.rect.y - catH + K
    cat.rect.x = bear.rect.center[0] - catW // 2

    if bear.rect.x > WIDTH:
        bear.rect.x = - bearW

    screen.blit(BG, (0, 0))

    sprites.update()
    sprites.draw(screen)

    pg.display.update()
    clock.tick(FPS)
