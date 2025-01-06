import pygame
import time

last_key_time, key_cooldown = 0, 0.2 #防止多重輸入

def show_story(screen, font, SCREEN_WIDTH, SCREEN_HEIGHT):
    # 劇情內容分頁
    pages = [
        [
            "",
            "",
            "",
            "本文產自GPT",
            "",
            "",
            "--按下Enter進入下一頁--"
        ],
        [
            "今天和高中同學為了躲雨跑進網咖，",
            "誰能想到隔壁居然上演了一場活春宮。",
            "",
            "操他媽，什麼人會在晚上七點跑來這種地方當摩鐵纏綿？",
            "明明是個打遊戲的地方，卻被搞得像是廉價情侶的秘密基地。",
            "",
            "--按下Enter進入下一頁--"
        ],
        [
            "我戴著耳機，卻無法完全屏蔽那斷斷續續的聲音，",
            "像針一樣戳進耳朵，帶著我根本無法處理的刺激與羞恥感。",
            "",
            "國中三年，別說牽手，甚至連和女生好好聊天的機會都屈指可數。",
            "到了高中，更是被徹底封印在男校的圍牆裡，",
            "每天只剩下課本和死氣沉沉的生活。",
            "",
            "--按下Enter進入下一頁--"
        ],
        [
            "隔壁的聲音帶來的衝擊，是我這輩子從未經歷過的現實打擊。",
            "看簧片的時候，那些聲音、畫面，不過是屏幕裡的虛擬影像，",
            "隔著一層冷冰冰的玻璃，沒什麼真實感。",
            "",
            "但現在，這是真正存在於我身邊的現實，隔著一堵牆，",
            "能清楚地聽見每一個喘息、每一個模糊的低語，",
            "",
            "--按下Enter進入下一頁--"
        ],
        [
            "真的好恨那些帥潮，彷彿他們天生就被允許擁有一切，而我什麼都沒有。",
            "聖誕節快到了，我知道那天大概和過去的每一天一樣，平淡無奇。",
            "",
            "但有那麼一瞬間，我真的好想好想，能過一次屬於自己的聖誕節，",
            "一個有炮打、有故事可說的聖誕節。",
            "可惜，我連走進那堵牆後的世界的資格都沒有，",
            "",
            "--按下Enter開始遊戲--"
        ],
        [
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
    ]
    page_index = 0
    global last_key_time, key_cooldown
    # 遍歷每一頁的內容
    while page_index < len(pages):
        screen.fill((0, 0, 0))  # 清空螢幕
        y = 150
        for line in pages[page_index]:
            text = font.render(line, True, (255, 255, 255))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y))
            screen.blit(text, text_rect)
            y += 50
        pygame.display.flip()

        # 等待玩家按下 Enter 鍵
        waiting = True
        while waiting:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              exit()
            if event.type == pygame.KEYDOWN:
              if time.time() - last_key_time > key_cooldown:
                last_key_time = time.time()
                if event.key == pygame.K_RETURN or event.key == pygame.K_RIGHT:  # 檢測 Enter 鍵
                  page_index += 1
                  waiting = False
                elif event.key == pygame.K_LEFT:  # 按下 ← 鍵回到上一頁
                  if page_index > 0:
                    page_index -= 1
                  waiting = False
