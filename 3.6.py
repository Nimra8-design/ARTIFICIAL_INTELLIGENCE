# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 23:49:49 2025

@author: cuty computer
"""

#Count even and odd numbers from a series of number

numbers=(1,2,3,4,5,6,7,8,9,2,3,0)
even=0
odd=0
for num in numbers:
    if num%2==0:
        even+=1
    else:
        odd+=1
        
print("Number of even numbers: ",even)
print("Number of odd numbers: ",odd)