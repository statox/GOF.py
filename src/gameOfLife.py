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
from PIL import Image, ImageTk
# from ttk import Frame, Button, Style
import time

class GOFImage():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('GEN')

        # pick an image file you have .bmp  .jpg  .gif.  .png
        # load the file and covert it to a Tkinter image object
        self.image1 = ImageTk.PhotoImage(Image.open(IMAGE_PATH))

        # get the image size
        w = self.image1.width()*10
        h = self.image1.height()*10

        # position coordinates of root 'upper left corner'
        x = 0
        y = 0

        # make the root window the size of the image
        self.root.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # root has no image argument, so use a label as a panel
        self.panel1 = tk.Label(self.root, image=self.image1)
        self.display = self.image1
        self.panel1.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        print("Display image1")
        # self.root.after(30000, self.update_image)
        self.root.mainloop()

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
        if c == cols-1:
            c=0
            l+=1

    im.save(IMAGE_PATH)
    for _ in range(5):
        imageGen.append(imageio.imread(IMAGE_PATH))

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

    while True:
        gens += 1
        thisGenStr = printGen(COLS, ROWS, thisGen, gens, imagesGen)
        # if (not isRepetition(thisGenStr)):
        if (gens<100 and not isRepetition(thisGenStr)):
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
# test= GOFImage()
