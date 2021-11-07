import pygame
from pygame import draw
from sort import SortContainer
from time import sleep

FPS = 30
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

BAR_WIDTH = 3
BAR_HEIGHT_MULT = 2
BAR_SPACING = 2

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Sort Visualizer')
clock = pygame.time.Clock()

items = SortContainer()

def draw_elements(snapshot, last_touched=None):
    for count, element in enumerate(snapshot):
        pygame.draw.rect(window, (255,255,255), pygame.Rect((BAR_SPACING+BAR_WIDTH)*count, 0, BAR_WIDTH, element*BAR_HEIGHT_MULT))

running = True
sorting = False
idx = 0
while running:
    inputs = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and not sorting:
                items.shuffle_elements()
                idx = 0
            if event.key == pygame.K_SPACE:
                if not sorting:
                    if idx == 0:
                        sorting = True
    
    # delta_time = clock.tick(FPS)
    clock.tick(FPS)
    # sleep(1/FPS)

    window.fill((0,0,0))

    if sorting and idx < len(items.elements): # TODO: figure out why display is already sorted on first frame
        draw_elements(items.get_snapshot(idx))
        idx += 1
    else:
        draw_elements(items.get_snapshot(idx))
        sorting = False

    pygame.display.flip()

pygame.quit()
