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

class GOFImage():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('GEN')

        self.thisGen = []
        self.nextGen = []

        self.initGrid(COLS, ROWS, self.thisGen)
        self.initGrid(COLS, ROWS, self.nextGen)

        self.gens = 0
        self.imagesGen = []

        self.image1 = ImageTk.PhotoImage(Image.open(IMAGE_PATH))

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

        self.root.after(DELAY, self.nextGenLoop)
        self.root.mainloop()

    def nextGenLoop(self):
        self.gens += 1
        self.thisGenStr = self.printGen(COLS, ROWS, self.thisGen, self.gens, self.imagesGen)

        if (not self.isRepetition(self.thisGenStr)):
            self.processNextGen(COLS, ROWS, self.thisGen, self.nextGen)
            self.thisGen, self.nextGen = self.nextGen, self.thisGen

            self.image1 = ImageTk.PhotoImage(Image.open(IMAGE_PATH_FULL))
            self.panel1.configure(image=self.image1)
            self.display = self.image1

            self.root.after(DELAY, self.nextGenLoop)
        return

    def initGrid(self, cols, rows, array):
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

    def printGen(self, cols, rows, array, genNo, imageGen):
        strArray = ""
        im = Image.new('L', (cols, rows))
        for i in range(rows):
            for j in range(cols):
                if array[i][j] == -1:
                    True
                elif array[i][j] == 1:
                    strArray += '.'
                    im.putpixel((j,i),1000)
                else:
                    strArray += ' '
                    im.putpixel((j,i),0)

        im.save(IMAGE_PATH)
        self.resizeImage()

        return strArray

    def resizeImage(self):
        basewidth = 500
        img = Image.open(IMAGE_PATH)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        img.save(IMAGE_PATH_FULL)

    def processNextGen(self, cols, rows, cur, nxt):
        for i in range(1,rows-1):
            for j in range(1,cols-1):
                nxt[i][j] = self.processNeighbours(i, j, cur)

    def processNeighbours(self, x, y, array):
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

    def isRepetition(self, thisGenStr):
        global PASTGENS
        hashStr = hashlib.md5(thisGenStr.encode('utf-8')).hexdigest()

        if hashStr in PASTGENS :
            return True
        else:
            PASTGENS.append(hashStr)
            return False


ROWS = 100
COLS = 100
DELAY = 1
PASTGENS = []
IMAGE_PATH='./gen.png'
IMAGE_PATH_FULL='./genFull.png'

test = GOFImage()
