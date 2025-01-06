import pygame
import time
class MainMenu:
  def __init__(self, screen):
    self.screen = screen
    self.options = ["開始遊戲", "設置", "退出遊戲"]  
    self.selected_option = -1
    self.font = pygame.font.Font("C:/Windows/Fonts/msyh.ttc", 25) 
    self.current_page = "menu"
    self.volume = 50
    self.save_slots = [None, None, None, None, None]
    self.selected_slot = 0
    self.last_key_time, self.key_cooldown = 0, 0.2 #防止多重輸入
    
  def time_str_to_seconds(self, time_str):  # 將 "hh:mm:ss" 轉換為秒數
    parts = time_str.split(":")
    while len(parts) < 3:
      parts.insert(0, "0")
    hours, minutes, seconds = map(int, parts)
    return hours * 3600 + minutes * 60 + seconds
  
  def format_time(self, seconds):#將秒數格式化為 hh:mm:ss
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"


  def render(self):
    if self.current_page == "menu":
      self.render_menu()
    elif self.current_page == "settings":
      self.render_settings()
    elif self.current_page == "save_slots":
      self.render_save_slots()
  
  def render_menu(self):
    self.screen.fill((0, 0, 0))  
    title_text = self.font.render("哥布林遊戲主選單", True, (255, 255, 255))
    self.screen.blit(title_text, (400 - title_text.get_width() // 2, 100))
    for i, option in enumerate(self.options):
      if self.selected_option == -1:
        color = (255, 255, 255)
      else:
        color = (255, 255, 0) if i == self.selected_option else (255, 255, 255)
      option_text = self.font.render(option, True, color)
      self.screen.blit(option_text, (400 - option_text.get_width() // 2, 200 + i * 50))

    pygame.display.flip() 

  def render_save_slots(self):
    self.screen.fill((0, 0, 0))
    title_text = self.font.render("選擇存檔槽", True, (255, 255, 255))
    self.screen.blit(title_text, (400 - title_text.get_width() // 2, 50))
    for i in range(5):
      y = 150 + i * 70
      if i == self.selected_slot:
        pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect(90, y-10, 620, 60), 3)
      if self.save_slots[i] is None:
        slot_text = self.font.render(f"槽 {i + 1}: 新遊戲", True, (255, 255, 255))
      else:
        time_played = self.format_time(self.time_str_to_seconds(self.save_slots[i]))
        slot_text = self.font.render(f"槽 {i + 1}: {time_played}", True, (255, 255, 255))
        delete_text = self.font.render("刪除", True, (255, 255, 0))
        delete_button = pygame.Rect(600, y, 80, 40)
        pygame.draw.rect(self.screen, (255, 0, 0), delete_button)
        self.screen.blit(delete_text, (610+5, y-1))
      self.screen.blit(slot_text, (100, y))
    back_text = self.font.render("按 ESC 返回主選單", True, (255, 255, 255))
    self.screen.blit(back_text, (400 - back_text.get_width() // 2, 500))
    pygame.display.flip()

  def render_settings(self):
    self.screen.fill((0, 0, 0))
    title_text = self.font.render("設置", True, (255, 255, 255))
    self.screen.blit(title_text, (400 - title_text.get_width()//2, 100))
    volumn_text = self.font.render(f"音量: {self.volume}", True, (255, 255, 255))
    self.screen.blit(volumn_text, (400 - volumn_text.get_width()//2, 200))
    self.decrease_button = pygame.Rect(300, 300, 200, 50)
    self.increase_button = pygame.Rect(450, 300, 200, 50)
    prompt_text = self.font.render("← 減少音量   → 增加音量", True, (255, 255, 255))
    self.screen.blit(prompt_text, (400 - prompt_text.get_width()//2, 300))
    back_text = self.font.render("按下esc返回", True, True, (255, 255, 255))
    self.screen.blit(back_text, (400 - back_text.get_width()//2, 400))
    pygame.display.flip()
  
  def handle_event(self, event):
    if self.current_page == "menu":
      self.handle_menu_event(event)
    elif self.current_page == "settings":
      self.handle_settings_event(event) 
    elif self.current_page == "save_slots":
      return self.handle_save_slots_event(event)
  
  def handle_menu_event(self, event):
    if event.type == pygame.KEYDOWN:
      if time.time() - self.last_key_time > self.key_cooldown:
        self.last_key_time = time.time()
        if event.key == pygame.K_UP:
            self.selected_option = (self.selected_option - 1) % len(self.options)
        elif event.key == pygame.K_DOWN: 
            self.selected_option = (self.selected_option + 1) % len(self.options)
        elif event.key == pygame.K_RETURN:
          if self.selected_option == 0:
            self.current_page = "save_slots"
          elif self.selected_option == 1:
            self.current_page = "settings"
          elif self.selected_option == 2:
            pygame.quit()
            exit()
        
  def handle_settings_event(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
      if self.increase_button.collidepoint(event.pos):
        self.volume = min(100, self.volume + 10)
      elif self.decrease_button.collidepoint(event.pos):
        self.volume = max(0, self.volume - 10)
      else:
        self.current_page = "menu"
    if event.type == pygame.KEYDOWN:
      if time.time() - self.last_key_time > self.key_cooldown:
        self.last_key_time = time.time()
        if event.key == pygame.K_LEFT:  
          self.volume = max(0, self.volume - 10)
        elif event.key == pygame.K_RIGHT: 
          self.volume = min(100, self.volume + 10)
        elif event.key == pygame.K_ESCAPE:
          self.current_page = "menu"
        
  def handle_save_slots_event(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_pos = event.pos
      for i in range(5):
        y = 150 + i * 70
        delete_button = pygame.Rect(600, y, 80, 40)
        if delete_button.collidepoint(mouse_pos):
          self.save_slots[i] = None 
          print(f"槽 {i + 1} 的存檔已刪除")
          return
        slot_area = pygame.Rect(100, y, 400, 40)
        if slot_area.collidepoint(mouse_pos):
          if self.save_slots[i] is None:
            print(f"開始新遊戲，槽 {i + 1}")
            self.save_slots[i] = "00:00:00"
          else:
            print(f"繼續遊戲，槽 {i + 1}，遊戲時間：{self.save_slots[i]}")
          return 1
    if event.type == pygame.KEYDOWN:
      if time.time() - self.last_key_time > self.key_cooldown:
        self.last_key_time = time.time()
        if event.key == pygame.K_UP:
          self.selected_slot = (self.selected_slot - 1) % 5
        elif event.key == pygame.K_DOWN:
          self.selected_slot = (self.selected_slot + 1) % 5
        elif event.key == pygame.K_RETURN:
          if self.save_slots[self.selected_slot] is None:
            self.save_slots[self.selected_slot] = "00:00:00"
          else:
            return 1
          pygame.event.clear()
        if event.key == pygame.K_ESCAPE:
          self.current_page = "menu"

        