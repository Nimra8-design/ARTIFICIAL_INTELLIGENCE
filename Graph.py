# -*- coding: utf-8 -*-
"""
Created on Sun May 11 06:25:11 2025

@author: cuty computer
"""
class Graph:
    def __init__(self):
        self.adj_list={}
        
        
    def add_edge(self,u,v):
        if u not in self.adj_list:
            self.adj_list[u]=[]
        self.adj_list[u].append(v)
        
        
      
        
        
    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex} -> {self.adj_list[vertex]}")
            
            
graph=Graph()
graph.add_edge(0,1)
graph.add_edge(2,3)
graph.add_edge(2,1)
graph.add_edge(4,1)
graph.add_edge(3,0)
graph.add_edge(2,0)
graph.add_edge(2,1)
graph.add_edge(3,1)

graph.print_graph()



            
