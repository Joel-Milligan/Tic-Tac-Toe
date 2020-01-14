import pygame
import colours

indent = 20
thickness = 5

def draw_grid(surface):
    dimensions = surface.get_size()

    # Draw vertical lines
    for x in range(1, 3):
        pygame.draw.line(surface, colours.black, \
            (x * (dimensions[0] / 3), indent), \
            (x * (dimensions[0] / 3), dimensions[1] - indent), \
            thickness)

    # Draw horizontal lines
    for y in range(1, 3):
        pygame.draw.line(surface, colours.black, \
            (indent, y * (dimensions[1] / 3)), \
            (dimensions[0] - indent, y * (dimensions[1] / 3)), \
            thickness)

def draw_cross(surface, col, row):

def draw_nought(surface, col, row):
    pass