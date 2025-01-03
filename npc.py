import pygame
import random

class NPC:
<<<<<<< Updated upstream
    def __init__(self, screen_width, screen_height, avoid_position):
        #隨機生成位置(不會再玩家目前位置)
        while True:
            self.x = random.randint(0, screen_width - 100)
            self.y = random.randint(0, screen_height - 100)
            if abs(self.x - avoid_position[0]) > 100 and abs(self.y - avoid_position[1]) > 100:
                break

        self.image = pygame.image.load("softwareEngineering/assets/images/npc.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
=======
    def __init__(self):
        self.x, self.y = 300, 300
        self.image = pygame.image.load("./assets/images/npc.png")
>>>>>>> Stashed changes

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def check_collision(self, player_position):
        px, py = player_position

        #檢查玩家與npc碰撞
        if abs(self.x - px) < 100 and abs(self.y - py) < 100:
            return True
        return False
