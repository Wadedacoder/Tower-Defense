import pygame
from src.balloon import Balloon
from src.path import Path
from src.tower import Tower


pygame.init()
window = pygame.display.set_mode((1000,700)) #Window initialisation
path=Path(10,[(0,100),(500,100)]) # Temp case
pls = Tower('test', 10, 500, pygame.Vector2(20,20) , pygame.Vector2(100,100) , pygame.Vector2(200,150)) #demo

balloons = [Balloon("default", 100, 2, path.start),Balloon("default", 100, 0.00, path.start)]

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
    path.render_path(window)
    draw(balloons)
    pygame.display.update()
    if pls.is_placed == False:
        pls.get_placed()
    pls.update(balloons)
    window.fill((0, 0, 0))
    for balloon in balloons:
        balloon.draw(window)
        balloon.move(path.edges[1])
        

# def update(balloons):
    
#     update()
pygame.quit()