# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 00:14:38 2025

@author: cuty computer
"""

# accepts a string and calculate number of digits 


text=input("Enter a string: ")

letters=0
digits =0

for char in text:
    if char.isalpha():
        letters+=1
    elif char.isdigit():
        digits+=1
    
print("Letters",letters)
print("Digits",digits)