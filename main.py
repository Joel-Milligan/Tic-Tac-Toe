import pygame
import colours
import drawing
import time

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

def check_win(board_state):
    for i in range(3):
        if (current_board[i][0] == 1 or current_board[i][0] == 2) and (current_board[i][0] == current_board[i][1] == current_board[i][2]):
            time.sleep(1)
            pygame.quit()
            quit()
        elif (current_board[0][i] == 1 or current_board[0][i] == 2) and (current_board[0][i] == current_board[1][i] == current_board[2][i]):
            time.sleep(1)
            pygame.quit()
            quit()
    
    if(current_board[1][1] == 1 or current_board[1][1] == 2):
        if current_board[0][0] == current_board[1][1] == current_board[2][2]:
            time.sleep(1)
            pygame.quit()
            quit()
        elif current_board[0][2] == current_board[1][1] == current_board[2][0]:
            time.sleep(1)
            pygame.quit()
            quit()

# Left Mouse Click Function
def left_mouse_clicked(mouse_pos, turn):
    # Left column
    if mouse_pos[0] < (screen_size[0] / 3):
        # Top Left
        if mouse_pos[1] < (screen_size[1] / 3):
            current_board[0][0] = turn
        # Middle Left
        elif mouse_pos[1] < 2 * (screen_size[1] / 3):
            current_board[0][1] = turn
        # Bottom Left
        elif mouse_pos[1] < screen_size[1]:
            current_board[0][2] = turn
    
    # Centre column
    elif mouse_pos[0] < 2 * (screen_size[0] / 3):
        # Top Centre
        if mouse_pos[1] < (screen_size[1] / 3):
            current_board[1][0] = turn
        # Middle Centre
        elif mouse_pos[1] < 2 * (screen_size[1] / 3):
            current_board[1][1] = turn
        # Bottom Centre
        elif mouse_pos[1] < screen_size[1]:
            current_board[1][2] = turn
    
    # Right column
    elif mouse_pos[0] < screen_size[0]:
        # Top Right
        if mouse_pos[1] < (screen_size[1] / 3):
            current_board[2][0] = turn
        # Middle Right
        elif mouse_pos[1] < 2 * (screen_size[1] / 3):
            current_board[2][1] = turn
        # Bottom Right
        elif mouse_pos[1] < screen_size[1]:
            current_board[2][2] = turn

    if turn == 1:
        return 2
    else:
        return 1       

# Main Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                current_turn = left_mouse_clicked(event.pos, current_turn)

        # print(event)

    game_display.fill(background_colour)
    drawing.draw_grid(game_display, current_board)
    pygame.display.update()
    check_win(current_board)
    clock.tick(60)

pygame.quit()
quit()
