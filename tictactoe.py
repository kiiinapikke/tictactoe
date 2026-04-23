import pygame, sys
pygame.init()

screen = pygame.display.set_mode((600, 600))
board = [[None]*3 for _ in range(3)]
turn = 'X'

while True:
    screen.fill((220,220,220))

  
    pygame.draw.line(screen,(0,0,0),(200,0),(200,600),5)
    pygame.draw.line(screen,(0,0,0),(400,0),(400,600),5)
    pygame.draw.line(screen,(0,0,0),(0,200),(600,200),5)
    pygame.draw.line(screen,(0,0,0),(0,400),(600,400),5)

    
    for i in range(3):
        for j in range(3):
            x, y = j*200+100, i*200+100
            if board[i][j] == 'X':
                pygame.draw.line(screen,(255,0,0),(x-50,y-50),(x+50,y+50),5)
                pygame.draw.line(screen,(255,0,0),(x+50,y-50),(x-50,y+50),5)
            elif board[i][j] == 'O':
                pygame.draw.circle(screen,(0,0,255),(x,y),60,5)

    pygame.display.update()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            r, c = my//200, mx//200

            if board[r][c] is None:
                board[r][c] = turn
                turn = 'O' if turn == 'X' else 'X'
