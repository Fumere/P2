#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 01:41:16 2022

@author: dharmendrakhakhar
"""

# from _PriorityQueue import PriorityQueue

class boardState:
    
    def __init__ (self, boardObj, nextMove, level):
        
        self.currLoc = nextMove
        self.boardObj = boardObj
        self.level = level
        
    
    def updateBoard(self, potMove):
        
        movingDigit = self.boardObj.board[potMove]
        self.boardObj.board[self.currLoc] = movingDigit
        
        self.boardObj.board[potMove] = []
                
        self.level+=1
        
        
                
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
    
            
        
            
        
        
        
        