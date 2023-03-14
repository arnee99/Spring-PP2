import pygame
pygame.init()

pygame.display.set_mode((600, 400), pygame.RESIZABLE)
pygame.display.set_caption("First YouTube test game")
# pygame.display.set_icon(pygame.image.load("images/intro_ball.png"))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # pygame.quit()
            # checkRunning = False
            exit()
            
    
    print("The game is running")
            
