import pygame

class Path:
    def __init__(self,level,edges):
        self.level=level
        self.edges=[pygame.Vector2(elem) for elem in edges]
        self.end=self.edges[-1]
        self.rectangles=self.calc_rectangles(edges)

    def calc_rectangles(self,edges):
        pairs=[edges[i:i+2] for i in range(len(edges)-1)] # Calculates consecutive pairs
        # Vertical edges
        rect_1=[elem for elem in pairs if elem[0][0]==elem[1][0]]
        rectangles=[(elem[0][0],j) for elem in rect_1 for j in range(elem[0][1],elem[1][1]+1)]
        # Horizontal edges
        rect_2=[elem for elem in pairs if elem[0][1]==elem[1][1]]
        rectangles+=[(i,elem[0][1]) for elem in rect_2 for i in range(elem[0][0],elem[1][0]+1)]
        # Rectangle conversion
        return [pygame.Rect(elem,(1,1)) for elem in set(rectangles)]

    def render_path(self):
        for point in self.rectangles:
            point.topleft=(point.x,point.y)
            pygame.draw.rect(window,(0,255,0),point)

pygame.init()
window = pygame.display.set_mode((1000,700)) #Window initialisation
path=Path(10,[(1,100),(1,500),(700,500)]) # Temp case

# Main loop
running_game=True
while running_game:
    # Exit condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
    # Drawing the path
    path.render_path()
    pygame.display.update()
pygame.quit()
