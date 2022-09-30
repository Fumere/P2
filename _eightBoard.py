#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:01:03 2022

@author: dharmendrakhakhar
"""

import math

class eightBoard :
    
    def __init__(self, size = 8, positions = [2,8,3,6,7,4,1,5,0], final = [1,2,3,8,0,4,7,6,5]):
        
        l = math.sqrt(size+1)
        self.length = int(l)
        self.board = self.setBoard(positions)
        self.finalBoard = self.setBoard(final)
                
    def setBoard (self, linearisedCords):
        
        rDict = dict()
        l = self.length
        for i in range(len(linearisedCords)):
            
            digit = linearisedCords[i]
            rDict[digit] = [int(i/l) , i%l]
            
        return rDict
        
    def goalTest (self):
        
        return (self.board == self.finalBoard)