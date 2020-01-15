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

# Fonts
win_font = pygame.font.Font(pygame.font.get_default_font(), 100)
draw_font = pygame.font.Font(pygame.font.get_default_font(), 50)

# Game screen
screen_size = (600, 600) 
game_display = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Tic Tac Toe")
background_colour = colours.white

def check_win(board_state):
    for i in range(3):
        if (current_board[i][0] == 1 or current_board[i][0] == 2) and (current_board[i][0] == current_board[i][1] == current_board[i][2]):
            game_win()
        elif (current_board[0][i] == 1 or current_board[0][i] == 2) and (current_board[0][i] == current_board[1][i] == current_board[2][i]):
            game_win()
    
    if(current_board[1][1] == 1 or current_board[1][1] == 2):
        if current_board[0][0] == current_board[1][1] == current_board[2][2]:
            game_win()
        elif current_board[0][2] == current_board[1][1] == current_board[2][0]:
            game_win()

    number_of_empty = 0
    for i in range(3):
        for j in range(3):
            if(current_board[i][j] == 0):
                number_of_empty += 1

    if number_of_empty == 0:
        game_draw()

def game_win():
    if current_turn == 2:
        text1 = win_font.render("x has won!", True, colours.green, colours.white)
        text2 = win_font.render("x has won!", True, colours.red, colours.white)
        
        for i in range(3):
            game_display.fill(background_colour)
            game_display.blit(text1, \
                ((game_display.get_size()[0] / 2) - (text1.get_size()[0] / 2), \
                (game_display.get_size()[1] / 2) - (text1.get_size()[1] / 2)) )
            
            pygame.display.update()
            pygame.time.delay(1000)

            game_display.fill(background_colour)
            game_display.blit(text1, \
                ((game_display.get_size()[0] / 2) - (text1.get_size()[0] / 2), \
                (game_display.get_size()[1] / 2) - (text1.get_size()[1] / 2)) )
            
            pygame.display.update()
            pygame.time.delay(1000)
    else:
        text1 = win_font.render("o has won!", True, colours.green, colours.white)
        text2 = win_font.render("o has won!", True, colours.red, colours.white)

        for i in range(3):
            game_display.fill(background_colour)
            game_display.blit(text1, \
                ((game_display.get_size()[0] / 2) - (text1.get_size()[0] / 2), \
                (game_display.get_size()[1] / 2) - (text1.get_size()[1] / 2)) )
            
            pygame.display.update()
            pygame.time.delay(1000)

            game_display.fill(background_colour)
           
            game_display.blit(text2, \
                ((game_display.get_size()[0] / 2) - (text1.get_size()[0] / 2), \
                (game_display.get_size()[1] / 2) - (text1.get_size()[1] / 2)) )
            
            pygame.display.update()
            pygame.time.delay(1000)

    pygame.quit()
    quit()

def game_draw():
    game_display.fill(background_colour)
    text = draw_font.render("The game is drawn!", True, colours.black, colours.white)
    game_display.blit(text, \
        ((game_display.get_size()[0] / 2) - (text.get_size()[0] / 2), \
        (game_display.get_size()[1] / 2) - (text.get_size()[1] / 2)) )
            
    pygame.display.update()
    pygame.time.delay(1000)
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
