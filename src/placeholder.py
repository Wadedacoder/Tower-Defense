import pygame
class Placeholder:
    def __init__(self, location: pygame.Vector2, tower):
        self.location = location
        self.tower = tower
        self.rect = self.tower.size            


    def update(self, new_loc):
        self.location = new_loc
        self.tower.location = self.location
        self.rect = self.tower.size            

    def draw(self, window):
        pygame.draw.rect(window,[255,0,1], self.size)
