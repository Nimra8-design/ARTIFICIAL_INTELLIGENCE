# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 14:59:34 2025

@author: cuty computer
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 14:15:49 2025

@author: cuty computer
"""

graph={
        1:[2,7,8],
        2:[3,6],
        3:[4,5],
        4:[],
        5:[],
        6:[],
        7:[],
        8:[9,12],
        9:[10,11],
        10:[],
        11:[],
        12:[]
        }

'''
print graph

'''
def print_graph(G):
     for node in G:
         print(f"{node} -> {G[node]}")
    

print_graph(graph)


'''
Iterative DFS

'''

def DFS_iterative(graph,start_node):
        visited=[]
        while stack:
         node=stack.top()
         stack.pop()
          
         for all neighbours w of node in graph:
                
            
            
            
print("Iterative DFS")           
DFS_iterative(graph,1)
    
    