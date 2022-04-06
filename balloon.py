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
        pass