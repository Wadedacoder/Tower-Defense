import pygame

class Path:
    def __init__(self,level,edges):
        self.level=level
        self.edges=[pygame.Vector2(elem) for elem in edges]
        self.start=self.edges[0]
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

    def render_path(self,window):
        for point in self.rectangles:
            point.topleft=(point.x,point.y)
            pygame.draw.rect(window,(0,255,0),point)
