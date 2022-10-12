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
        self.manHcost = 0
    
    def getStateAndKey(self, loc):
        
        b  = copy.deepcopy(self)
        b.updateBoard(loc)
        b.parentState = self
        
        return [b, tuple(b.boardObj.board.items())]
    
    def updateBoard(self, potMove):
        
        prevDigit = self.boardObj.board[tuple(potMove)]
        self.boardObj.board[tuple(self.currLoc)] = prevDigit
        self.boardObj.board[tuple(potMove)] = 0
        
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
        
        
        return [p2[0]-p1[0], p2[1]-p1[1] ]
    
    
    def printAllParents(self):
        
        c = self
        i=0
        while c:
            print('\n final route iter ', 10-i)
            c.boardObj.printState()
            print('\n g(n):', c.pathCost, '\t h(n): ', c.manHcost )
            c = c.parentState
            i+=1
    
    
        
            
        
        
        
        