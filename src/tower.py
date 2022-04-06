import pygame
import balloon

class Tower:
    def __init__(self, name, damage, attack_speed, size: pygame.Vector2, sprite, dmg_range: pygame.Vector2 , location: pygame.Vector2) -> None:
        self.name = name
        self.damage = damage
        self.attack_speed = attack_speed
        # self.sprite = sprite
        self.size = pygame.Rect(self.location.x - size.x, self.location.y + size.y, 2 * size.x,  2 * size.y)
        self.location = location
        self.dmg_range = pygame.Rect(self.location.x - dmg_range.x, self.location.y + dmg_range.y, 2 * dmg_range.x,  2 * dmg_range.y)
        self.is_placed = False

    def get_placed(self):
        self.is_placed = True

    def placement_checker(self, rectangles):
        '''Returns false if the tower is not colliding with anything'''
        return any(i.colliderect(self.size) for i in rectangles)

    def ballon_scanner(self, balloons):
        '''Checks for the balloons in the range, assuming balloons are point-sized'''
        for i in balloons:
            if self.dmg_range.collidepoint(balloons.location):
                pass
    
    def reduce_hp(self, balloon: balloon):
        balloon.reduce_hp(self.damage)
