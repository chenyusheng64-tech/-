# LightSystem.py
import pygame

WIDTH, HEIGHT = 1500, 750
player_radius = 40

class LightSystem:
    def __init__(self):
        self.darkness = pygame.Surface((WIDTH , HEIGHT), pygame.SRCALPHA)
        self.sugar_trail_lights = []
        self.wish_list = []

    def update(self, player_rect, have_oil, record, turn_on, of_streetlight):
        self.darkness.fill((0, 0, 0, 255))
        self.light_sugartrail()
        self.light_wishes()
        self.light_player(player_rect, have_oil, record, turn_on)
        self.light_streetlight(of_streetlight)

    def light_streetlight(self, of_streetlight):
        if of_streetlight["turn_on"] :# 送玩家路燈不耗油，可永續照明 and of_streetlight["have_oil"]:
            pygame.draw.circle(self.darkness, (255, 255, 102, 40), (270, 375), 100)
            pygame.draw.circle(self.darkness, (255, 255, 102, 30), (270, 375), 80)
            pygame.draw.circle(self.darkness, (255, 255, 102, 20), (270, 375), 60)
            
    def light_sugartrail(self):
        for point in self.sugar_trail_lights:
            pygame.draw.circle(self.darkness, (255, 255, 255, 30), point, 20)

    def light_wishes(self):
        for wish in self.wish_list.copy():
            for point in self.sugar_trail_lights:
                if wish.rect.collidepoint(point):
                    wish.is_seen = True
                    wish.Seen()
            if wish.is_illuminated:
                pygame.draw.circle(self.darkness, (0, 255, 255, 50), wish.rect.center, 25)

    def light_player(self, player_rect, have_oil, record, turn_on):
        if have_oil and turn_on:
            pygame.draw.circle(self.darkness, (255, 255, 0, 40), player_rect.center, player_radius + 15)
            pygame.draw.circle(self.darkness, (255, 255, 0, 30), player_rect.center, player_radius + 10)
            pygame.draw.circle(self.darkness, (255, 255, 0, 20), player_rect.center, player_radius)
            record["oil"] -= 0.005

    def add_trail_light(self, points):
        self.sugar_trail_lights.append(points)

    def draw(self, screen):
        screen.blit(self.darkness, (0, 0))
