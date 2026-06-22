# farm.py
import pygame
import time
import random

class Farm(pygame.sprite.Sprite):
    def __init__(self, White = (255, 227, 132)):
        super().__init__()
        #self.image = pygame.Surface((250, 400))
        #self.image.fill(White)
        self.image = pygame.image.load("20260620112614740043_JuHmf1EG.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (250, 400))
        self.rect = self.image.get_rect()
        self.rect.y = 175
        
class Pond(pygame.sprite.Sprite):
    def __init__(self, Blue = (176 , 224, 230)):
        super().__init__()
        #self.image = pygame.Surface((100, 150))
        #self.image.fill(Blue)
        self.image = pygame.image.load("20260620093700320978_sPta3sQH.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.y = 175
        
class Shop(pygame.sprite.Sprite):
    def __init__(self, Blue = (218, 112, 214)):
        super().__init__()
        #self.image = pygame.Surface((100, 150))
        #self.image.fill(Blue)
        self.image = pygame.image.load("20260620094159948237_tnh45hPA.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (175, 175))
        self.rect = self.image.get_rect()
        self.rect.y = 400
        
class Land(pygame.sprite.Sprite):
    def __init__(self, Grean = (0, 199, 140)):
        super().__init__()
        #self.image = pygame.Surface((100, 150))
        #self.image.fill(Grean)
        self.image = pygame.image.load("20260620091333228424_xL4Nz012.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 175
        
class Feed(pygame.sprite.Sprite):
    def __init__(self, Pink = (255, 192, 203)):
        super().__init__()
        #self.image = pygame.Surface((150, 150))
        #self.image.fill(Pink)
        self.image = pygame.image.load("20260620111538067560_MF92140j.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.x = 175
        self.rect.y = 500

class FarmSystem:
    def __init__(self):
        self.plants = []         # 儲存所有作物
        self.animals = []        # 飼養中的動物
        self.ready_products = [] # 可賣的產品

        # 初始化一隻會生蛋的雞，並記錄創建時間
        self.animals.append({
            'type': 'chicken',
            'last_egg_time': None  # 第一次產蛋將在第一次呼叫 update_animal_products 時初始化
        })

        # 釣魚系統狀態
        self.fishing = False
        self.fish_start_time = 0

    def plant_crop(self, crop_type):
        # 增加一筆種植作物
        self.plants.append({
            'type': crop_type,'growth': 0,'ready': False
        })

    def update_growth(self, ticks=1):
        # 模擬作物成長，ticks 控制成長速度
        for plant in self.plants:
            if not plant['ready']:
                plant['growth'] += ticks
                if plant['growth'] >= 1800:  # 成熟所需時間 30 秒
                    plant['ready'] = True
                    self.ready_products.append(plant['type'])

    def harvest(self):
        # 收成所有已成熟作物
        self.plants = [p for p in self.plants if not p['ready']]
        return self.ready_products

    def start_fishing(self):
        # 開始釣魚，記錄開始時間
        self.fishing = True
        self.fish_start_time = time.time()

    def check_fishing_result(self, player_rect, pond_rect):
        if not player_rect.colliderect(pond_rect):
            return None 
        # 檢查是否過了 15 秒          
        if self.fishing and (time.time() - self.fish_start_time >= 15):
            self.fishing = False
            if random.random() < 0.5:
                self.ready_products.append('fish')
                return 'fish'
            return -1
        return 'waiting'

    def update_animal_products(self):
        # 每隻動物根據時間決定是否可以產物
        current_time = time.time()
        for animal in self.animals:
            if animal['type'] == 'chicken':
                if animal['last_egg_time'] is None:
                    # 初始化產蛋時間
                    animal['last_egg_time'] = current_time
                elif current_time - animal['last_egg_time'] >= 60:  # 每 60 秒產一次蛋
                    self.ready_products.append('egg')
                    animal['last_egg_time'] = current_time

    
    def take_products(self):
        # 將可售產品取出，並清空內部儲存
        products = self.ready_products.copy()
        self.ready_products.clear()
        return products
