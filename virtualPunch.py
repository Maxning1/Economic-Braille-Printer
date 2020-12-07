#--------------------
# virtualPunch.py
# emulator for braille printer
#--------------------

import pygame
from textToBraille import textToPoints
from textReader import fileReader, chooseFile
from textwrap import text_wrapping

# emulates punch() in main.py, by drawing a circle
# if the parameters in textToBraille are bad and generate dots outside of page
# then the assert will fail!
def punch(x, y):
    if x == -1 and y == -1:
        screen.fill(WHITE)
        clock.tick(1)
    else:
        assert 0 <= x <= 190, "MOTOR X OUT OF RANGE" + str(x)
        assert 0 <= y <= 210, "MOTOR Y OUT OF RANGE" + str(y)
        pygame.draw.circle(screen, BLACK, [3*x, 3*y], 3)

# IMPORTANT
pointList = textToPoints(text_wrapping(fileReader(chooseFile())))

# pygame boilerplate code
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.init()
size = (190*3, 210*3)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("virtualPunch")
clock = pygame.time.Clock()
screen.fill(WHITE)


for x, y in pointList:
    # pygame stuff to make the window closable
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # the real magic
    punch(x, y)

    # update screen
    pygame.display.flip()
    clock.tick(25)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            break
