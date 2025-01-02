import pygame
from player import Player
from npc import NPC
from map import Map


pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("玩家與 NPC 戰鬥遊戲")

# 主遊戲循環
def main():
    clock = pygame.time.Clock()
    running = True

    player = Player()
    npc = NPC()
    game_map = Map()

    while running:
        screen.fill((0, 0, 0))  # 填充背景色
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                game_map.handle_movement(event.key)

        # 更新與繪製
        game_map.draw(screen)
        player.draw(screen)
        npc.draw(screen)

        pygame.display.flip()
        clock.tick(60)  #限制 FPS

    pygame.quit()

if __name__ == "__main__":
    main()