#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#----------------------------------------------
# Conway's Game of Life
# More programs at UsingPython.com/programs
#----------------------------------------------

from PIL import Image
import random
import time
import os
import hashlib
import sys
import imageio

import tkinter as tk
from PIL import ImageTk, Image

def initGrid(cols, rows, array):
    for i in range(rows):
        arrayRow = []
        for j in range(cols):
            if (i == 0 or j == 0 or (i == rows - 1) or (j == cols - 1)):
                arrayRow += [-1]
            else:
                ran = random.randint(0,3)
                if ran == 0:
                    arrayRow += [1]
                else:
                    arrayRow += [0]
        array += [arrayRow]

def printGen(cols, rows, array, genNo, imageGen):
    os.system("clear")

    # print("Game of Life -- Generation " + str(genNo + 1))
    print(str(genNo))

    strArray = ""
    for i in range(rows):
        for j in range(cols):
            if array[i][j] == -1:
                # strArray += '#'
                True
            elif array[i][j] == 1:
                strArray += '.'
            else:
                strArray += ' '
        strArray += '\n'

    im = Image.new('L', (cols, rows))
    c = l = 0
    for v in strArray:
        if v == '.':
            im.putpixel((c,l),1000)
        elif v == ' ':
            im.putpixel((c,l),0)
        c += 1
        if c == cols:
            c=0
            l+=1

    im.save(IMAGE_PATH)
    for _ in range(5):
        imageGen.append(imageio.imread(IMAGE_PATH))
        # imageGen.append(imageio.imread(im))


    # print(strArray)
    return strArray

def processNextGen(cols, rows, cur, nxt):
    for i in range(1,rows-1):
        for j in range(1,cols-1):
            nxt[i][j] = processNeighbours(i, j, cur)

def processNeighbours(x, y, array):
    nCount = 0
    for j in range(y-1,y+2):
        for i in range(x-1,x+2):
            if not(i == x and j == y):
                if array[i][j] != -1:
                    nCount += array[i][j]
    if array[x][y] == 1 and nCount < 2:
        return 0
    if array[x][y] == 1 and nCount > 3:
        return 0
    if array[x][y] == 0 and nCount == 3:
        return 1
    else:
        return array[x][y]

def isRepetition(thisGenStr):
    global PASTGENS
    hashStr = hashlib.md5(thisGenStr.encode('utf-8')).hexdigest()

    if hashStr in PASTGENS :
        return True
    else:
        PASTGENS.append(hashStr)
        return False

def main():
    thisGen = []
    nextGen = []

    initGrid(COLS, ROWS, thisGen)
    initGrid(COLS, ROWS, nextGen)

    gens = 0
    imagesGen = []

# window = tk.Tk()
# window.title("Join")
# window.geometry("300x300")
# window.configure(background='grey')
# window.mainloop()
    while True:
        gens += 1
        thisGenStr = printGen(COLS, ROWS, thisGen, gens, imagesGen)
        if (gens<50 and not isRepetition(thisGenStr)):
            processNextGen(COLS, ROWS, thisGen, nextGen)
            time.sleep(DELAY)
            thisGen, nextGen = nextGen, thisGen
        else:
            imageio.mimsave('./GOF.gif', imagesGen)
            input("Finished. Press <return> to quit.")
            sys.exit()


ROWS = 100
COLS = 200
GENERATIONS = 100
# DELAY = 0.3
DELAY = 0.0
PASTGENS = []
IMAGE_PATH='./gen.png'
main()
