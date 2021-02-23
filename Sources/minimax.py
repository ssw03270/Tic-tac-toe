def checkWinner(map)->int:
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

    if winner != 0:
        return winner

    # check game end
    isEnd = True
    for i in range(3):
        if not isEnd:
            break
        for j in range(3):
            if map[i][j] == 0:
                isEnd = False
                break
    if isEnd:
        return 3

    return winner

def randomMark(playerTurn:int, map:list, recordXY:list)->tuple:
    winner = checkWinner(map)
    if winner != 0:
        if winner == 2: 
            return (1, recordXY)
        elif winner == 1:
            return (-1, recordXY)
        elif winner == 3:
            return (0, recordXY)

    recordScore = []
    
    for i in range(3):
        for j in range(3):
            if map[i][j] == 0:
                if playerTurn == 1:
                    map[i][j] = 1
                    recordXY.append((i, j))
                    recordScore.append(randomMark(2, map, recordXY[0:len(recordXY)]))
                    map[i][j] = 0
                    recordXY.pop()
                elif playerTurn == 2:
                    map[i][j] = 2
                    recordXY.append((i, j))
                    recordScore.append(randomMark(1, map, recordXY[0:len(recordXY)]))
                    map[i][j] = 0
                    recordXY.pop()
    

    totalScore = recordScore[0][0]
    maxScore = recordScore[0][0]
    maxRecordXY = recordScore[0][1]
    minScore = recordScore[0][0]
    minRecordXY = recordScore[0][1]
    
    for i in range(1, len(recordScore)):
        score = recordScore[i][0]
        totalScore += recordScore[i][0]

        if maxScore < score:
            maxScore = score
            maxRecordXY = recordScore[i][1]
        if minScore > score:
            minScore = score
            minRecordXY = recordScore[i][1]

    if playerTurn == 1:
        return (minScore, minRecordXY)
    elif playerTurn == 2:
        return (maxScore, maxRecordXY)