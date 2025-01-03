import os
import pygame

class NPC:
    def __init__(self):
        # 獲取當前腳本所在目錄
        base_dir = os.path.dirname(os.path.abspath(__file__))  
        # 將目錄與檔案名結合
        file_path = os.path.join(base_dir, "./assets/images/npc.png")
        
        # 確認檔案是否存在
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # 載入圖片
        self.image = pygame.image.load(file_path)

# 測試 NPC 類別
if __name__ == "__main__":
    pygame.init()
    npc = NPC()
    print("NPC image loaded successfully!")
