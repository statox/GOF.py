#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('./'))
from GOL import *

import tkinter as tk
from PIL import Image, ImageTk

class GOLImage():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('GEN')

        self.gol = GOL()

        self.image1 = ImageTk.PhotoImage(Image.open(IMAGE_PATH))

        w = COLS * 5.5
        h = ROWS * 5.5

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
        self.gol.processNextGen()
        thisGenStr = self.printGen(self.gol.thisGen, 1)

        if (not self.gol.isRepetition(thisGenStr)):
            self.image1 = ImageTk.PhotoImage(Image.open(IMAGE_PATH_FULL))
            self.panel1.configure(image=self.image1)
            self.display = self.image1

            self.root.after(DELAY, self.nextGenLoop)
        return

    def printGen(self, array, genNo):
        strArray = ""
        im = Image.new('L', (COLS, ROWS))
        for i in range(ROWS):
            for j in range(COLS):
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
        basewidth = 1000
        img = Image.open(IMAGE_PATH)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        img.save(IMAGE_PATH_FULL)

ROWS = 100
COLS = 200
DELAY = 1
PASTGENS = []
IMAGE_PATH='./gen.png'
IMAGE_PATH_FULL='./genFull.png'
