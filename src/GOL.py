#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import hashlib

class GOL():
    def __init__(self):
        self.thisGen = []
        self.nextGen = []
        self.thisGenStr = ""

        self.cols = COLS
        self.rows = ROWS

        self.initGrid(self.thisGen)
        self.initGrid(self.nextGen)

        self.gens = 0
        self.imagesGen = []

        self.PASTGENS = []

    def initGrid(self, array):
        # array = [[random.randint(0,1) for i in range(ROWS)] for j in range(COLS)]
        for i in range(self.rows):
            arrayRow = []
            for j in range(self.cols):
                if (i == 0 or j == 0 or (i == self.rows - 1) or (j == self.cols - 1)):
                    arrayRow += [-1]
                else:
                    ran = random.randint(0,3)
                    if ran == 0:
                        arrayRow += [1]
                    else:
                        arrayRow += [0]
            array += [arrayRow]

    def processNextGen(self):
        for i in range(1,self.rows-1):
            for j in range(1,self.cols-1):
                self.nextGen[i][j] = self.processNeighbours(i, j, self.thisGen)

        self.thisGen, self.nextGen = self.nextGen, self.thisGen

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
        hashStr = hashlib.md5(thisGenStr.encode('utf-8')).hexdigest()

        if hashStr in self.PASTGENS :
            return True
        else:
            self.PASTGENS.append(hashStr)
            return False

ROWS = 100
COLS = 200
