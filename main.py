import pygame
import colours
import drawing

# Initialisation of the game
pygame.init()
clock = pygame.time.Clock()
running = True
current_turn = 1
current_board = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]

# Game screen
screen_size = (600, 600) 
game_display = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Tic Tac Toe")
background_colour = colours.white

# Main Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        print(event)

    game_display.fill(background_colour)
    drawing.draw_grid(game_display)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
