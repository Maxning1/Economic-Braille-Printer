# --------------------
# textToBraille.py
# provides functions for converting text into braille
# add extra functionality in this file (such as text formatting)
# --------------------

import math

# -----GLOBAL PARAMETERS-----
charsPerLine = 13
numOfLines = 9
# --------------------

# dictionary that stores braille equivalent of common letters
# format: (the letter "n" for example)
# . .       [[1, 1],
#   .   =    [0, 1],
# .          [1, 0]]
brailleDict = {
    'a': [[1, 0], [0, 0], [0, 0]],
    'b': [[1, 0], [1, 0], [0, 0]],
    'c': [[1, 1], [0, 0], [0, 0]],
    'd': [[1, 1], [0, 1], [0, 0]],
    'e': [[1, 0], [0, 1], [0, 0]],
    'f': [[1, 1], [1, 0], [0, 0]],
    'g': [[1, 1], [1, 1], [0, 0]],
    'h': [[1, 0], [1, 1], [0, 0]],
    'i': [[0, 1], [1, 0], [0, 0]],
    'j': [[0, 1], [1, 1], [0, 0]],
    'k': [[1, 0], [0, 0], [1, 0]],
    'l': [[1, 0], [1, 0], [1, 0]],
    'm': [[1, 1], [0, 0], [1, 0]],
    'n': [[1, 1], [0, 1], [1, 0]],
    'o': [[1, 0], [0, 1], [1, 0]],
    'p': [[1, 1], [1, 0], [1, 0]],
    'q': [[1, 1], [1, 1], [1, 0]],
    'r': [[1, 0], [1, 1], [1, 0]],
    's': [[0, 1], [1, 0], [1, 0]],
    't': [[0, 1], [1, 1], [1, 0]],
    'u': [[1, 0], [0, 0], [1, 1]],
    'v': [[1, 0], [1, 0], [1, 1]],
    'w': [[0, 1], [1, 1], [0, 1]],
    'x': [[1, 1], [0, 0], [1, 1]],
    'y': [[1, 1], [0, 1], [1, 1]],
    'z': [[1, 0], [0, 1], [1, 1]],
    ' ': [[0, 0], [0, 0], [0, 0]],
    '0': [[0, 1], [1, 1], [0, 0]],
    '1': [[1, 0], [0, 0], [0, 0]],
    '2': [[1, 0], [1, 0], [0, 0]],
    '3': [[1, 1], [0, 0], [0, 0]],
    '4': [[1, 1], [0, 1], [0, 0]],
    '5': [[1, 0], [0, 1], [0, 0]],
    '6': [[1, 1], [1, 0], [0, 0]],
    '7': [[1, 1], [1, 1], [0, 0]],
    '8': [[1, 0], [1, 1], [0, 0]],
    '9': [[0, 1], [1, 0], [0, 0]],
    '.': [[0, 0], [1, 1], [0, 1]],
    ',': [[0, 0], [1, 0], [0, 0]],
    "'": [[0, 0], [0, 0], [1, 0]],
    '~': [[0, 0], [0, 0], [0, 1]],
    '`': [[0, 1], [0, 1], [1, 1]]
}

# returns a special character if text is either upper case or numeric and returns
# a blank string if otherwise because you can't contatinate a nonetype to a string


def specialChar(char: str):
    if char.isupper():
        return '~'
    return ''

# if a character is not a lower case number, return 2


#if a character is not a lower case number, return 2
def numOfChar(char: str):
    if char.isupper():
        return 2
    return 1


def textToBraille(textList):
    brailleList = []
    for textLine in textList:
        brailleLine = []
        for char in textLine:
            brailleLine.append(brailleDict.get(char))
        brailleList.append(brailleLine)
    return brailleList

def textToPoints(textList):
    brailleList = textToBraille(textList)

    # INTERNAL parameters for braille spacing
    dotSpacing = 5
    charSpacing = 8
    lineSpacing = 12
    margin = 3

    pointList = []

    for lineNum in range(len(brailleList)):
        # reset the position of print head at the beginning of each new page
        if (lineNum % numOfLines == 0):
            posX = posY = margin
            counter = 0  # count how many lines printed so far
            if lineNum > 0:
                pointList.append([-1, -1])  # SIGNAL TO START NEW PAGE


        line = brailleList[lineNum]
        
        for rowNum in range(3):  # print the 1st row of each line, then 2nd, then 3rd
            counter += 1
            row = []  # stores the current row being printed
            for char in line:
                dot1, dot2 = char[rowNum]
                if dot1:
                    row.append([posX, posY])
                posX += dotSpacing
                if dot2:
                    row.append([posX, posY])
                posX += charSpacing

            # printing optimization: reverse every two rows
            if counter % 2 == 1:
                row.reverse()
            
            pointList.extend(row)
            posX = margin
            posY += dotSpacing

        posX = margin
        posY += lineSpacing - dotSpacing

    return pointList
