import pygame
from ring import Ring

pygame.init()

BLACK = (0, 0, 0)
W, H = 728, 410

sc = pygame.display.set_mode((W, H))
rings = pygame.sprite.Group()

bg = pygame.image.load('images/shire.jpeg').convert()
speed = 1

rings.add(Ring(W//2, speed, 'images/ring.png')
          ,Ring(250, speed+1, 'images/ring2.png')
          ,Ring(500, speed+2, 'images/ring3.png'))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    sc.blit(bg, (0, 0))
    rings.draw(sc)
    
    pygame.display.update()
    rings.update(H)