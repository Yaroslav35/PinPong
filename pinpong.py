from pygame import *

window = display.set_mode((700, 500))
display.set_caption("GD против Brawl Stars")
clock = time.Clock()

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    
    clock.tick(240)

    display.update()