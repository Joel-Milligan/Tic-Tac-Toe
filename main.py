import pygame
import colours
import drawing

# Initialisation of PyGame
pygame.init()
clock = pygame.time.Clock()
running = True

# Game screen
screen_size = (800, 600) 
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

    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()
