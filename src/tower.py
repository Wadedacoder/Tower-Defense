import pygame

#pls = Tower(test, 10, 500, (50,50) , (60,60) , (200,200))
class Tower:
    def __init__(self, name, damage, attack_speed, size: pygame.Vector2, dmg_range: pygame.Vector2 , location: pygame.Vector2) -> None:
        self.name = name
        self.damage = damage
        self.attack_speed = attack_speed
        '''Represent time(in ms) between attack'''
        # self.sprite = sprite
        self.location = location
        self.size = pygame.Rect(self.location.x - size.x , self.location.y - size.y , 2 * size.x,  2 * size.y)
        #self.attack_range=dmg_range
        self.dmg_range = pygame.Rect(self.location.x - dmg_range.x, self.location.y - dmg_range.y , 2 * dmg_range.x,  2 * dmg_range.y)
        self.initial_time = pygame.time.get_ticks()

    def balloon_scanner(self, balloons):
        '''Checks for the balloons in the range, assuming balloons are point-sized'''
        for balloon in balloons:
            if self.dmg_range.collidepoint(balloon.location):
                self.reduce_hp(balloon)
                return
    
    def reduce_hp(self, balloon):
        balloon.reduce_hp(self.damage)

    def draw(self, window):
        # pygame.draw.rect(window,[0,0,255], self.dmg_range)
        pygame.draw.rect(window,[255,0,1], self.size)
    
    def update(self,balloons):
        if (pygame.time.get_ticks() - self.initial_time) % self.attack_speed == 0:
            self.balloon_scanner(balloons)    
        else:
            pass

