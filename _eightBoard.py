#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:01:03 2022

@author: dharmendrakhakhar
"""

import math
import numpy as np

class eightBoard :
    
    def __init__(self, size = 8, positions = [2,8,3,6,7,4,1,5,0], final = [1,2,3,8,0,4,7,6,5]):
        
        l = math.sqrt(size+1)
        self.length = int(l)
        self.board = self.setLoc2Val(positions)
        self.finalBoard = self.setVal2Loc(final)
                
    def setLoc2Val (self, linearisedCords):
        
        rDict = dict()
        l = self.length
        for i in range(len(linearisedCords)):
            
            digit = linearisedCords[i]
            rDict[int(i/l) , i%l] = digit
            
        return rDict
    
    def setVal2Loc (self, linearisedCords):
        
        rDict = dict()
        l = self.length
        for i in range(len(linearisedCords)):
            
            digit = linearisedCords[i]
            rDict[digit] = [int(i/l) , i%l]
            
        return rDict
        
    def goalTest (self):
        
        
        return all([k==self.board[tuple(v)] for k,v in self.finalBoard.items() ])
    
    
    def printState(self):
        
        b = self.board
        l = self.length
        board = np.empty((l, l))
        
        for k,v in b.items():
            
            board[k[0]][k[1]] = v
    
        print('\n', board, '\n ---------')