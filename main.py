#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 21:50:16 2022

@author: dharmendrakhakhar
"""
from _Player import Player


P = Player()

for i in range(500):
    print(i,' iter \n')
    [nl, pc] = P.action()
    P.updateState(nl, pc)
    
    if P.currState.boardObj.goalTest():
        break
