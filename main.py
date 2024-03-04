import pygame
from golfBall import *

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Mini-Golf")

WHITE = (255,255,255)

FPS = 60
ball = golfBall()


def main():
    field = pygame.Rect(100, 100, WIDTH, HEIGHT)
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        ball.resetInputs()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                ball.mouseButtonDown(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                ball.mouseButtonRelease(event.pos)

        
        ball.tick(field)
        ball.render(WIN)   
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()
    
