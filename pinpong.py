from pygame import *
font.init()
finish = False
speed_x = 2
speed_y = 2
win_height = 500
font1 = font.Font(None, 35)
win1 = font1.render('Игрок 1 выйграл!', True, (180,0,0))
win2 = font1.render('Игрок 2 выйграл!', True, (180,0,0))
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

        if keys_pressed[K_DOWN] and self.rect.y < 445:
            self.rect.y += 3
    
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 3


class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_s] and self.rect.y < 445:
            self.rect.y += 3
    
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 3

class Ball(GameSprite):
    def update(self):
        pass


window = display.set_mode((700, 500))
display.set_caption("GD против Brawl Stars")

clock = time.Clock()

platform1 = Player1("UFO1.png", 10, 100, 3)
platform2 = Player2("UFO2.png", 640, 100, 3)
ball = Ball("Ball.png", 300, 300, 3)
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
        ball.reset()
        ball.update()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(platform1, ball) or sprite.collide_rect(platform2, ball):
            speed_x *= -1

        if ball.rect.x > 695:
            #выйграла 1 ракетка
            window.blit(win1,(200,200))
            finish = True
        
        if ball.rect.x < 1:
            #выйграла 2 ракетка
            window.blit(win2,(200,200))
            finish = True

    clock.tick(240)

    display.update()
