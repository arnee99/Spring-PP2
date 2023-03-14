import pygame
pygame.init()

WIDTH = 320 
HEIGHT = 240
speed = [2, 2]

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
ball = pygame.image.load("images/intro_ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            # pass
            
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > WIDTH:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > HEIGHT:
        speed[1] = -speed[1]
        
    
        
    screen.fill(BLACK)
    screen.blit(ball, ballrect)
    # pygame.display.update()