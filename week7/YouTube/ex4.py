import pygame

pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

surf = pygame.Surface((200, 200))
surf.fill(RED)
pygame.draw.circle(surf, GREEN, (100, 100), 80)

surf_alpha = pygame.Surface((W, 100))
pygame.draw.rect(surf_alpha, BLUE, (0, 0, W, 100))
surf_alpha.set_alpha(128)

surf_alpha.blit(surf, (0, 0))
# surf.blit(surf_alpha, (0, 50))
sc.blit(surf_alpha, (50, 50))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()