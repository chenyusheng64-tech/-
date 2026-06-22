# Lantern.py
import pygame

ORANGE = (255, 153, 18)
GRAY = (192, 192 ,192)

class Lantern(pygame.sprite.Sprite):
    def __init__(self, of_lantern):
        super().__init__()
        self.of_lantern = of_lantern
        self.image = pygame.Surface((10, 15))
        self.image.fill(ORANGE)
        self.color1 = ORANGE
        self.color2 = GRAY
        self.rect = self.image.get_rect()
        self.turn = 10

    def update_position(self, player_rect):
        self.rect.centerx = player_rect.centerx + self.turn
        self.rect.centery = player_rect.centery
        
    def status(self):
        if self.of_lantern["turn_on"] and self.of_lantern["have_oil"]:
            self.image.fill(self.color1)
        else:
            self.image.fill(self.color2)
            
            
        
        
