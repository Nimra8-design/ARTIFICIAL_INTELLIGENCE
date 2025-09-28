import heapq  # We will use heapq (min-heap) to always get the node with the smallest heuristic value

class Node:
    def __init__(self, name, heuristic, parent=None):
        self.name = name           # Node name (for identification)
        self.heuristic = heuristic # Estimated cost to the goal (heuristic value)
        self.parent = parent       # Parent node in the search tree
        
    def __lt__(self, other):
        """Comparison function for the priority queue to order nodes by heuristic value"""
        return self.heuristic < other.heuristic

class GreedyBestFirstSearch:
    def __init__(self, start, goal, heuristic):
        self.start = start        # Starting node
        self.goal = goal          # Goal node
        self.heuristic = heuristic # Heuristic function (dict or function for each node)
        
    def search(self):
        open_list = []  # Priority queue (min-heap) for nodes to explore
        closed_list = set()  # Set of already explored nodes
        
        # Start with the start node
        start_node = Node(self.start, self.heuristic[self.start])
        heapq.heappush(open_list, start_node)
    
        while open_list:
            # Pop the node with the smallest heuristic value
            current_node = heapq.heappop(open_list)
            
            # If we reached the goal, return the path
            if current_node.name == self.goal:
                path = []
                while current_node:
                    path.append(current_node.name)
                    current_node = current_node.parent
                return path[::-1]  # Reverse the path to start from the beginning
            
            closed_list.add(current_node.name)
            
            # Explore neighbors 
            for neighbor in self.heuristic:
                if neighbor not in closed_list and neighbor != current_node.name:
                    neighbor_node = Node(neighbor, self.heuristic[neighbor], current_node)
                    heapq.heappush(open_list, neighbor_node)
        
        return None  # Return None if no path found

# Example usage
if __name__ == "__main__":
    # Example graph with heuristics for each node
    # You can replace this with a more complex heuristic function if needed
    heuristic = {
        'A': 7,  # Example: heuristic estimate of cost from node 'A' to goal
        'B': 6,
        'C': 2,
        'D': 3,
        'E': 5,
        'F': 1,
        'G': 0   # Goal node with heuristic 0
    }
    
    # Start node is 'A' and goal node is 'G'
    gbfs = GreedyBestFirstSearch(start='A', goal='G', heuristic=heuristic)
    
    # Perform the search
    path = gbfs.search()
    
    if path:
        print("Path found:", path)
    else:
        print("No path found")
