# -*- coding: utf-8 -*-
"""
Created on Sat May  3 07:38:19 2025

@author: cuty computer
"""
#deque (double ended queue) efficient for O(1)
from collections import deque

class Graph:
    def __init__(self,vertices):
        #number of vertices
        self.v=vertices
        #adjency list 
        #list of lists
        #where each vertex has its own list of connected vertices
        self.adj=[[]for _ in range (vertices)]
        
    #Adding an edge to graph
    def add_edge(self,v,w):
        #add w to v in list
        self.adj[v].append(w)
        
    #BFS implementation
    def BFS(self,s):
        
        #Mark all vertices as not visited
        visited=[False]*self.v
      
        #Initializes a queue for BFS
        queue=deque()
        
        #Mark the starting node as visited and enqueue it
        visited[s]=True
        queue.append(s)
        
        #Processiimg nodes in BFS order
        while queue:
            #Dequeue a vertex and print it
            s=queue.popleft()
            print(s,end=' ')
            
            #explore all adjacent vertices
            for i in self.adj[s]:
                if not visited[i]:
                    visited[i]=True
                    queue.append(i)
                    
#Code to  test BFS
if __name__=="__main__": 

    #Create a graph with 4 vertices
    g=Graph(4)

    #Add edges (0->1, 0->2, 1->2, 2->0, 2->3, 3->3)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)


    print("Following is Breadth First Traversal (starting from vertex 2)")
    g.BFS(2)  # Start BFS from vertex 2
