# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 00:13:48 2025

@author: cuty computer
"""

'''
Queue works on FIFO principle
'''

class Queue:  # uses class to define queue
    def __init__(self):  # It is a constructor and initializes an empty list
        self.queue = []  # Self is the keyword used inside the class. It is the reference to the object of the class.

    '''
    Following is the function to create a new queue 
    and clear an existing one
    '''

    # Creating a linear queue
    def create(self):
        self.queue = []
        print("Queue is created")

    # Function to add element in queue (enqueueing)
    def enqueue(self, value):
        self.queue.append(value)
        print(f"Enqueued: {value}")

    # Function to remove the front (first) element from queue (dequeueing)
    def dequeue(self):
        if not self.queue:
            print("Queue is empty. We cannot dequeue it.")
            return None
        value = self.queue.pop(0)
        print(f"Dequeued: {value}")
        return value

    # Function to see the first value entered in queue
    def first(self):
        if not self.queue:
            print("Queue is empty.")
            return None
        print(f"First element: {self.queue[0]}")
        return self.queue[0]

    # Function to display the queue
    def display(self):
        if not self.queue:
            print("Queue is empty.")
        else:
            print("Queue Contents:", self.queue)

    # Function to display reverse queue (Without modifying the queue)
    def reverse_display(self):
        if not self.queue:
            print("Queue is empty.")
        else:
            print("Queue in reverse order:", self.queue[::-1])

    # Function to update a value at a given index
    def update(self, index, new_value):
        if 0 <= index < len(self.queue):
            old_value = self.queue[index]
            self.queue[index] = new_value
            print(f"Updated index {index}: {old_value} -> {new_value}")
        else:
            print("Invalid index.. Update failed.")

    # Function to delete a value at a given index
    def delete(self, index):
        if 0 <= index < len(self.queue):
            removed = self.queue.pop(index)
            print(f"Deleted element at index {index}: {removed}")
        else:
            print("Invalid index... Deletion failed.")

    # Function to search for a value in a queue
    def search(self, value):
        if value in self.queue:
            index = self.queue.index(value)
            print(f"Element '{value}' found at index {index}.")
            return index
        else:
            print(f"Element '{value}' not found.")
            return -1

# MAIN FUNCTION
def main():
    q = Queue()
    q.create()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()
    q.first()
    q.reverse_display()
    q.update(1, 25)
    q.display()
    q.search(25)
    q.dequeue()
    q.display()

main()
