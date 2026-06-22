# economy.py

class EconomySystem:
    def __init__(self, inventory):
        self.inventory = inventory  # 背包

        self.shop_items = {
            'lantern': 20,
            'oil': 10,
            'seed': 1
        }

        self.sell_prices = {
            'wheat': 3,
            'fish': 10,
            'egg': 1
        }

        # 預設所有物品在背包中數量為 0
        for item in list(self.shop_items.keys()) + list(self.sell_prices.keys()):
            if item not in self.inventory:
                self.inventory[item] = 0

    def buy(self, item_name, count):
        if item_name in self.shop_items:
            price = self.shop_items[item_name] * count
            if self.inventory["money"] >= price:
                self.inventory["money"] -= price
                # 背包一定有該品項，初始化已保證
                self.inventory[item_name] += count
                return True
        return False

    def sell(self, product_name, count):
        # 確認物品存在於價格表，並且玩家背包內數量足夠
        if product_name not in self.sell_prices:
            return 0  # 商品不在可販售列表中
        if self.inventory[product_name] < count:
            return 0  # 玩家庫存不足

        # 開始販售
        price_per_item = self.sell_prices[product_name]
        total = price_per_item * count
        self.inventory[product_name] -= count
        self.inventory["money"] += total
        return total
