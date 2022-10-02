#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 01:41:16 2022

@author: dharmendrakhakhar
"""

# from _PriorityQueue import PriorityQueue

import copy
#LOC TO VAL IS INIT STATE
class boardState:
    
    def __init__ (self, boardObj, nextMove, pathCost, prevDigit = 0 ):
        
        self.currLoc = nextMove
        self.boardObj = boardObj
        # self.level = level
        self.pathCost = pathCost
        self.parentState = []
        
        
    # def getStateKey(self, loc):
        
    #     b  = copy.deepcopy(self.boardObj.board)
    #     b[tuple(self.currLoc)] = b[tuple(loc)]
    #     b[tuple(loc)] = 0        
    #     return tuple(b.items())
    
    
    def getStateAndKey(self, loc):
        
        b  = copy.deepcopy(self)
        b.updateBoard(loc)
        b.parentState = self
        
        return [b, tuple(b.boardObj.board.items())]
    
    def updateBoard(self, potMove):
        
        # movingDigit = self.boardObj.board[potMove[0]][potMove[1]]
        prevDigit = self.boardObj.board[tuple(potMove)]
        self.boardObj.board[tuple(self.currLoc)] = prevDigit
        self.boardObj.board[tuple(potMove)] = 0
        
        # self.prevDigit = prevDigit
        self.currLoc = potMove
                        
        
                
    def getPossMoves(self, defMov):
        
        newMoves = []
        currLoc = self.currLoc
        l = self.boardObj.length
        
        for i in defMov:
            
            if ((i[0]+currLoc[0])< l and (i[1]+ currLoc[1])< l) and ((i[0]+currLoc[0])>-1 and (i[1]+ currLoc[1])>-1):
                
                newMoves.append([i[0]+currLoc[0], i[1]+currLoc[1]])
        
        return newMoves

        
    def getDirectionMag(self, p1, p2):
        
        #Direction of p2 from p1
        # if abs(self.currLoc[0]-trial[0]) + abs(self.currLoc)
        
        return [p2[0]-p1[0], p2[1]-p1[1] ]
    
    
    def printAllParents(self):
        
        c = self
        i=0
        while c:
            print('\n final route iter ', i)
            c.boardObj.printState()
            c = c.parentState
            i+=1
    
    
        
            
        
        
        
        