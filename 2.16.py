# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 00:17:27 2025

@author: cuty computer
"""

#the _init_ function
class Person:
    
    def _init_(self,name,age):
        self.name=name
        self.age=age
    
p1=Person()
p1._init_("nimra", 19)
print(p1.name)  
print(p1.age)
    
