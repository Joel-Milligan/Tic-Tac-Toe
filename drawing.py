import pygame
import colours

indent = 20
window_border = 50

def draw_grid(surface, board_state):
    dimensions = surface.get_size()

    # Draw vertical lines
    for x in range(1, 3):
        pygame.draw.line(surface, colours.black, \
            ((x * ((dimensions[0] - (2 * window_border)) / 3)) + window_border, window_border), \
            ((x * ((dimensions[0] - (2 * window_border)) / 3)) + window_border, dimensions[1] - window_border), \
            thickness)

    # Draw horizontal lines
    for y in range(1, 3):
        pygame.draw.line(surface, colours.black, \
            (window_border, (y * ((dimensions[1] - (2 * window_border)) / 3)) + window_border), \
            (dimensions[0] - window_border, (y * ((dimensions[1] - (2 * window_border)) / 3)) + window_border), \
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
    
    x11 = (indent + (col * ((dimensions[0] - (2 * window_border)) / 3))) + window_border
    y11 = (indent + (row * ((dimensions[1] - (2 * window_border)) / 3))) + window_border
    x12 = (((col + 1) * ((dimensions[0] - (2 * window_border)) / 3)) - indent) + window_border
    y12 = (((row + 1) * ((dimensions[1] - (2 * window_border)) / 3)) - indent) + window_border

    # Top left to bottom right
    pygame.draw.line(surface, colours.red, \
            (x11, y11), \
            (x12, y12), \
            thickness)
    
    x21 = (((col + 1) * ((dimensions[0] - (2 * window_border)) / 3)) - indent) + window_border
    y21 = ((row * ((dimensions[1] - (2 * window_border)) / 3)) + indent) + window_border
    x22 = (indent + (col * ((dimensions[0] - (2 * window_border)) / 3))) + window_border
    y22 = (((row + 1) * ((dimensions[1] - (2 * window_border)) / 3)) - indent) + window_border

    # Top right to bottom left
    pygame.draw.line(surface, colours.red, \
            (x21, y21), \
            (x22, y22), \
            thickness)

# Currently only works for square window sizes
def draw_nought(surface, col, row):
    dimensions = surface.get_size()

    x = (col * (dimensions[0] - (2 * window_border)) / 3) + ((dimensions[0] - (2 * window_border)) / 6) + window_border
    y = (row * (dimensions[1] - (2 * window_border)) / 3) + ((dimensions[1] - (2 * window_border)) / 6) + window_border 
    r = ((dimensions[0] - (2 * window_border)) / 6) - indent

    pygame.draw.circle(surface, colours.blue, (int(x), int(y)), int(r), int(thickness))