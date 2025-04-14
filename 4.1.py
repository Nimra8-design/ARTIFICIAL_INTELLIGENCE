# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 12:28:12 2025

@author: cuty computer
"""


#Implement stack 

'''
STACK WORKS ON LIFO

'''


class stack:    #uses class to define stack
    def __init__(self):       #It is a constructor and initializes empty list
        self.stack=[]       #Self is the keyword used inside the class. It is the 
                            #reference to the object of the class.
                            #Empty class is created
    
    
    
    #adds item in the list
    def push(self,item):
        self.stack.append(item)
        print(f"Pushed {item} to stack.")
        

    #removes the top item
    def pop(self):
        if not self.is_empty():
            item=self.stack.pop()
            print(f"Popped {item} from stack.")
            return item
        else:
            print("Stack is empty...Nothing left to be popped.")
            
            
    #Shows the top element
    def top(self):
        if not self.is_empty():
            print(f"Top element is {self.stack[-1]}.")
        else:
            print("Stack is empty.")
            
    
    
    #Display the contents of stack
    def display(self):
        if self.stack:
            print("Contents in stack (top to bottom) LIFO are:")
            for item in reversed(self.stack):
                print(item)
        else:
            print("Stack is empty.")
            
    
    
    #Shows stack contents reversely
    def reverse_display(self):
        if self.stack:
            print("Contents in stack (bottom to top) reversed are:")
            for item in (self.stack):
                print(item)
        else:
            print("Stack is empty.")
            
        
    #Update item of stack
    def update(self, old_item, new_item):
        if old_item in self.stack:
            index=self.stack.index(old_item)
            self.stack[index]=new_item
            print(f"Old item {old_item} is updated by a new item {new_item}")
        else:
            print ("Item not found in current stack")
            
            
            
    
    #Delete item from stack
    def delete(self,item):
        if item in self.stack:
            self.stack.remove(item)
            print(f"Content {item} is deleted from stack. ")
        else:
            print ("Content {item} not found in current stack.")
            
            
    #Search item from stack
    def search(self,item):
        if item in self.stack:
            index=self.stack.index(item)
            print(f"{item} fount at index {len(self.stack)-index} from top")
        else:
            print("Item {item} not found in stack")
            
            
    
    
    #Stack is empty
    def is_empty(self):
        return len(self.stack)==0
    

#MAIN FUNCTION

def main():

    s= stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.display()
    s.top()
    s.pop()
    s.display()
    s.reverse_display()
    s.update(20,25)
    s.display()
    s.search(25)
    s.delete(10)
    s.display()    


main()
            
    