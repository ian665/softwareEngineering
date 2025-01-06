import pygame
from menu import MainMenu

def main():
    # 初始化 Pygame
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("哥布林遊戲測試")

    # 初始化主選單
    main_menu = MainMenu(screen)
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # 將事件傳遞給主選單進行處理
            main_menu.handle_event(event)

        # 根據當前頁面繪製畫面
        main_menu.render()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
