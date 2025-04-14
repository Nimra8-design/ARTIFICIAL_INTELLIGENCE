# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 00:01:22 2025

@author: cuty computer
"""

#Fizz buzz program

for i in range(1,51):
    if i%3==0 and i%5==0 :
        print("fizzbuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5 ==0:
        print("Buzz")
    else:
        print(i)