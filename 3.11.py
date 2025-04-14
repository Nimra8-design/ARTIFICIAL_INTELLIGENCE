# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 15:50:35 2025

@author: cuty computer
"""

#Enters a blank line to to finish input and 
#write in output all upper cases as lower case
print("Enter lines of text (enter a blank line to finish):")
lines = []
while True:
        line = input()
        if line == "":
            break
        lines.append(line.lower())
print("\nOutput:")
for line in lines:
        print(line)