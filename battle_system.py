import pygame
import random

class BattleSystem:
    def __init__(self, inventory):
        self.inventory = inventory

    def display_message(self, screen, font, messages):
        screen.fill((0, 0, 0))
        y = 200
        for message in messages:
            text = font.render(message, True, (255, 255, 255))
            text_rect = text.get_rect(center=(800 // 2, y))
            screen.blit(text, text_rect)
            y += 50
        pygame.display.flip()

        
        pygame.key.set_repeat(0) #禁用按鍵重複避免多次觸發
        

        #等待按下Enter
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    waiting = False
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

        
        pygame.key.set_repeat(1, 50) #確保回到主遊戲邏輯後按鍵模式正常

    def random_rewards(self):
        rewards = []
        if random.choice([True, False]):
            rewards.append("獎勵A")
        if random.choice([True, False]):
            rewards.append("獎勵B")
        if random.choice([True, False]):
            rewards.append("獎勵C")
        return rewards

    def add_rewards_to_inventory(self, rewards):
        for reward in rewards:
            self.inventory.add_reward(reward)

    def initiate_battle(self, screen, font):
        screen.fill((0, 0, 0))

        #戰鬥選項與對話
        options = [
            "哥布林 : 冒險者納命來!想奪取寶物就先過我這關!",
            "1. 嘗試說服他",
            "2. 將他痛扁一頓"
        ]

        y = 200
        for option in options:
            text = font.render(option, True, (255, 255, 255))
            text_rect = text.get_rect(center=(800 // 2, y))
            screen.blit(text, text_rect)
            y += 50
        pygame.display.flip()

        pygame.key.set_repeat(0) #禁用按鍵重複避免多次觸發
        

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:  #選擇說服
                        persuade_success = random.randint(20, 60) >= random.randint(0, 100)
                        if persuade_success:
                            rewards = self.random_rewards()
                            self.add_rewards_to_inventory(rewards)
                            self.inventory.add_experience(50)
                            self.display_message(screen, font, ["說服成功！", "--按下Enter繼續--"])
                            self.display_rewards(screen, font, rewards)
                            return True  #NPC消失
                        else:
                            self.display_message(screen, font, ["說服失敗，進入戰鬥", "--按下Enter繼續--"])
                            return self.fight(screen, font)
                    elif event.key == pygame.K_2:  #選擇戰鬥
                        return self.fight(screen, font)
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

        pygame.key.set_repeat(1, 50) #確保回到主遊戲邏輯後按鍵模式正常

    def fight(self, screen, font):
        rewards = self.random_rewards()
        self.add_rewards_to_inventory(rewards)
        self.inventory.add_experience(50)
        self.display_message(screen, font, ["戰鬥結束！", "--按下Enter繼續--"])
        self.display_rewards(screen, font, rewards)
        return True  #NPC消失

        

    def display_rewards(self, screen, font, rewards):
        messages = ["你獲得了以下獎勵:"]
        if rewards:
            messages.append("經驗值+50")
            messages.extend(rewards)
        else:
            messages.append("經驗值+50")
        messages.append("--按下Enter退出--")
        messages.append("--回到遊戲畫面後再次按下Enter以繼續--")
        self.display_message(screen, font, messages)
