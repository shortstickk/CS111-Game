import pygame
import math

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

BALL_WIDTH, BALL_HEIGHT = 40, 40

class golfBall:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.vx = 0
        self.vy = 0
        self.mouseDown = False
        self.mouseRelease = False
        self.cp = []
        self.rp = []

    def resetInputs(self):
        self.mouseDown = False
        self.mouseRelease = False
    
    def mouseButtonDown(self, position):
        self.mouseDown = True
        self.cp = position
    
    def mouseButtonRelease(self, position):
        self.mouseRelease = True
        self.rp = position
        


    def tick(self,field):
        if self.vx ** 2 + self.vy ** 2 > 0.0001:
            self.x += self.vx
            self.y += self.vy
            self.vx *= 0.98
            self.vy *= 0.98
        else:
            if self.mouseRelease:
                dlx = self.cp[0] - self.rp[0]
                dly = self.cp[1] - self.rp[1]
                ml = math.sqrt(dlx ** 2 + dly ** 2)
                if ml > 0.5:
                    nlx = dlx/ml
                    nly = dly/ml
                    p = min(ml/10, 10)
                    self.vx = p * nlx
                    self.vy = p * nly
                
        
    def render(self, WIN):
        WIN.fill(GREEN)
        pygame.draw.circle(WIN, BLACK, (self.x, self.y), 10)
        
    def setPos(self, x, y):
        self.x = x
        self.y = y    
    

