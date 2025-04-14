# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 23:38:43 2025

@author: cuty computer
"""

'''
Write a python program to guess a number between 1 to 9.
'''

import random

target=random.randint(1,9)
while True:
    guess=int(input("Guess a number between 1 and 9: "))
    if guess==target:
        print("Well guessed")
        break