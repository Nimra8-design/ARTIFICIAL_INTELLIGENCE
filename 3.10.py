# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 00:04:37 2025

@author: cuty computer
"""

#2D array

rows=3
cols=4

result=[]

for i in range (rows):
    row=[]
    for j in range (cols):
        row.append(i*j)
    result.append(row)
    
print(result)