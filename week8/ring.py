import pygame

# class Ring(pygame.sprite.Sprite):
#     def __init__(self, x, speed, filename):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(filename).convert_alpha()
#         self.image = pygame.transform.scale(self.image, (40, 40))
#         self.rect = self.image.get_rect(center=(x, 0))
#         self.speed = speed
        
#     def update(self, *args):
#         if self.rect.y < args[0]-20:
#             self.rect.y += self.speed
#         else:
#             self.rect.y = 0

# class Ring(pygame.sprite.Sprite):
#     def __init__(self, x, speed, surf, group):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = surf
#         self.image = pygame.transform.scale(self.image, (40, 40))
#         self.rect = self.image.get_rect(center=(x, 0))
#         self.speed = speed
#         self.add(group)
        
#     def update(self, *args):
#         if self.rect.y < args[0]-20:
#             self.rect.y += self.speed
#         else:
#             self.rect.y = 0

class Ring(pygame.sprite.Sprite):
    def __init__(self, x, speed, surf, score, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.score = score
        self.add(group)
        
    def update(self, *args):
        if self.rect.y < args[0]-20:
            self.rect.y += self.speed
        else:
            self.kill()