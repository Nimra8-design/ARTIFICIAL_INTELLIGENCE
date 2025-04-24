# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 10:05:06 2025

@author: cuty computer
"""

#Binary Search

def binary_search(arr,target):
    low=0
    high=len(arr)-1
    
    while low<=high:
        mid=(low+high)//2
        print(f"Low: {low}, High: {high}, Mid: {mid}, Value at Mid: {arr[mid]}")
        
        if arr[mid]==target:
            print(f" {target} found at index {mid}")
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
            
    print(f"{target} not found in the array")
    return -1

numbers=[0,1,2,3,4,5,6,7,8,9]
binary_search(numbers,9)