from pygame import *

finish = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 50))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_DOWN]:
            self.rect.y += 3
    
        if keys_pressed[K_UP]:
            self.rect.y -= 3


class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_s]:
            self.rect.y += 3
    
        if keys_pressed[K_w]:
            self.rect.y -= 3

window = display.set_mode((700, 500))
display.set_caption("GD против Brawl Stars")

clock = time.Clock()

platform1 = Player1("UFO1.png", 10, 100, 3)
platform2 = Player2("UFO2.png", 640, 100, 3)
background = transform.scale(image.load("polyana.jpg"), (700, 500))
game = True



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        platform1.update()
        platform1.reset()
        platform2.update()
        platform2.reset()

    clock.tick(240)

    display.update()
