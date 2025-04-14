# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 23:52:18 2025

@author: cuty computer
"""

#print item and its corresponding types

datalist=[1452,11.23,1+2j,True,'hello',(1,7),{"class:'5","section:A"}]

for item in datalist:
    print(f"{item} is of type {type(item)}")