from mode import *
from pygame import *

import menu

GRAVITY = 0.2
THRUSTER = 0.5
FUELUSE = 1

class Game(Mode):
    def __init__(self, core):
        Mode.__init__(self, core, 30)

        self.pos = [620,0]
        self.speed = [-5,1]
        self.fuel = 100

        self.fonten = font.Font(None, 14)
        self.messagefont = font.Font(None, 20)
        self.motorsound = mixer.Sound("motor.wav")

        self.shipImages = [ image.load("ship-%i.png" % i).convert() for i in range(0,3) ]
        for i,s in enumerate(self.shipImages):
            self.shipImages[i].set_colorkey((0,0,255))

        self.animCounter = 0
        self.doAnimate = False

    def onDraw(self, screen, core, numTicks):
        screen.fill((0,0,0))

        screen.fill((255,255,255),(0,475,640,5))
        screen.fill((255,0,0),(300,475,40,5))

        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
    
        if self.pos[1] > (475 - 20):
            if self.pos[0] >= 300 and self.pos[0] <= 320 and self.speed[1] < 5:
                print("Successfull landing")
                core.setActiveMode( menu.Menu(core, 1) )
            else:
                print("You crashed!!")
                core.setActiveMode( menu.Menu(core, 2) )

            self.pos[1] = 455
            #run = False
    
        if self.doAnimate:
            if not mixer.get_busy():
                self.motorsound.play(0)

            self.animCounter += 1
            screen.blit(self.shipImages[1 + int(self.animCounter / 3)], (self.pos[0], self.pos[1], 20, 20))

            if self.animCounter == 5:
                self.animCounter = 0

            self.fuel -= FUELUSE
        else:
            screen.blit(self.shipImages[0], (self.pos[0], self.pos[1], 20, 20))

        keys = key.get_pressed()

        if self.fuel <= 0:
            self.fuel = 0
            self.doAnimate = False
            self.motorsound.stop()
        else:
            self.doAnimate = True
            if keys[K_UP]:
                self.speed[1] -= THRUSTER
                #print("Thruster up")
            elif keys[K_LEFT]:
                self.speed[0] -= THRUSTER
                #print("Thruster left")
            elif keys[K_RIGHT]:
                self.speed[0] += THRUSTER
            else:
                self.doAnimate = False
                self.motorsound.stop()

        self.speed[1] += GRAVITY

        #Print stats
        screen.blit(self.fonten.render("V-Speed: %f" % self.speed[1], True, (0,255,0)), (10,10,40,100))
        screen.blit(self.fonten.render("Fuel: %f" % self.fuel, True, (0,255,0)), (10,20,40,100))
