# Depth Limited Search (DLS) with path
def depth_limited_search(graph, start, goal, limit):
    def recursive_dls(node, goal, limit, path):
        if node == goal:              # Goal test
            return path
        elif limit == 0:              # Depth limit reached
            return "cutoff"
        else:
            cutoff_occurred = False
            for child in graph.get(node, []):   # Expand successors
                result = recursive_dls(child, goal, limit - 1, path + [child])
                if result == "cutoff":
                    cutoff_occurred = True
                elif result != "failure":
                    return result
            return "cutoff" if cutoff_occurred else "failure"

    return recursive_dls(start, goal, limit, [start])


# Iterative Deepening Search (IDS)
def iterative_deepening_search(graph, start, goal, max_depth=10):
    for depth in range(0, max_depth + 1):
        result = depth_limited_search(graph, start, goal, depth)
        if result != "cutoff":   # agar cutoff nahi hai to wahi return karo
            return result
    return "cutoff"


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

# Test IDS
print(iterative_deepening_search(graph, 'A', 'G', 1))  # → cutoff
print(iterative_deepening_search(graph, 'A', 'G', 2))  # → ['A', 'B', 'E', 'G']
print(iterative_deepening_search(graph, 'A', 'Z', 3))  # → failure
