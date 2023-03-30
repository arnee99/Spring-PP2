import pygame
pygame.init()

# print(pygame.font.get_fonts())
# f_sys = pygame.font.SysFont('arial', 12)

W, H = 600, 400

sc = pygame.display.set_mode((W, H))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)

f = pygame.font.Font('fonts/Space Crusaders.ttf', 48)
print(type(f))
sc_text = f.render("Hello Frodo!", 10, RED, YELLOW)
print(type(sc_text))
pos = sc_text.get_rect(center=(W//2, H//2))

sc.fill(WHITE)
sc.blit(sc_text, pos)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()