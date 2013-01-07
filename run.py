from pygame import *

GRAVITY = 0.2
THRUSTER = 0.5
FUELUSE = 1

pos = [620,0]
speed = [-5,1]
fuel = 100

init()
screen = display.set_mode((640,480))
fonten = font.Font(None, 14)
motorsound = mixer.Sound("motor.wav")
run = True

shipImages = [ image.load("ship-%i.png" % i).convert() for i in range(0,3) ]
for i,s in enumerate(shipImages):
    shipImages[i].set_colorkey((0,0,255))

animCounter = 0
doAnimate = False

while run:
    screen.fill((0,0,0))

    screen.fill((255,255,255),(0,475,640,5))
    screen.fill((255,0,0),(300,475,40,5))

    pos[0] += speed[0]
    pos[1] += speed[1]
    
    if pos[1] > (475 - 20):
        if pos[0] >= 300 and pos[0] <= 320 and speed[1] < 5:
            print("Successfull landing")
        else:
            print("You crashed!!")

        pos[1] = 455
        run = False
    
    if doAnimate:
        if not mixer.get_busy():
            motorsound.play(0)

        animCounter += 1
        screen.blit(shipImages[1 + int(animCounter / 3)], (pos[0], pos[1], 20, 20))

        if animCounter == 5:
            animCounter = 0

        fuel -= FUELUSE
    else:
        screen.blit(shipImages[0], (pos[0], pos[1], 20, 20))

    for e in event.get():
        if e.type == QUIT:
            run = False

    keys = key.get_pressed()


    if fuel <= 0:
        fuel = 0
        doAnimate = False
        motorsound.stop()
    else:
        doAnimate = True
        if keys[K_UP]:
            speed[1] -= THRUSTER
            #print("Thruster up")
        elif keys[K_LEFT]:
            speed[0] -= THRUSTER
            #print("Thruster left")
        elif keys[K_RIGHT]:
            speed[0] += THRUSTER
        else:
            doAnimate = False
            motorsound.stop()

    speed[1] += GRAVITY

    #Print stats
    screen.blit(fonten.render("V-Speed: %f" % speed[1], True, (0,255,0)), (10,10,40,100))
    screen.blit(fonten.render("Fuel: %f" % fuel, True, (0,255,0)), (10,20,40,100))

    display.flip()
    time.delay(40)
