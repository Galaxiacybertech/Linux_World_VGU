import pygame
pygame.init()

screen = pygame.display.set_mode((600,600)) # display is used to set dimension of display

# heading set (caption)
pygame.display.set_caption("MyGame (X-O Game)")

# background color
WHITE = (255,255,255)

# text color
BLACK = (0,0,0)

# kitni size me dikhana hai
size = 200

# design of board # 3rows 3 columns
board = [["","",""], #1st row
        ["","",""], #2nd row
        ["","",""]] #3rd row

player = "X" #1st player
font = pygame.font.Font(None, 100) # font size is 100px

def check_winner(board):
    for i in range(3):
        # row check
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]

        # column check
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]

    # diagonal check
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    return None

def is_draw(board):
    for row in board:
        if "" in row:
            return False
    return True

winner = None
game_over = False

run = True
while run:
    screen.fill(WHITE)

    # drawing board lines
    pygame.draw.line(screen,BLACK,(200,0),(200,600),5)
    pygame.draw.line(screen,BLACK,(400,0),(400,600),5)
    pygame.draw.line(screen,BLACK,(0,200),(600,200),5)
    pygame.draw.line(screen,BLACK,(0,400),(600,400),5)

    # showing X and O on board
    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                text = font.render(board[row][col], True, BLACK)
                screen.blit(text,(col * size +70, row * size +50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type==pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x , mouse_y = pygame.mouse.get_pos()
            row = mouse_y //200
            col = mouse_x //200

            if board[row][col] == "":
                board[row][col] = player

                # checking winner and draw
                winner = check_winner(board)
                if winner:
                    game_over = True
                elif is_draw(board):
                    game_over = True
                else:
                    if player == "X":
                        player = "O"
                    else :
                        player = "X"

    # showing result on screen
    if game_over:
        if winner:
            end_text = font.render(winner + " wins!", True, BLACK)
        else:
            end_text = font.render("Draw!", True, BLACK)
        screen.blit(end_text, (180,260))

    pygame.display.update()

pygame.quit()