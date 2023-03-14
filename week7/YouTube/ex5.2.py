import pygame

pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

rect1 = pygame.Rect((0, 0, 30, 30))
rect2 = pygame.Rect((30, 30, 30, 30))

rect2.move_ip(20, 20)
print(rect2)
rect3 = rect2.union(rect1)
print(rect3)

hero = pygame.Surface((40, 50))
hero.fill(BLUE)
rect = hero.get_rect()
# 2 rect = hero.get_rect(center = (W // 2, H // 2))
# rect.x = 100
# rect.y = 20
print(rect.center)


sc.fill(WHITE)
sc.blit(hero, (100, 50))
# 2 sc.blit(hero, rect)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    sc.fill(WHITE)
    sc.blit(hero, (100, 50))
    pygame.display.update()