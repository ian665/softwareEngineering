import pygame

class Inventory:
    def __init__(self):
        self.experience = 0  #經驗值
        self.level = 1  #初始等級
        self.rewards = {"獎勵A": 0, "獎勵B": 0, "獎勵C": 0}  #獎勵

    def add_experience(self, amount):
        self.experience += amount
        self.check_level_up()

    def check_level_up(self):
        required_experience = 100 + (self.level - 1) * 50  #升級所需經驗
        while self.experience >= required_experience:
            self.experience -= required_experience  #扣除對應經驗值
            self.level += 1  #升級
            required_experience = 100 + (self.level - 1) * 50  #更新下一階所需經驗

    def add_reward(self, reward_name):
        if reward_name in self.rewards:
            self.rewards[reward_name] += 1

    def show_inventory(self, screen, font):
        screen.fill((0, 0, 0))
        inventory_text = [
            f"等級: {self.level}",
            f"經驗值: {self.experience}",
            f"獎勵A: {self.rewards['獎勵A']}",
            f"獎勵B: {self.rewards['獎勵B']}",
            f"獎勵C: {self.rewards['獎勵C']}",
            "",
            "-- 按下ESC返回遊戲 --"
        ]
        y = 150
        for line in inventory_text:
            text = font.render(line, True, (255, 255, 255))
            text_rect = text.get_rect(center=(800 // 2, y))
            screen.blit(text, text_rect)
            y += 50
        pygame.display.flip()
