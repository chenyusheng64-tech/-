# UI.py
import pygame

WHITE = (255, 255, 255)
BLUE = (152, 245, 255)
WIDTH = 1500
HEIGHT = 750

class UI:
    @staticmethod
    def start1UI (screen, font2, font1):
        # 糖粒之願
        text1, text2, text3 = font2.render("糖粒", True, WHITE), font2.render("之", True, BLUE), font2.render("願", True, WHITE)
        total_width = text1.get_width() + text2.get_width() + text3.get_width()
        x = WIDTH/2 - total_width/2
        y = HEIGHT/2
        screen.blit(text1, (x, y))
        x += text1.get_width()
        screen.blit(text2, (x, y))
        x += text2.get_width()
        screen.blit(text3, (x, y))
        # 內文
        text_surface1 = font1.render("致楓玥", True, WHITE)
        screen.blit(text_surface1, (WIDTH/2 - text_surface1.get_width()/2, HEIGHT/2 + 160))
        text_surface2 = font1.render("點擊 [SPACE] 開始遊戲", True, WHITE)
        screen.blit(text_surface2, (WIDTH/2 - text_surface2.get_width()/2, 680)) # HEIGHT/2 + 220

    @staticmethod
    def start2UI(screen, font1):

        lines = [
            "這個世界沒有太陽，沒有星光。",
            "黑暗覆蓋著一切，而你僅擁有一座微弱燈火照亮的小小農場......",
            "但請記住——",
            "",
            "時間就是會一點點加熱著你白糖顆粒般微小的願望，",
            "將它們融化成糖漿，流淌向最適合你的那條道路。",
            "不需要變得很厲害，不需要取得什麼入場券。",
            "",
            "以後也盡力積攢自己的白糖顆粒，",
            "也為自己微小的幸福感到滿足吧。",
            "-楓玥"
        ]

        y_positions = [
            70,
            120,
            200,
            250,
            290,
            340,
            390,
            440,
            490,
            540,
            610
        ]

        for text, y in zip(lines, y_positions):
            text_surface = font1.render(text, True, WHITE)
            screen.blit(text_surface, (WIDTH/2 - text_surface.get_width()/2, y))

        text_surface8 = font1.render("點擊 [SPACE] 繼續遊戲", True, WHITE)
        screen.blit(text_surface8, (WIDTH/2 - text_surface8.get_width()/2, 680))

    @staticmethod
    def start3UI (screen, font3, font1):
        text_surface = font3.render("遊戲玩法", True, WHITE)
        screen.blit(text_surface, (WIDTH/2 - text_surface.get_width()/2, 200))
        text_surface1 = font1.render("[Z]-收集糖粒  [X]-收集願望  [C]-打開燈籠  [V]-打開路燈  [SPACE]-鋪設道路", True, WHITE)
        screen.blit(text_surface1, (WIDTH/2 - text_surface1.get_width()/2, HEIGHT/4 + 150))
        text_surface2 = font1.render("[A]-收成  [S]-釣魚/種植  [Q]-買種子  [W]-買燈油  [E]-賣小麥  [R]-賣雞蛋  [T]-賣魚", True, WHITE)
        screen.blit(text_surface2, (WIDTH/2 - text_surface2.get_width()/2, HEIGHT/4 + 225))
        text_surface4 = font1.render("[↑]-向上移動  [↓]-向下移動  [←]-向左移動  [→]-向右移動", True, WHITE)
        screen.blit(text_surface4, (WIDTH/2 - text_surface4.get_width()/2, HEIGHT/4 + 300))
        text_surface3 = font1.render("點擊 [SPACE] 繼續遊戲", True, WHITE)
        screen.blit(text_surface3, (WIDTH/2 - text_surface3.get_width()/2, 680)) # HEIGHT/4 + 310

    @staticmethod
    def worldUI (screen, font, record, wish_total_count):
        #happiness_text_surface = font.render(f"happiness: {record["happiness"]}", True, WHITE)
        #screen.blit(happiness_text_surface, (10, 10))
        granule_text_surface = font.render(f"糖粒×{int(record["granules_count"])}", True, WHITE)
        screen.blit(granule_text_surface, (10, 10))
        wish_text_surface = font.render(f"願望瓶-{int(record["wishes_count"])} / {wish_total_count}", True, WHITE)
        screen.blit(wish_text_surface, (10, 50))
        oil_text_surface = font.render(f"燈油×{int(record["oil"])}", True, WHITE)
        screen.blit(oil_text_surface, (10, 90))
        oil_text_surface = font.render(f"燈籠-普通的燈籠 Lv 0", True, WHITE)
        screen.blit(oil_text_surface, (10, 130))
            
    @staticmethod
    def farmUI (screen, font, inventory, player, farm):
        #if pygame.sprite.collide_rect(player, farm): # 考慮只在農場區顯示
        if True: # 考慮一直顯示
            money_text_surface = font.render(f"金幣×{int(inventory["money"])}", True, WHITE)
            screen.blit(money_text_surface, (10, 585))
            fish_text_surface = font.render(f"魚×{int(inventory["fish"])}", True, WHITE)
            screen.blit(fish_text_surface, (10, 625))
            wheat_text_surface = font.render(f"小麥×{int(inventory["wheat"])} / 種子×{int(inventory["seed"])}", True, WHITE)
            screen.blit(wheat_text_surface, (10, 665))
            egg_text_surface = font.render(f"蛋×{int(inventory["egg"])}", True, WHITE)
            screen.blit(egg_text_surface, (10, 705))
            
    @staticmethod
    def textUI (screen, font1, player, feed, land, pond, shop, text1, text2, text3, text4, texta):       
        if pygame.sprite.collide_rect(player, pond):
            text_text_surface = font1.render(text1, True, WHITE)
            screen.blit(text_text_surface, (WIDTH/2 - text_text_surface.get_width()/2, 705))
        if pygame.sprite.collide_rect(player, land):
            text_text_surface = font1.render(text2, True, WHITE)
            screen.blit(text_text_surface, (WIDTH/2 - text_text_surface.get_width()/2, 705))
        if pygame.sprite.collide_rect(player, feed):
            text_text_surface = font1.render(text3, True, WHITE)
            screen.blit(text_text_surface, (WIDTH/2 - text_text_surface.get_width()/2, 705))
        if pygame.sprite.collide_rect(player, shop):
            text_text_surface = font1.render(text4, True, WHITE)
            screen.blit(text_text_surface, (WIDTH/2 - text_text_surface.get_width()/2, 705))
        text_text_surface = font1.render(texta, True, WHITE)
        screen.blit(text_text_surface, (WIDTH/2 - text_text_surface.get_width()/2, 705))
    