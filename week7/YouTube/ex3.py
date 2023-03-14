import pygame

pygame.init()
W, H = 600, 400

sc = pygame.display.set_mode((W, H))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

x = W // 2
y = H // 2
speed = 5

# FPS = 60
# clock = pygame.time.Clock()

fLeft = fRight = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fLeft = True
            elif event.key == pygame.K_RIGHT:
                fRight = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                fLeft = fRight = False
    
    if fLeft:
        x -= speed
    if fRight:
        x += speed
        
    sc.fill(WHITE)
    pygame.draw.rect(sc, BLUE, (x, y, 10, 20))
    pygame.display.update()
    
    # clock.tick(FPS)