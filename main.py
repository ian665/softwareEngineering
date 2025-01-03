import pygame
from player import Player
from npc import NPC
from map import Map
import random

pygame.init()

#設定視窗大小
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("哥布林小隊")


font = pygame.font.Font("C:/Windows/Fonts/msyh.ttc", 25)  #微軟正黑體

def show_rules():
    screen.fill((0, 0, 0))

    rules = [
        "歡迎來到哥布林小隊遊戲",
        "",
        "遊戲規則如下:",
        "",
        "規則1:透過WASD或上下左右控制玩家角色移動(輸入法需要為英文)",
        "規則2:透過移動到哥布林的位置進行對話說服或是將目標殺死獲得獎勵",
        "規則3:按下B查看獲得的資源以及經驗值",
        "",
        "--按下Enter進入遊戲--"
    ]

    y = 150
    for rule in rules:
        text = font.render(rule, True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y))
        screen.blit(text, text_rect)
        y += 50

    pygame.display.flip()

def generate_npcs(num_npcs, player_position):
    return [NPC(SCREEN_WIDTH, SCREEN_HEIGHT, player_position) for _ in range(num_npcs)]

def main():
    clock = pygame.time.Clock()
    running = True
    game_started = False  #判斷是否進入遊戲

    player = Player()
    game_map = Map(SCREEN_WIDTH, SCREEN_HEIGHT)

    #初始化NPC
    npcs = generate_npcs(random.randint(2, 8), (player.x, player.y))

    #啟用按鍵重複
    pygame.key.set_repeat(1, 50)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not game_started:  #顯示遊戲規則
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    game_started = True
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_UP, pygame.K_w):  #向上
                        player.move(0, -10)
                    elif event.key in (pygame.K_DOWN, pygame.K_s):  #向下
                        player.move(0, 10)
                    elif event.key in (pygame.K_LEFT, pygame.K_a):  #向左
                        player.move(-10, 0)
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):  #向右
                        player.move(10, 0)

        if not game_started:
            show_rules()
        else:
            #確保玩家不移出邊界
            player.x = max(0, min(SCREEN_WIDTH - 110, player.x))
            player.y = max(0, min(SCREEN_HEIGHT - 110, player.y))

            #檢測玩家是否與NPC碰撞
            npcs = [npc for npc in npcs if not npc.check_collision((player.x, player.y))]

            #所有NPC消失就重新隨機生成
            if not npcs:
                npcs = generate_npcs(random.randint(2, 8), (player.x, player.y))

            #更新與繪製遊戲畫面
            game_map.draw(screen)
            player.draw(screen)
            for npc in npcs:
                npc.draw(screen)


            pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
