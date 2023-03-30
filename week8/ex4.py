import pygame
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

pygame.mixer.music.load('audio/bird.mp3')
pygame.mixer.music.play(-1)

W, H = 500, 300
sc = pygame.display.set_mode((W, H))

s = pygame.mixer.Sound('audio/catch.ogg')

flPause = False
vol = 1.0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flPause = not flPause
                if flPause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_LEFT:
                vol -= 0.1
                pygame.mixer.music.set_volume(vol)
            elif event.key == pygame.K_RIGHT:
                vol += 0.1
                pygame.mixer.music.set_volume(vol)
            elif event.key == pygame.K_RETURN:
                s.play()
            
    