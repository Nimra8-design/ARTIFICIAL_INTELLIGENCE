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
Recursive DFS

'''

def DFS_recursive(graph,node,visit=None):
    if visit is None:
        visit=set()
    visit.add(node)
    print(node,end='')
        
    for neighbour in graph[node]:
        if neighbour not in visit:
            DFS_recursive(graph,neighbour,visit)
            
print("Recursive DFS")           
DFS_recursive(graph,1)
    
    