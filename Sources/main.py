import pygame

# draw game init
def drawInit():
    screen.fill(WHITE)
 
    pygame.draw.rect(screen, BLACK, [50, 50, 300, 300], 2)      # draw border line
    pygame.draw.line(screen, BLACK, [150, 50], [150, 350], 2)   # divide boundaries
    pygame.draw.line(screen, BLACK, [250, 50], [250, 350], 2)   # divide boundaries
    pygame.draw.line(screen, BLACK, [50, 150], [350, 150], 2)   # divide boundaries
    pygame.draw.line(screen, BLACK, [50, 250], [350, 250], 2)   # divide boundaries
# draw x 
def drawX(x : int, y : int):
    pygame.draw.line(screen, BLUE, [x + 20, y + 20], [x + 80, y + 80], 3)   # divide boundaries
    pygame.draw.line(screen, BLUE, [x + 80, y + 20], [x + 20, y + 80], 3)   # divide boundaries
# draw circle
def drawCircle(x : int, y : int):
    pygame.draw.circle(screen, RED, [x + 50, y + 50], 35, 2)   # divide boundaries
# draw game result
def drawResult(winner : int):
    # draw result box
    pygame.draw.rect(screen, WHITE, [50, 100, 275, 200])
    pygame.draw.aalines(screen, BLACK, True, [[50, 100], [50, 300], [325, 300], [325, 100]], True)

    # set font
    font = pygame.font.SysFont('arial',30)  #폰트 설정

    # set text 
    textStr = "X is winner" if winner == 1 else "O is winner"
    textStr2 = "If you want to play again"
    textStr3 = "press R"

    # set text render
    text = font.render(textStr, True, BLACK)
    text2 = font.render(textStr2, True, BLACK)
    text3 = font.render(textStr3, True, BLACK)

    # set text position
    textRect = text.get_rect(center = [200, 155])
    textRect2 = text2.get_rect(center = [200, 210])
    textRect3 = text3.get_rect(center = [200, 240])

    # show text in display
    screen.blit(text,textRect)
    screen.blit(text2,textRect2)
    screen.blit(text3,textRect3)
# check mouse pos and draw mark
# return bool type, can mark -> return true
def normalizeMousePos(mousePos : tuple)-> bool:
    # get mouse position
    x = mousePos[0]
    y = mousePos[1]
    
    # normalize mouse position
    if 50 < x and x < 150:          # if 50 < x < 150
        if 50 < y and y < 150:      # if 50 < y < 150
            x = 50
            y = 50
        elif 150 < y and y < 250:   # if 150 < y < 250
            x = 50
            y = 150
        elif 250 < y and y < 350:   # if 250 < y < 350
            x = 50
            y = 250
    elif 150 < x and x < 250:       # if 150 < x < 250
        if 50 < y and y < 150:      # if 50 < y < 150
            x = 150
            y = 50
        elif 150 < y and y < 250:   # if 150 < y < 250
            x = 150
            y = 150
        elif 250 < y and y < 350:   # if 250 < y < 350
            x = 150
            y = 250
    elif 250 < x and x < 350:       # if 250 < x < 350
        if 50 < y and y < 150:      # if 50 < y < 150
            x = 250
            y = 50
        elif 150 < y and y < 250:   # if 150 < y < 250
            x = 250
            y = 150
        elif 250 < y and y < 350:   # if 250 < y < 350
            x = 250
            y = 250

    if(map[int((x - 50) / 100)][int((y - 50) / 100)] == 0):  # if map[x][y] hasn't mark
        if(isPlayerOne):                # if player one win
            drawX(x, y)                 # draw x
            map[int((x - 50) / 100)][int((y - 50) / 100)] = 1
        else:                           # if player two win
            drawCircle(x, y)            # draw circle
            map[int((x - 50) / 100)][int((y - 50) / 100)] = 2
        return True
    else:
        return False
# check who is winner
def checkWinner():
    winner = 0
    # check vertical
    for i in range(3):
        isFinishX = True
        for j in range(3):
            if map[i][j] == 2 or map[i][j] == 0:
                isFinishX = False
                break
        if isFinishX:
            winner = 1

        isFinishO = True
        for j in range(3):
            if map[i][j] == 1 or map[i][j] == 0:
                isFinishO = False
                break
        if isFinishO:
            winner = 2

    if winner != 0: # if there is a winner
        return winner
        
    # check Horizontal
    for i in range(3):
        isFinishX = True
        for j in range(3):
            if map[j][i] == 2 or map[j][i] == 0:
                isFinishX = False
                break
        if isFinishX:
            winner = 1
            break

        isFinishO = True
        for j in range(3):
            if map[j][i] == 1 or map[j][i] == 0:
                isFinishO = False
                break
        if isFinishO:
            winner = 2
            break

    if winner != 0: # if there is a winner
        return winner

    
    # check Cross type 1
    isFinishX = True
    for i in range(3):
        if map[i][i] == 2 or map[i][i] == 0:
            isFinishX = False
            break
    if isFinishX:
        winner = 1

    isFinishO = True
    for i in range(3):
        if map[i][i] == 1 or map[i][i] == 0:
            isFinishO = False
            break
    if isFinishO:
        winner = 2

    # check Cross type 2
    isFinishX = True
    for i in range(3):
        if map[i][2 - i] == 2 or map[i][2 - i] == 0:
            isFinishX = False
            break
    if isFinishX:
        winner = 1
    
    isFinishO = True
    for i in range(3):
        if map[i][2 - i] == 1 or map[i][2 - i] == 0:
            isFinishO = False
            break
    if isFinishO:
        winner = 2

    return winner
# restart game
def restartGame():
    global end     
    end = False
    global map
    map = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]         # reset map
    drawInit()                                      # draw game again

# pygame start
pygame.init()

# game color
BLACK   = (  0,   0,   0)
WHITE   = (255, 255, 255)
BLUE    = (  0,   0, 255)
RED     = (255,   0,   0)

# set display size
size = [400, 400]
screen = pygame.display.set_mode(size)

# set display title
pygame.display.set_caption("Tic-tac-toe")

# set value
mouseDown = False
end = False
done = False
map = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]             # 0 : blank, 1 : x, 2 : o
isPlayerOne = True                                  # True : playerOne, False : playerTwo
clock = pygame.time.Clock()                         # pygame set fps value

# set game
drawInit()

# loop game
while not done:
    clock.tick(10)                                  # set fps, 1 sec to 10 frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:               # if quit game
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:    # if input mouse button down
            mouseDown = True
        if event.type == pygame.KEYDOWN:            # if input key down
            if event.key == ord('r'):               # if input key down "R"
                restartGame()                       # restart game
  
    if mouseDown and not end:                       # if mouse down and game wasn't end
        mousePos = pygame.mouse.get_pos()           # get mouse position    
        if(normalizeMousePos(mousePos)):            # normalization mouse position
            isPlayerOne = not isPlayerOne           # turn player
            winner = checkWinner()                  # check winner
            if winner != 0:                         # if there is a winner
                drawResult(winner)                  # draw result
                end = True                          # game end

    pygame.display.flip()                           # update game display 

    # update value
    mouseDown = False
