# Player.py

import pygame
import math

GREEN = (0, 255, 0)

'''
def limit_mouse_move(update_func):
    def wrapper(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x > self.rect.centerx:
            self.rect.x += self.speed
        if mouse_x < self.rect.centerx:
            self.rect.x -= self.speed
        if mouse_y > self.rect.centery:
            self.rect.y += self.speed
        if mouse_y < self.rect.centery:
            self.rect.y -= self.speed
        return update_func(self)
    return wrapper
    
def mouse_move(update_func):
    def wrapper(self):
        vetor = lambda mouse_x, mouse_y, center_x, center_y: ((mouse_x - center_x), (mouse_y - center_y))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        x, y = vetor(mouse_x, mouse_y, self.rect.centerx, self.rect.centery)
        distance = math.sqrt(x**2 + y**2)
        if distance >10:
            x /= distance
            y /= distance
            self.rect.x += x * self.speed
            self.rect.y += y * self.speed     
        self.rect.clamp_ip(self.screen.get_rect())
        return update_func(self)
    return wrapper
'''

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, lantern):
        super().__init__()
        self.screen = screen
        self.lantern = lantern
        self.speed = 5
        # 載入像素角色貼圖
        self.original_image = pygame.image.load("20260619134937455865_8udilRHt-removebg-preview.png").convert_alpha()
        self.original_image = pygame.transform.scale_by(self.original_image, 0.2)
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (50, 375)
    
    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.lantern.turn = 10
            self.image = pygame.transform.flip(self.original_image, True, False)
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.lantern.turn = -10
            self.image = self.original_image
        if key_pressed[pygame.K_UP]:
            self.rect.y -= self.speed
        if key_pressed[pygame.K_DOWN]:
            self.rect.y += self.speed   
        self.rect.clamp_ip(self.screen.get_rect())
        
        self.lantern.update_position(self.rect)
        self.lantern.status()
        
    '''  
    def seen(self, turn_on, in_light):
        if not turn_on or not in_light:
            BLACK = (0, 0, 0)
            self.image.fill(BLACK)
        else:
            GREEN = (0, 255, 0)
            self.image.fill(GREEN)
    '''
