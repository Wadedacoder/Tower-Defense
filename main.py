import pygame
from src.balloon import Balloon
from src.path import Path
from src.tower import Tower


pygame.init()
window = pygame.display.set_mode((1000,700)) #Window initialisation
path=Path(10,[(0,100),(500,100)]) # Temp case
pls = Tower('test', 10, 500, pygame.Vector2(20,20) , pygame.Vector2(100,100) , pygame.Vector2(200,150)) #demo

balloons = [Balloon("default", 100, 2, path.start)]

def draw(balloons):
    for balloon in balloons:
        balloon.draw(window)

running_game=True
while running_game:
    # Exit condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
    # Drawing the path
    pls.draw(window)
    pls.get_placed()
    # pls.update(balloons)
    path.render_path(window)
    pygame.display.update()
    draw(balloons)
    for balloon in balloons:
        balloon.draw(window)
        balloon.move(path.edges[1])
        

# def update(balloons):
    
#     update()
pygame.quit()