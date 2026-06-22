import pygame
from Lantern import Lantern

YELLOW = (255, 255, 102)
DARK_GRAY = (80, 80, 80)

class StreetLight(Lantern):
    def __init__(self, of_streetlight):
        super().__init__(of_lantern = of_streetlight)
        self.image = pygame.Surface((14, 30))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (270, 375)
        
        self.color1 = YELLOW
        self.color2 = DARK_GRAY

    def update_position(self, player_rect = None):
        pass
    
    # 繼承 status() 方法