# Collection.py
import math

granules_number = 500

class GranulesCount:
    @staticmethod  
    def collect_granules(player, granules, player_radius, all_sprites, granule_class, record, of_lantern_turn_on):
        if of_lantern_turn_on:
            distance = lambda g: math.sqrt((player.rect.centerx - granule.rect.centerx) ** 2 +\
                                           (player.rect.centery - granule.rect.centery) ** 2)
            
            temp = 0
            for granule in granules.copy():
                if distance(granule) < player_radius + 15:
                    temp +=1
                    granule.kill()
                    record["granules_count"] += 1
                    record["happiness"] += 1 
                    #print(f"已收集糖粒數: {int(self.granules_count)}")
                
                if len(granules) == 0:
                    GranulesCount.produce_granules(granules, all_sprites, granule_class)
            if temp >=1:
                return temp

    @staticmethod
    def produce_granules(granules, all_sprites, granule_class):
        for granule in range(granules_number):
            new_granule = granule_class()
            granules.add(new_granule)
            all_sprites.add(new_granule)
            #print("糖粒已重新生成 500 顆！")
       
class WishCount:
    @staticmethod
    def collect_wishes(player, wishes, player_radius, record):
        distance = lambda w: math.sqrt((player.rect.centerx - wish.rect.centerx) ** 2 + (player.rect.centery - wish.rect.centery) ** 2)
        
        for wish in wishes.copy():
            if wish.is_seen and wish.is_not_collected:
                if distance(wish) < player_radius + 15:
                    #wish.is_illuminate = True
                    wish.is_not_collected = False
                    wish.illuminate()
                    record["wishes_count"] += 1
                    return True
                    #print(f"已收集願望數: {int(self.wishes_count)}")