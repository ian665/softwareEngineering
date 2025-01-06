import pygame
from player import Player
from npc import NPC
from map import Map
from inventory import Inventory
from battle_system import BattleSystem
from menu import MainMenu
import random
import time
import story

pygame.init()

#設定視窗大小
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("哥布林小隊")


font = pygame.font.Font("C:/Windows/Fonts/msyh.ttc", 25)  #微軟正黑體

def generate_npcs(num_npcs, player_position):
    return [NPC(SCREEN_WIDTH, SCREEN_HEIGHT, player_position) for _ in range(num_npcs)]

def main():
    clock = pygame.time.Clock()
    running = True
    game_started = False  #判斷是否進入遊戲
    inventory_open = False  #資源畫面是否打開
    message_displaying = False  #是否正在顯示訊息
    player = Player()
    start_time = 0
    end_time = 0
    elapsed_time = 0
    main_menu = MainMenu(screen)
    game_map = Map(SCREEN_WIDTH, SCREEN_HEIGHT)
    inventory = Inventory()
    battle_system = BattleSystem(inventory)
    npcs = []
    #啟用按鍵重複
    pygame.key.set_repeat(1, 50)
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          if game_started:
            end_time = time.time()
            elapsed_time += end_time - start_time
            print(f"總遊戲時間: {elapsed_time:.0f} 秒")
            if main_menu.save_slots[main_menu.selected_slot] is not None:
              main_menu.save_slots[main_menu.selected_slot] += elapsed_time
            else:
              main_menu.save_slots[main_menu.selected_slot] = elapsed_time
        if not game_started:
          result = main_menu.handle_event(event)
          if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            if result == 1:
              if main_menu.time_str_to_seconds(main_menu.save_slots[main_menu.selected_slot]) == 0:
                story.show_story(screen, font, SCREEN_WIDTH, SCREEN_HEIGHT)#沒有遊戲存檔要進入劇情
              game_started = True
              start_time = time.time()
              npcs = generate_npcs(random.randint(2, 8), (player.x, player.y))
              elapsed_time = 0
        if game_started:
          if inventory_open:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
              inventory_open = False
              pygame.key.set_repeat(1, 50) #啟用按鍵重複
          elif message_displaying:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                message_displaying = False
                pygame.key.set_repeat(1, 50)  #啟用按鍵重複
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
                  elif event.key == pygame.K_b:  #打開資源畫面
                      inventory_open = True
                      pygame.key.set_repeat(0)  #禁用按鍵重複
                  elif event.key == pygame.K_ESCAPE:
                    game_started = False
                    inventory_open = False
                    message_displaying = False
                    pygame.key.set_repeat(0)  # 禁用按鍵重複
                    main_menu.current_page = "menu"  # 切換到主選單頁面 
                    end_time = time.time()
                    elapsed_time += end_time - start_time
                    print(f"總遊戲時間: {elapsed_time:.0f} 秒")
                    if main_menu.save_slots[main_menu.selected_slot] is not None:
                      current_time_in_seconds = main_menu.time_str_to_seconds(main_menu.save_slots[main_menu.selected_slot])
                      updated_time_in_seconds = current_time_in_seconds + int(elapsed_time)
                      main_menu.save_slots[main_menu.selected_slot] = main_menu.format_time(updated_time_in_seconds)
                    else:
                      main_menu.save_slots[main_menu.selected_slot] = main_menu.format_time(int(elapsed_time))

      if not game_started:
        main_menu.render()
      elif inventory_open:
        inventory.show_inventory(screen, font)
      elif message_displaying:
        pygame.key.set_repeat(0)  #禁用按鍵重複
      else:
        #玩家不移出邊界
        player.x = max(0, min(SCREEN_WIDTH - 110, player.x))
        player.y = max(0, min(SCREEN_HEIGHT - 110, player.y))

        remaining_npcs = []
        for npc in npcs:
            if npc.check_collision((player.x, player.y)):  #碰撞檢測
              message_displaying = battle_system.initiate_battle(screen, font)  #戰鬥
              pygame.key.set_repeat(0)  # 禁用按鍵重複並進入訊息顯示模式
            else:
                remaining_npcs.append(npc)
        npcs = remaining_npcs

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
