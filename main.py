import pygame

# 初始化 Pygame
pygame.init()

# 設置窗口
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("玩家與 NPC 戰鬥遊戲")