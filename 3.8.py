# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 23:57:24 2025

@author: cuty computer
"""

#Print all numbers from 0 to 6 except 3 and 6

for i in range(7):
    if i==3 or i==6:
        continue
    print(i,end=" ")