from pygame import *
from mode import *
from game import Game

class Menu(Mode):
    def __init__(self, core, status = 0):
        Mode.__init__(self, core, 30)
        self.status = status

        self.statusFont = font.Font(None, 50)
        self.infoFont = font.Font(None, 70)

    def onDraw(self, screen, core, numTicks):
        screen.fill((0,0,0))

        if self.status != 0:
            texts = {"1": "You landed successfully", "2": "You crashed... sucker!"}
            text = self.statusFont.render(texts[ str(self.status) ], True, (0,255,0))

            draw.rect(screen, (0,255,0), Rect(50, 80, 540, 200), 1)
            screen.blit(text, (50 + ((540 / 2) - (text.get_width() / 2)), 80 + ((200/2) - (text.get_height() / 2))))
            
        info = self.infoFont.render("[p]lay          [q]uit", True, (0,255,0))
        screen.blit(info, (320 - (info.get_width() / 2), 380))

    def handleEvent(self, e, core, numTicks):
        if e.type == KEYDOWN:
            if e.key == K_p:
                core.setActiveMode( Game(core) )
            elif e.key == K_q:
                core.pleaseExit()
