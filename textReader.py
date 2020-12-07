from os import listdir
import sys

def fileReader(fileName):
    path= "textfiles/"
    extension=".txt"
    filePath= path+fileName+extension
    textFile= open(filePath,"r")
    line= textFile.read()
    return str(line)

def chooseFile():
    fileList = [fileName for fileName in listdir("./textfiles") if fileName[-4:] == ".txt"]
    numFiles = len(fileList)
    assert numFiles > 0, "ERROR: no text files found"
    print("Choose text to print (enter the number on the left)")
    for index in range(numFiles):
        print(index, fileList[index])

    while True:
        try:
            response = int(input())
            if 0 <= response < numFiles:
                break
            else:
                print("Please enter a number from 0 to", numFiles-1)
        except ValueError:
            print("Please enter a number from 0 to", numFiles-1)

    return fileList[response][:-4]
        