import pygame

class Player:
    def __init__(self):
        self.x, self.y = 50, 50
        try:
            self.image = pygame.image.load("softwareEngineering/assets/images/player.png")
            self.image = pygame.transform.scale(self.image, (110, 110))
        except pygame.error as e:
            print(f"Error loading player image: {e}")
            exit()

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        print(f"Player position updated to: ({self.x}, {self.y})")

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
