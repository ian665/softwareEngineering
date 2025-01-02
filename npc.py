import pygame

class NPC:
    def __init__(self):
        self.x, self.y = 300, 300
        self.image = pygame.image.load("softwareEngineering/assets/images/npc.png")

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
