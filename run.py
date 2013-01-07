from pygame import *

GRAVITY = 0.2
THRUSTER = 0.5

pos = [0,0]
speed = [5,1]

init()
screen = display.set_mode((640,480))
run = True

while run:
    screen.fill((0,0,0))

    screen.fill((255,255,255),(0,475,640,5))
    screen.fill((255,0,0),(310,475,20,5))

    pos[0] += speed[0]
    pos[1] += speed[1]
    
    if pos[1] > (480 - 10):
        if pos[0] >= 310 and pos[0] <= 320 and speed[1] < 5:
            print("Successfull landing")
        else:
            print("You crashed!!")

        run = False
    else:
        screen.fill((0,0,255), (pos[0],pos[1],10,10))

    for e in event.get():
        if e.type == QUIT:
            run = False

    keys = key.get_pressed()

    if keys[K_UP]:
        speed[1] -= THRUSTER
        print("Thruster up")
    elif keys[K_LEFT]:
        speed[0] -= THRUSTER
        print("Thruster left")
    elif keys[K_RIGHT]:
        speed[0] += THRUSTER

    speed[1] += GRAVITY

    display.flip()
    time.delay(40)
