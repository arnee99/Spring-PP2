import pygame
pygame.init()

W, H = 600, 400
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)

pygame.draw.rect(sc, WHITE, (10,10,50,100))

pygame.draw.line(sc, BLUE, (200, 20), (350, 50), 2)
pygame.draw.lines(sc, GREEN, True, [(300, 80), (350, 80), (400, 200)], 2)

pygame.draw.aaline(sc, RED, (200, 40), (350, 70), 2)
pygame.draw.aalines(sc, GREEN, True, [(200, 80), (250, 80), (300, 200)], 2)

pygame.draw.polygon(sc, WHITE, [[150, 210], [180, 250], [90, 290], [30, 230], [40, 150]], 1)
pygame.draw.polygon(sc, WHITE, [[150, 310], [180, 350], [90, 390], [30, 330], [30, 180]], 1)

pygame.draw.circle(sc, RED, (300, 250), 40, 5)
pygame.draw.ellipse(sc, BLUE, (300, 300, 100, 50), 1)

pi = 3.14
pygame.draw.arc(sc, RED, (450, 30, 50, 150), pi, 2*pi, 5)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()