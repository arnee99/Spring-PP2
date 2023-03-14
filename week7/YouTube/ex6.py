import pygame
pygame.init()

W, H = 600, 400
sc = pygame.display.set_mode((W, H))
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)

print(pygame.image.get_extended())

ball_surf = pygame.image.load("images/intro_ball.gif")
ball_rect = ball_surf.get_rect(center=(W//2, H//2))

beach_surf = pygame.image.load("images/beach.jpeg")

sc.blit(beach_surf, (0,0))
sc.blit(ball_surf, ball_rect)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()