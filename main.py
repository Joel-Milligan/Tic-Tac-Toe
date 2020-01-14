import pygame

# Initialisation of PyGame
pygame.init()
clock = pygame.time.Clock()
running = True

# Game screen
screen_size = (800, 600) 
game_display = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Tic Tac Toe")

# Main Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        print(event)

    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()
