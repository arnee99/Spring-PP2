import pygame

pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

ground = H - 70
jump_force = 20
move = jump_force + 1

hero = pygame.Surface((40, 50))
hero.fill(BLUE)
rect = hero.get_rect(centerx = W//2)
rect.bottom = ground

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ground == rect.bottom:
                move = -jump_force
                
    if move <= jump_force:
        if rect.bottom + move < ground:
            rect.bottom += move
            if move < jump_force:
                move += 1
        else:
            rect.bottom = ground
            move = jump_force + 1
            
    sc.fill(WHITE)
    sc.blit(hero, rect)
    pygame.display.update()