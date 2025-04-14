# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 23:16:41 2025

@author: cuty computer
"""

'''
Write a python program to convert temperatures to and from celcius ,Farenheit
'''


#Celcius to farenheit

c=float(input("Enter temperature in celcius: "))

f=(c*9/5)+32

print(f"{c} `C is {f} in farenheit")

#farenheit to celcius

f=float(input("Enter temperature in farenheit: "))

c=(f-32)*5/9

print(f"{f} `F is {c} in celcius")
