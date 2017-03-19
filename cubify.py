filler = '/'

def cubify(word, subsqaures = True):
    #if not ((word.__len__() >= 5) & (word.isalpha()) & (word.endswith(word[0]))):
    if not ((word.__len__() >= 5) & (word.endswith(word[0]))):

        print("[cubify] This word (%s) can't be cubified." %word)
        return False
    else:
        print("[cubify] This word (%s) can be cubified." %word)

    word = word.upper()


    #create matrix filled with placeholder .
    size = int(word.__len__() / 2 + word.__len__()) + 1
    matrix = [[' ' for x in range(size)] for y in range(size)]


    gap = int(len(word) / 2)

    correction = 0
    if ((len(word) % 2) == 0):
        correction = 1

    for i in range(len(word)):
        #write horizontal words
        matrix[0][gap + i] = word[i]
        matrix[gap][i] = word[i]
        matrix[2*gap - correction][gap + i] = word[i]
        matrix[3*gap - correction][i] = word[i]

        #write vertical words
        matrix[gap + i][0] = word[i]
        matrix[i][gap] = word[i]
        matrix[i][3*gap - correction] = word[i]
        matrix[gap + i][2*gap - correction] = word[i]

    #write diagonal
    for i in range(1,gap):
        matrix[gap - i][i] = filler
        matrix[gap - i][2 * gap + i - correction] = filler
        matrix[3 * gap - i - correction][i] = filler
        matrix[3 * gap - i - correction][2 * gap + i - correction] = filler

    if(subsqaures):
        #add subsquare
        #determine at which position subsquare has to be added
        amountOfSubsqaures = 0
        if (len(word) < 12):
            amountOfSubsqaures = int(int(len(word) / 2) / 4)
        else:
            amountOfSubsqaures = int(int(len(word) / 2) / 3) - 1


        positionOfSubsquares = [int(int(len(word)/2)/(amountOfSubsqaures+1)) * (x+1) for x in range(amountOfSubsqaures)]


        #actual code of add subsquare
        for position in positionOfSubsquares:
            for i in range(len(word)):
                # write horizontal words
                matrix[position][gap - position + i] = word[i]
                matrix[2*gap + position - correction][gap - position + i] = word[i]

                # write vertical words
                matrix[i + position][gap - position] = word[i]
                matrix[i + position][3*gap - position - correction] = word[i]

    #making matrix pretty
    # matrix = [[x if x != ' ' else ' ' for x in row] for row in matrix]     #replace background with another character
    matrix = [' '.join(row) for row in matrix]

    matrix = ['    ' + row for row in matrix]

    return displayMatrix(matrix)


def displayMatrix(matrix):
    string = ''
    for x in matrix:
        for y in x:
            string += y
        string += '\n'
    return string
