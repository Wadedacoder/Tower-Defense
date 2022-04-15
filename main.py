import pygame
from src.balloon import Balloon
from src.path import Path
from src.tower import Tower
from random import random
# from src.placeholder import Placeholder

pygame.init()
window = pygame.display.set_mode((1000,700)) #Window initialisation
path=Path(10,[(0,100),(500,100),(500,700)]) # Temp case
towers = [Tower('test', 200, 10, pygame.Vector2(20,20) , pygame.Vector2(100,100) , pygame.Vector2(200,150))] #demo

pygame.font.init()
# my_font = pygame.font.SysFont('Comic Sans MS', 30)
# text_surface = my_font.render('Some Text', False, (0, 0, 0))
# window.blit(text_surface, (0,0))

def draw_text(window):
    font = pygame.font.SysFont(pygame.font.get_default_font(), 36)
    text_surface = font.render('Press T for Tower', True, (255, 255, 255))
    window.blit(text_surface, dest=(0,0))

def placement_checker(self, rectangles):
        '''Returns false if the tower is not colliding with anything'''
        return any(i.size.colliderect(self.tower.size) for i in rectangles)

balloons = [
    Balloon("default", 100, 1, path.start + pygame.Vector2(0, 0),1),
    Balloon("default", 100, 1.2, path.start + pygame.Vector2(0, 0),1),
    Balloon("default", 100, 1.4, path.start + pygame.Vector2(0, 0),1),
    Balloon("default", 100, 1.5, path.start + pygame.Vector2(0, 0),1),
    Balloon("default", 100, 1.6, path.start + pygame.Vector2(0, 0),1),
    Balloon("default", 100, 1.7, path.start + pygame.Vector2(0, 0),1)]

# def draw(balloons):
#     for balloon in balloons:
#         balloon.draw(window)

edge_num = 1

KEY_T = 116
running_game=True
checker = False
initial_time = pygame.time.get_ticks()
while running_game:
    mouse = pygame.Vector2(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
    # Exit condition
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == KEY_T:
                checker = True
        if event.type == pygame.MOUSEBUTTONDOWN and checker:
            checker = False
            towers.append(Tower('test', 200, 10, pygame.Vector2(20,20) , pygame.Vector2(100,100) , pygame.Vector2(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])))
        if event.type == pygame.QUIT:
            running_game = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == KEY_T:
        #         if event.type == pygame.MOUSEBUTTONDOWN:
        #             towers.append(Tower('test', 200, 10, pygame.Vector2(20,20) , pygame.Vector2(100,100) , mouse))
            
        if event.type == pygame.QUIT:
            running_game = False
    # Drawing the path
    for Toweri in towers:
        Toweri.draw(window)
        Toweri.update(balloons)
    path.render_path(window)
    # draw(balloons)
    pygame.display.update()
    # try:
    #     print(place)
    #     place.update(mouse)
    #     place.draw(window)
    # except:
    #     pass
    window.fill((0, 0, 0))
    draw_text(window) 
    [balloon.draw(window,path.end) for balloon in balloons]
    for balloon in balloons:
        # for tower in towers:
        #     if tower.dmg_range.collidepoint(balloon.location):
        #         balloon.reduce_hp(tower.damage)
        if balloon.edge_num<len(path.edges):
            if balloon.location!=path.edges[balloon.edge_num]:
                balloon.move(path.edges[balloon.edge_num])
            else:
                balloon.edge_num+=1
    if (pygame.time.get_ticks() - initial_time) % 200 == 0:
        balloons.append(Balloon("default", 100, random()*2, path.start + pygame.Vector2(0, 0),1))

            
        # if balloon.has_collided(path, edge_num):
        #    print("Balloon collided!", edge_num)
        #    edge_num += 1
        #    if edge_num >= len(path.edges):
        #        print("bruh")
        #        edge_num -= 1
        

# def update(balloons):
    
#     update()
pygame.quit()