# main.py
import pygame
import os
import time
from Player import Player
from MapManager import Granule, Wish
from LightSystem import LightSystem
from Collection import GranulesCount, WishCount
from SugarPath import SugarPath
from Lantern import Lantern
from Streetlight import StreetLight
from UI import UI
from farm import Farm, Pond, Shop, Land, Feed
from farm import FarmSystem
from economy import EconomySystem


# 遊戲參數
FPS = 60
WIDTH, HEIGHT = 1500, 750
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
player_radius = 40
granules_number = 500
wish_number = 100
decay_rate = 0.5

#遊戲變數
record = {"happiness": 0, "granules_count": 0, "wishes_count": 0, "oil": 10000}
of_lantern = {"have_oil": True, "turn_on": False}
of_streetlight = {"have_oil": True, "turn_on": True}
inventory = {"money": 10, "seed": 3,"fish":0, "wheat":0, "egg":0}
text1 = None #pond
text2 = None #land
text3 = None
text4 = None
texta = None #granules
text_time = time.time()
check_see_wish = [False]
harvested = []

# 初始化
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("糖粒之願")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
font_name = os.path.join("font.ttf")
font1 = pygame.font.Font(font_name, 25)
font2 = pygame.font.Font(font_name, 64)
font3 = pygame.font.Font(font_name, 40)

# 創建遊戲物件
all_sprites = pygame.sprite.Group()
all_sprites2 = pygame.sprite.Group()

farm = Farm()
pond = Pond()
shop = Shop()
land = Land()
feed = Feed()
farm_system = FarmSystem()

lantern = Lantern(of_lantern)
streetlight = StreetLight(of_streetlight)
player = Player(screen, lantern)
economy = EconomySystem(inventory)
all_sprites2.add(farm, pond, shop, land, feed, streetlight, player, lantern)

light = LightSystem()
sugarpath = SugarPath(light, decay_rate)

granules = pygame.sprite.Group()
for granule in range(granules_number):
    granule = Granule()
    granules.add(granule)
    all_sprites.add(granule)
#wishes = [Wish() for i in range(wish_number)] 測試用
wishes = [Wish(x, y, check_see_wish) for x, y in zip([365, 700, 1300], [655, 255, 500])]
light.wish_list += wishes
all_sprites.add(wishes)

running = True
game_state = "start1"
press_space = False
while running:
    if game_state == "start1":
        screen.fill(BLACK)
        UI.start1UI (screen, font2, font1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = "game over"
                running = False
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE:
                    game_state = "start2"

        pygame.display.update()
        continue

    if game_state == "start2":
        screen.fill(BLACK)
        UI.start2UI (screen, font1)
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = "game over"
                running = False
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE:
                    game_state = "start3"

        pygame.display.update()
        continue

    if game_state == "start3":
        screen.fill(BLACK)
        UI.start3UI (screen, font3, font1)
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = "game over"
                running = False
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE:
                    game_state = "playing"

        pygame.display.update()
        continue
    
    clock.tick(FPS)
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: 
            # 黑暗區  
            if event.key == pygame.K_z:
                temp = 0
                temp = GranulesCount.collect_granules(player, granules, player_radius, all_sprites, Granule, record, of_lantern["turn_on"])
                if (temp is not None) and (temp > 1):
                    texta = "收集到" + str(temp) +"顆糖粒"
                    text_time = time.time()
                    text1 = ""
                    text2 = ""
                    text3 = ""
                    text4 = ""
            elif event.key == pygame.K_x:
                if WishCount.collect_wishes(player, wishes, player_radius, record):
                    texta = "成功點亮願望"
                    text_time = time.time()
            elif event.key == pygame.K_SPACE:
                press_space = True
                sugarpath.start_new_trail(record)    
            elif event.key == pygame.K_c:
                of_lantern["turn_on"] = not of_lantern["turn_on"]
            elif event.key == pygame.K_v:
                of_streetlight["turn_on"] = not of_streetlight["turn_on"]
                streetlight.status()
            
            # 農場區
            if player.rect.colliderect(land.rect) and pygame.key.get_pressed()[pygame.K_s]:
                if inventory["seed"] > 0:
                    farm_system.plant_crop('wheat')
                    inventory['seed'] -= 1
                    print("已種下一顆小麥種子")
                    text2 = "已種下一顆小麥種子"
                    text_time = time.time()
                else:
                    print("沒有種子！")
                    text2 = "沒有種子！"
                    text_time = time.time()
                    
            elif player.rect.colliderect(pond.rect) and pygame.key.get_pressed()[pygame.K_s]:
                farm_system.start_fishing() # 執行釣魚邏輯在遊戲更新
                
            elif pygame.key.get_pressed()[pygame.K_a]:
                harvested = farm_system.take_products()
                for item in harvested:
                    if item == 'wheat' and player.rect.colliderect(land.rect):
                        inventory["wheat"] += 1
                        print(f"收成了 {item}")
                        text2 = "收成了小麥"
                        text_time = time.time()
                    elif item == 'egg' and player.rect.colliderect(feed.rect):
                        inventory["egg"] += 1
                        print(f"收成了 {item}")
                        text3 = "收成了蛋"
                        text_time = time.time()
                    elif item == 'fish' and player.rect.colliderect(pond.rect):
                        inventory["fish"] += 1
                        print(f"收成了 {item}")
                        text1 = "收成了魚"
                        text_time = time.time()
                        
            elif player.rect.colliderect(shop.rect):
                if pygame.key.get_pressed()[pygame.K_q]:
                    if economy.buy('seed', 1):
                        #inventory['seed'] += 1
                        text4= "金幣-1 成功購買一粒種子"
                        text_time = time.time()
                    else:
                        text4= "錢不夠買種子"
                        text_time = time.time()
                
                elif pygame.key.get_pressed()[pygame.K_w]:
                    if economy.buy('oil', 1):
                        if record['oil'] <= 10000:
                            record['oil'] = min(record['oil']+ 10, 10000)
                            text4 = "金幣-10 補充10滴燈油"
                            text_time = time.time()
                        else:
                            text4 = "燈油已滿"
                            text_time = time.time()
                    else:
                        text4 = "錢不夠買燈油"
                        text_time = time.time()
                        
                elif pygame.key.get_pressed()[pygame.K_e]:
                    if economy.sell('wheat', 1):
                        #inventory['money'] += 3
                        text4 = "金幣+3 賣出小麥"
                        text_time = time.time()
                    else:
                        text4 = "沒有小麥可賣"
                        text_time = time.time()
                        
                elif pygame.key.get_pressed()[pygame.K_r]:
                    if economy.sell('egg', 1):
                        #inventory['money'] += 1
                        text4 = "金幣+1 賣出雞蛋"
                        text_time = time.time()
                    else:
                        text4 = "沒有雞蛋可賣"
                        text_time = time.time()
                        
                elif pygame.key.get_pressed()[pygame.K_t]:
                    if economy.sell('fish', 1):
                        #inventory['money'] += 10
                        text4 = "金幣+10 賣出魚"
                        text_time = time.time()
                    else:
                        text4 = "沒有魚可賣"
                        text_time = time.time()
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                press_space = False
                sugarpath.stop_trail()
                
    # 更新遊戲 黑暗區
    if record["oil"] > 0:
        of_lantern["have_oil"] = True
    else :
        of_lantern["have_oil"] = False
        
    all_sprites.update() # granules wishes
    all_sprites2.update() # player
    light.update(player.rect, of_lantern["have_oil"], record, of_lantern["turn_on"], of_streetlight)

    if record["granules_count"] <= 0:
        press_space = False
    if press_space:
        sugarpath.add_trail_point(record, player.rect.center)
    if check_see_wish[0] == True:
        texta = "看見願望瓶"
        check_see_wish[0] = False
    # 更新遊戲 農場區
    farm_system.update_growth(ticks=1)
    farm_system.update_animal_products()
    
    fishing_result = farm_system.check_fishing_result(player.rect, pond.rect)
    if fishing_result == 'fish':
        print("釣到魚！")
        text1 = "釣到魚！"
        text_time = time.time()
    elif fishing_result == -1:
        print("沒釣到！")
        text1 = "沒釣到！"
        text_time = time.time()
        
    for text in [text1, text2, text3, text4]:
        if text != "":
            texta = ""
            break
    
    if time.time() - text_time >= 3:
        text1 = ""
        text2 = ""
        text3 = ""
        text4 = ""
        texta = ""
        text_time = time.time()
        
    # 畫面顯示
    screen.fill(BLACK)

    # 顯示遊戲畫面
    sugarpath.draw(screen)
    all_sprites.draw(screen)
    light.draw(screen)

    # 顯示文字
    UI.worldUI(screen, font1, record, Wish.get_total_count())
    UI.farmUI (screen, font1, inventory, player, farm)
    UI.textUI (screen, font1, player, feed, land, pond, shop, text1, text2, text3, text4, texta)

    # 顯示玩家
    all_sprites2.draw(screen)

    #測試用
    #all_sprites.draw(screen)
    # Debug
    #print(harvested)
    
    pygame.display.update()

pygame.quit()
