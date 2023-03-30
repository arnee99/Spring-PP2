import pygame
from ring import Ring
from random import randint

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)

BLACK = (0, 0, 0)
W, H = 728, 410

sc = pygame.display.set_mode((W, H))

score = pygame.image.load('images/score.png').convert_alpha()
f = pygame.font.Font('fonts/Space Crusaders.ttf', 30)

ghollum = pygame.image.load('images/ghollum.png').convert_alpha()
ghollum = pygame.transform.scale(ghollum, (160, 160))
ghollum_rect = ghollum.get_rect(centerx=W//2, bottom=H-5)

rings_data = ({'path': 'ring.png', 'score': 200},
              {'path': 'ring2.png', 'score': 150},
              {'path': 'ring3.png', 'score': 170})

# rings_images = ['ring.png', 'ring2.png', 'ring3.png']
rings_surf = [pygame.image.load('images/'+data['path']).convert_alpha() for 
              data in rings_data]

def createRing(group):
    indX = randint(0, len(rings_surf)-1)
    x = randint(20, W-20)
    speed = randint(1, 4)
    
    return Ring(x, speed, rings_surf[indX], rings_data[indX]['score'], group)

game_score = 0

def collideRings():
    global game_score
    for ring in rings:
        if ghollum_rect.collidepoint(ring.rect.center):
            game_score += ring.score
            ring.kill()

rings = pygame.sprite.Group()

bg = pygame.image.load('images/shire.jpeg').convert()

speed = 10
createRing(rings)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createRing(rings)
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ghollum_rect.x -= speed
        if ghollum_rect.x < 0:
            ghollum_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        ghollum_rect.x += speed
        if ghollum_rect.x > W-ghollum_rect.width:
            ghollum_rect.x = W-ghollum_rect.width
            
    collideRings()        
    sc.blit(bg, (0, 0))
    sc.blit(score, (0, 0))
    sc_text = f.render(str(game_score), 1, (94, 138, 14))
    sc.blit(sc_text, (20, 10))
    rings.draw(sc)
    
    sc.blit(ghollum, ghollum_rect)
    
    pygame.display.update()
    rings.update(H)