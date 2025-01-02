import pygame

class Map:
    def __init__(self):
        self.background = pygame.image.load("softwareEngineering/assets/images/map.png")
        self.player_position = [100, 100]

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

    def handle_movement(self, key):
        if key == pygame.K_UP:
            self.player_position[1] -= 10
        elif key == pygame.K_DOWN:
            self.player_position[1] += 10
        elif key == pygame.K_LEFT:
            self.player_position[0] -= 10
        elif key == pygame.K_RIGHT:
            self.player_position[0] += 10
