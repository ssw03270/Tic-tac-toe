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
    pygame.draw.line(screen, BLACK, [x + 20, y + 20], [x + 80, y + 80], 3)   # divide boundaries
    pygame.draw.line(screen, BLACK, [x + 80, y + 20], [x + 20, y + 80], 3)   # divide boundaries

# draw circle
def drawCircle(x : int, y : int):
    pygame.draw.circle(screen, BLACK, [x + 50, y + 50], 35, 2)   # divide boundaries

# check mouse pos and draw mark
def checkMousePos(mousePos : tuple):
    x = mousePos[0]
    y = mousePos[1]
    
    if 50 < x and x < 150:
        if 50 < y and y < 150:
            x = 50
            y = 50
        elif 150 < y and y < 250:
            x = 50
            y = 150
        elif 250 < y and y < 350:
            x = 50
            y = 250
    elif 150 < x and x < 250:
        if 50 < y and y < 150:
            x = 150
            y = 50
        elif 150 < y and y < 250:
            x = 150
            y = 150
        elif 250 < y and y < 350:
            x = 150
            y = 250
    elif 250 < x and x < 350:
        if 50 < y and y < 150:
            x = 250
            y = 50
        elif 150 < y and y < 250:
            x = 250
            y = 150
        elif 250 < y and y < 350:
            x = 250
            y = 250

    if(isPlayerOne):
        drawX(x, y)
        map[int((x - 50) / 100)][int((y - 50) / 100)] = 1
    else:
        drawCircle(x, y)
        map[int((x - 50) / 100)][int((y - 50) / 100)] = 2

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

    if winner != 0:
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

    if winner != 0:
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
done = False
map = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # 0 : blank, 1 : x, 2 : o
isPlayerOne = True  # True : playerOne, False : playerTwo
clock = pygame.time.Clock()

# set game
drawInit()

# loop game
while not done:
    clock.tick(10)  # set fps, 1 sec to 10 frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # if quit game
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN: # if input mouse button down
            mouseDown = True
  
    if mouseDown:
        mousePos = pygame.mouse.get_pos()
        checkMousePos(mousePos)
        isPlayerOne = not isPlayerOne
        winner = checkWinner()
        if winner != 0:
            if winner == 1:
                print("winner is x")
                done = True
            elif winner == 2:
                print("winner is o")
                done = True

    pygame.display.flip()   # update game display 

    # update value
    mouseDown = False
