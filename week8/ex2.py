import pygame
from ring import Ring

pygame.init()

BLACK = (0, 0, 0)
W, H = 728, 410

sc = pygame.display.set_mode((W, H))
speed = 1
bg = pygame.image.load('images/shire.jpeg').convert()

r1 = Ring(W//2, speed, 'images/ring.png')
r2 = Ring(250, speed+1, 'images/ring2.png')
r3 = Ring(500, speed+2, 'images/ring3.png')

# b1 = pygame.transform.scale(b1.image, (80, 80))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    sc.blit(bg, (0, 0))
    sc.blit(r1.image, r1.rect)
    sc.blit(r2.image, r2.rect)
    sc.blit(r3.image, r3.rect)
    pygame.display.update()
    
    
    r1.update(H)
    r2.update(H)
    r3.update(H)
