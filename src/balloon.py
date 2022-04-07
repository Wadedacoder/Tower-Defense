import pygame

class Balloon:
    def __init__(self, name: str, hp: int, speed: float, location):
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
        self.location = location
        self.isAlive = True

    def has_crossed_end(self):
        """Return true if this balloon has crossed the finish line of the path."""
        pass

    def die(self):
        """Change balloon's life status to dead."""
        self.isAlive = False

    def reduce_hp(self, value: float):
        """Reduce balloon hp by the passed value."""
        if value >= self.hp:
            self.hp = 0
        else:
            self.hp = round(self.hp - value)
        assert self.hp >= 0

    def move(self, end_vector):
        """Move the balloon's location by vector"""
        magn = (self.location + end_vector)
        print("magn is", self.location)
        print(magn.length())
        self.location.x += self.speed * (end_vector.x - self.location.x) / magn.magnitude()

    def update_location(self, new_location):
        self.location = new_location
    
    def draw(self, window):
        # self.location = path.start
        pygame.draw.rect(window,(255, 255, 255), pygame.Rect(self.location.x, self.location.y, 10, 10))