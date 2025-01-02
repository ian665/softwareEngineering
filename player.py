import pygame

class Player:
    def __init__(self):
        self.x, self.y = 100, 100
        self.image = pygame.image.load("softwareEngineering/assets/images/player.png")

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
