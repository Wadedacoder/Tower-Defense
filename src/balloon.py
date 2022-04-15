import pygame
from src.score import Score

class Balloon:
    def __init__(self, name: str, hp: int, speed: float, location, edge_num: int):
        """
        Args:
            name (string): type of balloon
            hp (int): initial health of balloon
            speed (float): speed of balloon
            location (pygame.Vector2): initialise the location of the balloon as a vector
        """
        self.name = name
        self.hp = hp
        self.speed = speed
        self.edge_num=edge_num
        self.location = location
        self.isAlive = True

    def has_collided(self, path, edge_num):
        """Return true if balloon has collided with a path edge"""
        if self.location.x >= path.edges[edge_num].x or self.location.y >= path.edges[edge_num].y:
            return True

    def has_crossed_end(self,end):
        """Return true if this balloon has crossed the finish line of the path."""
        return abs(self.location.x - end.x) <= 40 and abs(self.location.y - end.y) <= 40

    def die(self):
        """Change balloon's life status to dead."""
        self.isAlive = False
        Score.increment_score()
        del self
        # print(Score.get_score())

    def reduce_hp(self, value: float):
        """Reduce balloon hp by the passed value."""
        if value >= self.hp:
            self.hp = 0
        else:
            self.hp = round(self.hp - value)
        try:
            assert self.hp > 0
        except:
            self.die()

    def move(self, end_vector):
        """Move the balloon's location by vector"""
        magn = (self.location - end_vector) 
        # print("magn is", self.location)
        # print(magn.length())
        if end_vector.y==self.location.y:
            self.location.x += self.speed * (end_vector.x - self.location.x) / (magn.magnitude() + 1)
        else:
            self.location.y += self.speed * (end_vector.y - self.location.y) / (magn.magnitude() + 1)
        # self.location.x += self.speed


    def update_location(self, new_location):
        self.location = new_location
    
    def draw(self, window,end):
        # self.location = path.start
        if self.has_crossed_end(end):
            self.die()
        if self.isAlive:
            pygame.draw.rect(window,(255, 255, 255), pygame.Rect(self.location.x, self.location.y, 10, 10))