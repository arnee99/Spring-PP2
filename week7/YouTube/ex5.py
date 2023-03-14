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
# rect = hero.get_rect(topleft=(100, 50))
rect = hero.get_rect(center=(300, 200))
rect.bottom = ground

# rect1 = pygame.Rect((0, 0, 30, 30))
# rect2 = pygame.Rect((30, 30, 30, 30))

# rect2.move_ip(20,20)
# print(rect2)
# rect3 = rect2.union(rect1)
# print(rect3)

# sc.fill(WHITE)
# sc.blit(hero, (100, 50))
# pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ground == rect.bottom:
                move = - jump_force
    
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