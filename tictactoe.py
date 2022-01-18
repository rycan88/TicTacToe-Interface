import pygame, os, sys

class Square(object):
    def __init__(self, x, y):
        self.c = (x,y)
        self.coord = (board_margin + x * (tile_size + line_width), board_margin + y * (tile_size + line_width))
        self.text_coord = (self.coord[0] + tile_size * 0.2, self.coord[1] + tile_size * 0.2)
        self.rect = pygame.Rect(self.coord[0], self.coord[1], tile_size, tile_size)
        self.string = ""
        self.num = y * 3 + x
        self.color = (0, 0, 0)
    def displayChar(self):
        text = c_f.render(self.string, True, self.color)
        screen.blit(text, self.text_coord)
        pygame.display.update()

def initBoard():
    screen.fill(l_grey)
    board = pygame.Rect(board_margin, board_margin, board_size, board_size)

    first_line_start = board_margin + tile_size
    second_line_start = board_margin + line_width + 2 * tile_size
    Lines.append(pygame.Rect(first_line_start, board_margin, line_width, board_size))
    Lines.append(pygame.Rect(second_line_start, board_margin, line_width, board_size))
    Lines.append(pygame.Rect(board_margin, first_line_start, board_size, line_width))
    Lines.append(pygame.Rect(board_margin, second_line_start, board_size, line_width))

    for line in Lines:
        pygame.draw.rect(screen, d_grey, line)

    for y in range(3):
        for x in range(3):
            Tiles.append(Square(x, y))

        text = f.render(message, True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (750,200)
        screen.blit(text, textRect)
        pygame.display.update()
def Redraw():
    screen.fill(l_grey)
    for line in Lines:
        pygame.draw.rect(screen, d_grey, line)

    for tile in Tiles:
        tile.displayChar()
    message = "Player " + player + "'s Turn"

    if game_complete:
        message = "Player " + player + " Wins!!!"
        r_message = "Press R to Restart"
        text = f.render(r_message, True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (750, 400)
        screen.blit(text, textRect)
        pygame.display.update()
    elif turn == 9:
        message = "It is a tie!"
        r_message = "Press R to Restart"
        text = f.render(r_message, True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (750, 400)
        screen.blit(text, textRect)
        pygame.display.update()
    text = f.render(message, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (750, 200)
    screen.blit(text, textRect)
    pygame.display.update()

def is_Win(num, player):
    for com in win_boards:
        if num in com:
            running = True
            for x in com:
                if Tiles[x].string != player:
                    running = False
            if running:
                if player =="O":
                    for x in com:
                        Tiles[x].color = blue
                else:
                    for x in com:
                        Tiles[x].color = red
                return True
    return False


pygame.init()
screen_width=1000
screen_height=600
x = 0
y = 30
size=[screen_width,screen_height]
#os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pygame.init()
screen=pygame.display.set_mode(size)
pygame.mouse.set_visible(1)
pygame.display.set_caption("Ryan's TicTacToe Game")
f = pygame.font.Font("freesansbold.ttf", 40)


d_grey = (100, 100, 100)
l_grey = (200, 200, 200)
blue = (35,20,189)
red = (189,20,35)



line_width = 10
board_size = screen_height * 0.8
board_margin = screen_height * 0.1
tile_size = (board_size - 2 * line_width) / 3
c_f = pygame.font.Font("freesansbold.ttf", int(tile_size * 0.8))

win_boards = []
for y in range(3):
    B1 = []
    B2 = []
    for x in range(3):
        B1.append(x * 3 + y) #Vertical wins
        B2.append(y * 3 + x) #Horizontal wins
    win_boards.append(B1)
    win_boards.append(B2)
win_boards.append([0, 4, 8])
win_boards.append([2, 4, 6])

def main():
    global game_complete, player, message, Tiles, Lines, turn
    Tiles = []
    Lines = []
    turn = 0
    game_complete = False
    player = "O"
    message = "Player " + player + "'s Turn"
    text = f.render(message, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (800, 200)
    screen.blit(text, textRect)
    pygame.display.update()


    initBoard()

    X_Tiles = []
    O_Tiles = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game_complete:
                    continue
                if pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()
                    for tile in Tiles:
                        if tile.rect.collidepoint(x, y):
                            if tile.string == "":
                                turn += 1
                                tile.string = player
                                if player == "O":
                                    O_Tiles.append(tile.num)
                                    game_complete = is_Win(tile.num, "O")
                                    if game_complete == True:
                                        Redraw()
                                        break
                                    player = "X"
                                else:
                                    X_Tiles.append(tile.num)
                                    game_complete = is_Win(tile.num, "X")
                                    if game_complete == True:
                                        Redraw()
                                        break
                                    player = "O"
                                Redraw()

main()