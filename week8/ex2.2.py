import pygame
from ring import Ring
from random import randint

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)

BLACK = (0, 0, 0)
W, H = 728, 410

sc = pygame.display.set_mode((W, H))

rings_images = ['ring.png', 'ring2.png', 'ring3.png']
rings_surf = [pygame.image.load('images/'+path).convert_alpha() for 
              path in rings_images]

def createRing(group):
    indX = randint(0, len(rings_surf)-1)
    x = randint(20, W-20) # from 20 to 708
    speed = randint(1, 3)

    return Ring(x, speed, rings_surf[indX], group)

rings = pygame.sprite.Group()

bg = pygame.image.load('images/shire.jpeg').convert()

speed = 1
createRing(rings)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createRing(rings)
            
    sc.blit(bg, (0, 0))
    rings.draw(sc)
    
    pygame.display.update()
    rings.update(H)