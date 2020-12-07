from textToBraille import numOfChar
from textToBraille import specialChar

charsPerLine = 13

def text_wrapping(text):
    brailleEngWords = 0
    toBeConverted = []
    #there will be maxLines elements each with charsPerLine characters in the final array
    #split input by a newline and then determine how many times the text got split
    textbynewLine = text.split('\n')
    inputLines = len(textbynewLine)
    currentLine = 0
    lenOfPrevLine = charsPerLine + 1
    while currentLine < inputLines:
        #further split input by a space to acheive words
        Words = textbynewLine[currentLine].split(' ')
        inputWords = len(Words)
        currentWord = 0
        while currentWord < inputWords:
            wordlen = 0
            #if there is an extra space, skip
            if len(Words[currentWord]) == 0:
                currentWord = currentWord + 1
                continue
            #determine the length of a word
            for char in Words[currentWord]:
                wordlen = wordlen + numOfChar(char)
            #if a word is over the word limit, split up the word until it fits
            charLeftOver = wordlen - charsPerLine
            while charLeftOver > 0:
                toBeConverted.append(Words[currentWord][0:charsPerLine-1])
                Words[currentWord] = Words[currentWord][charsPerLine-1:]
                charLeftOver = charLeftOver - charsPerLine
                brailleEngWords = brailleEngWords + 2
                lenOfPrevLine = len(toBeConverted[currentWord])
                currentWord = currentWord + 1
            #resets wordlen
            wordlen = 0
            for char in Words[currentWord]:
                wordlen = wordlen + numOfChar(char)
            #if a word plus a previous word and a space fit on a line, append the word to the previous line
            totalLen = int(lenOfPrevLine) + 1 + int(wordlen)
            if totalLen <= charsPerLine:
                if wordlen == 0:
                    break
                brailleEngWords = brailleEngWords - 1
                toBeConverted[brailleEngWords] = toBeConverted[brailleEngWords] + ' ' + (Words[currentWord])
                lenOfPrevLine = len(toBeConverted[brailleEngWords])
                brailleEngWords = brailleEngWords + 1
                currentWord = currentWord + 1
                continue
            #otherwise add the word onto its own line
            else:
                toBeConverted.append(Words[currentWord])
                lenOfPrevLine = len(toBeConverted[brailleEngWords])
                brailleEngWords = brailleEngWords + 1
                currentWord = currentWord + 1
        currentLine = currentLine + 1
    return text_conversion(toBeConverted)

def text_conversion(toBeConverted):
    x = 0
    while x < len(toBeConverted):
        brailleEng = ''
        for char in toBeConverted[x]:
            brailleEng = brailleEng + specialChar(char)
            brailleEng = brailleEng + char.lower()
        toBeConverted[x] = brailleEng
        x = x + 1
    return toBeConverted