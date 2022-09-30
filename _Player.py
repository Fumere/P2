#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 18:44:45 2022

@author: dharmendrakhakhar
"""
from _eightBoard import eightBoard
from _boardState import boardState
from _PriorityQueue import PriorityQueue

class Player():
    
    def __init__ (self, defMov = [[0,-1], [-1,0],[0,1], [1,0]], costHuer = [2,1,2,3], boardObj = eightBoard()):
        
        self.costHeur = costHuer
        self.defMov = defMov
        self.currState = boardState(boardObj, [2,2], 0)
        
        self.pathCost = 0
        
        self.possMoves = PriorityQueue()
        
    
    
    def getManhCost(self, possMoves):
        board = self.currState.boardObj.board
        finalBoard = self.currState.boardObj.finalBoard
        magDistances = []
        for i in possMoves:
            
            for k in board.keys():
                
                if board[k]==i:
                    
                    finalLoc = finalBoard[k]
                    
                    dist = self.currState.getDirectionMag(i, finalLoc)
                    magDistances.append(dist)
                    break
        
        costs =[]
        for j in range(len(magDistances)):
            jthCost =0
            if magDistances[j][1]<0:
                
                jthCost = jthCost + abs(magDistances[j][1]*self.costHeur[0])
                
            if magDistances[j][0]<0:
                    
                jthCost = jthCost + abs(magDistances[j][0]*self.costHeur[1])

            if magDistances[j][1]>0:
                
                jthCost = jthCost + abs(magDistances[j][1]*self.costHeur[2])

            if magDistances[j][0]>0:
                
                jthCost = jthCost + abs(magDistances[j][0]*self.costHeur[3])  
            
            costs.append(jthCost)
        
        return costs            

    
    def updateFrontier(self, moves, costs):            
        
        for i in range(len(moves)):
            
            move = moves[i]
            self.possMoves.insert([move, costs[i]])
            
        
        nextLoc = self.possMoves.delete()
        
        return nextLoc          
                    
                
    def action(self):
        
        possMoves = self.currState.getPossMoves(self.defMov)

        getManhCost = self.getManhCost(possMoves)  
        
        finalCosts = [(x+self.pathCost) for x in getManhCost]
        
        nextLoc = self.updateFrontier(possMoves, finalCosts)
        
        return nextLoc
        
        
        