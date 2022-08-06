from random import randint
import pygame as pg
import sys

pg.init()
pg.time.set_timer(pg.USEREVENT, 1000)

W = 400
H = 400
WHITE = (255, 255, 255)
CARS = ('Images and sounds\car1.png', 'Images and sounds\car2.png', 'Images and sounds\car3.png')
CARS_SURF = []

sc = pg.display.set_mode((W, H))
pg.mixer.music.load('Images and sounds\Beethoven_-_opus47-3_03.ogg')
pg.mixer.music.play(-1)

sound = pg.mixer.Sound('Images and sounds\mixkit-arcade-game-explosion-1699.wav')

for i in range(len(CARS)):
    CARS_SURF.append(pg.image.load(CARS[i]).convert())
    
class Car(pg.sprite.Sprite):

    def __init__(self, x, surf, group):
        pg.sprite.Sprite.__init__(self)
        self.image = surf
        self.image.set_colorkey((0, 0, 0)) # обрати внимание: метод set_colorkey мог быть вызван на 17 или на 23 строке, но это вызволобы ошибку, т. к. тогда self.image не имел бы метода get_rect(). Отсюда можно придти к выводу что поверхность и поверхность с примененным к ней методом set_colorkey() это не одно и тоже, т. е. при применении этого метода создается копия, несмотря на то что именно она будет отображатся на экране это не экземпляр класса Surface (?)
        self.rect = self.image.get_rect(center = (x, 0))
        self.add(group)
        self.speed = randint(1, 3)
    def update(self): # перепишем этот метод, который был унаследован от класса Sprite
        if self.rect.y < H:
            self.rect.y += self.speed
        else:
            self.kill()

class UserCar(pg.sprite.Sprite):

    def  __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('Images and sounds\Sprite-0004.PNG').convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(midbottom = (W / 2, H - 10))

cars = pg.sprite.Group()

Car(randint(1, W), CARS_SURF[randint(0, 2)], cars)
user = UserCar()

while 1:

    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        elif i.type == pg.USEREVENT:
            Car(randint(1, W), CARS_SURF[randint(0, 2)], cars)
    
    sc.fill(WHITE)
    cars.draw(sc)
    cars.update()

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        user.rect.x -= 3
    if keys[pg.K_RIGHT]:
        user.rect.x += 3

    sc.blit(user.image, user.rect)

    pg.display.update()
    pg.time.delay(20)

    if pg.sprite.spritecollideany(user, cars):
        pg.mixer.music.stop()
        sound.play()
        pg.time.delay((int(sound.get_length()) + 1) * 1000)
        sys.exit()

            
