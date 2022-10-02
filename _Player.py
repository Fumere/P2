#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 18:44:45 2022

@author: dharmendrakhakhar
"""
from _eightBoard import eightBoard
from _boardState import boardState
from _PriorityQueue import PriorityQueue
from _HashTable import HashTable

class Player():
    
    def __init__ (self, defMov = [[0,-1], [-1,0],[0,1], [1,0]], costHuer = [2,1,2,3], boardObj = eightBoard()):
        
        self.costHeur = costHuer
        self.defMov = defMov
        self.currState = boardState(boardObj, [2,2], 0, 0)
                
        self.possMoves = PriorityQueue()
        
        self.stateMap = HashTable()
        
        [state, stateKey] = self.currState.getStateAndKey([2,2])
        self.stateMap.set(stateKey, state)
    
    
    def getManhCost(self, possMoves):
        board = self.currState.boardObj.board
        finalBoard = self.currState.boardObj.finalBoard
        magDistances = []
        for i in possMoves:
            
            valATi = board[tuple(i)] 
            finalLoc = finalBoard[valATi]
            
            dist = self.currState.getDirectionMag(i, finalLoc)
            magDistances.append(dist)
        
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
            
            [state, stateKey] = self.currState.getStateAndKey(move)
            self.possMoves.insert([state, costs[i]])
            
            # stateKey = self.currState.getStateKey(move)
            self.stateMap.set(stateKey, state)
            
        
        nextBoardState = self.possMoves.delete()
        
        return nextBoardState



    def removeVisitedMoves(self, possMoves):
        
        remaining = []
        
        for i in possMoves:
            [_, stateKey] = self.currState.getStateAndKey(i)

            if not(self.stateMap.checkKey(stateKey)):
                remaining.append(i)
        
        return remaining
                    
                
    def action(self):
        
        possMoves = self.currState.getPossMoves(self.defMov)
        
        remainingMoves = self.removeVisitedMoves(possMoves)

        getManhCost = self.getManhCost(remainingMoves)  
        
        finalCosts = [(x+self.currState.pathCost) for x in getManhCost]
        
        nextBoardState = self.updateFrontier(remainingMoves, finalCosts)
        
        # stateKey = self.currState.getStateKey(nextLoc)
        
        goingLoc = nextBoardState.parentState.currLoc
        
        comingLoc = nextBoardState.currLoc
        
        direction = self.currState.getDirectionMag(goingLoc, comingLoc)
        
        for i in range(len(self.defMov)):
            if self.defMov[i] == direction: stepCost = self.costHeur[i]; break
        
        return [nextBoardState, stepCost]
        
     
    def updateState(self, nextBoardState, pathCost):
        
        self.currState = nextBoardState
        
        newPathCost = self.currState.pathCost + pathCost
        
        # self.stateMap.set(nextLoc, self.currState)
        
        self.currState.pathCost = newPathCost
        
        # self.currState = copy.deepcopy(self.stateMap.get(nextBoardStateKey))
        
        self.currState.boardObj.printState()
        