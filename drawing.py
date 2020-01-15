import pygame
import colours

indent = 20
thickness = 5

def draw_grid(surface, board_state):
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

    # Draw noughts and crosses
    for i in range(3):
        for j in range(3):
            if board_state[i][j] == 1:
                draw_cross(surface, i, j)
            elif board_state[i][j] == 2:
                draw_nought(surface, i, j)

def draw_cross(surface, col, row):
    dimensions = surface.get_size()
    
    # Top left to bottom right
    pygame.draw.line(surface, colours.red, \
            (indent + (col * (dimensions[0] / 3)), indent + (row * (dimensions[1] / 3))), \
            (((col + 1) * (dimensions[0] / 3)) - indent, ((row + 1) * (dimensions[1] / 3)) - indent), \
            thickness)
    
    # Top right to bottom left
    pygame.draw.line(surface, colours.red, \
            (((col + 1) * (dimensions[0] / 3)) - indent, (row * (dimensions[1] / 3)) + indent), \
            (indent + (col * (dimensions[0] / 3)), ((row + 1) * (dimensions[1] / 3)) - indent), \
            thickness)

# Currently only works for square window sizes
def draw_nought(surface, col, row):
    dimensions = surface.get_size()

    pygame.draw.circle(surface, colours.blue, \
        (int((col * dimensions[0] / 3) + dimensions[0] / 6), \
        int((row * dimensions[1] / 3) + dimensions[1] / 6)), \
        int((dimensions[0] / 6) - indent), int(thickness))