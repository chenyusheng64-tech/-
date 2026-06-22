# MapManager
import pygame
import random

WHITE, GRAY, BLACK, RED = (255, 255, 255), (169, 169, 169), (0, 0, 0), (255, 0, 0)
WIDTH, HEIGHT = 1500, 750

class Granule(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(250, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
        
class Wish(pygame.sprite.Sprite):
    total_count = 0
    
    def __init__(self, x, y, check_see_wish):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0)) # (0, 255, 0) 測試用
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_seen = False
        self.is_illuminated = False
        self.is_not_collected = True
        self.check_see_wish = check_see_wish
        Wish.total_count +=1
    
    def Seen(self):
        if self.is_seen and not self.is_illuminated:
            #self.image.fill(GRAY)  
            self.image = pygame.image.load("20260620013612712230_x1GZC0Dn-removebg-preview.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (32, 32))
            self.check_see_wish[0] = True
    
    def illuminate(self):
        #self.image.fill(RED)
        self.image = pygame.image.load("20260620011552962666_X5VIjZIn-removebg-preview.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.is_illuminated = True
        
    @classmethod
    def get_total_count(cls):
        return cls.total_count