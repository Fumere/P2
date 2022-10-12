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
        distDiffs =[]
        currManhCost = 0
        for k,v in board.items():
            # print(k,v)
            if v != 0:
                valATi = v
                finalLoc = finalBoard[v]
                
                dist = self.currState.getDirectionMag(k, finalLoc)
                jthCost =0
                if dist[1]<0:
                    
                    jthCost = jthCost + abs(dist[1]*self.costHeur[0])
                    
                if dist[0]<0:
                        
                    jthCost = jthCost + abs(dist[0]*self.costHeur[1])
    
                if dist[1]>0:
                    
                    jthCost = jthCost + abs(dist[1]*self.costHeur[2])
    
                if dist[0]>0:
                    
                    jthCost = jthCost + abs(dist[0]*self.costHeur[3])  
                
                currManhCost += jthCost
                # print(jthCost)
            
        for i in possMoves:
            
            valATi = board[tuple(i)] 
            finalLoc = finalBoard[valATi]
            
            distOld = self.currState.getDirectionMag(i, finalLoc)
            distNew = self.currState.getDirectionMag(self.currState.currLoc, finalLoc)
            
            distDiffs.append([distNew[0] - distOld[0], distNew[0] - distOld[0]])
        
        costsDiff =[]
        for j in range(len(distDiffs)):
            jthCost =0
            if distDiffs[j][1] <0:
                
                jthCost = jthCost + distDiffs[j][1]*self.costHeur[0]
                
            if distDiffs[j][0]  <0:
                    
                jthCost = jthCost + distDiffs[j][0]*self.costHeur[1]

            if distDiffs[j][1]>0:
                
                jthCost = jthCost + distDiffs[j][1]*self.costHeur[2]

            if distDiffs[j][0]>0:
                
                jthCost = jthCost + distDiffs[j][0]*self.costHeur[3]
            
            costsDiff.append(jthCost)
        
        
        manHCostsofPossMoves = [(currManhCost + aCostsDiff) for aCostsDiff in costsDiff]
        
        self.currState.manHcost = currManhCost
        return manHCostsofPossMoves            

    
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
            # [_, stateKey] = self.currState.getStateAndKey(i)
            s=[]
            digitATi= self.currState.boardObj.board[tuple(i)]
            t = tuple([tuple(i),0])
            
            for j in tuple(self.currState.boardObj.board.items()):
                
                if (j[0]==tuple(i)):
                    s.append(t)
                elif (j[1]==0):
                    s.append((j[0],digitATi))
                else:
                    s.append(j)
                    
                    
            if not(self.stateMap.checkKey(tuple(s))):
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
            if [-1*self.defMov[i][0], -1*self.defMov[i][1]] == direction: stepCost = self.costHeur[i]; break
        
        return [nextBoardState, stepCost]
        
     
    def updateState(self, nextBoardState, stepCost):
        
        # nextBoardState.manHcost = self.getManhCost([nextBoardState.currLoc])
        self.currState = nextBoardState
        
        newPathCost = self.currState.pathCost + stepCost
        
        
        
        # self.stateMap.set(nextLoc, self.currState)
        
        self.currState.pathCost = newPathCost
        
        # self.currState = copy.deepcopy(self.stateMap.get(nextBoardStateKey))
        
        # self.currState.boardObj.printState()
        