#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 21:50:16 2022

@author: dharmendrakhakhar
"""
from _Player import Player


P = Player()

for i in range(500):
    # print(i,' iter \n')
    [nextBoardState, stepCost] = P.action()
    P.updateState(nextBoardState, stepCost)
    
    if P.currState.boardObj.goalTest():
        P.currState.manHcost =0
        P.currState.printAllParents()
        break
