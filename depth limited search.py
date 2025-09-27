# Simple Depth Limited Search (DLS)

def depth_limited_search(graph, start, goal, limit):
    def recursive_dls(node, goal, limit):
        if node == goal:              # Goal test
            return True
        elif limit == 0:              # Depth limit reached
            return "cutoff"
        else:
            cutoff_occurred = False
            for child in graph.get(node, []):   # Expand successors
                result = recursive_dls(child, goal, limit - 1)
                if result == "cutoff":
                    cutoff_occurred = True
                elif result:          # Found solution
                    return True
            return "cutoff" if cutoff_occurred else False

    return recursive_dls(start, goal, limit)


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Test
print(depth_limited_search(graph, 'A', 'G', 2))  # → cutoff
print(depth_limited_search(graph, 'A', 'G', 3))  # → True (solution found)
print(depth_limited_search(graph, 'A', 'Z', 3))  # → False (failure)
