import math

def minimax(node, depth, maximizingPlayer):
    
    if depth == 0 or isinstance(node, int):
        return node   # static evaluation

    # Maximizing Player
    if maximizingPlayer:
        maxEva = -math.inf
        for child in node:   
            eva = minimax(child, depth - 1, False)
            maxEva = max(maxEva, eva)
        return maxEva

    # Minimizing Player
    else:
        minEva = math.inf
        for child in node:
            eva = minimax(child, depth - 1, True)
            minEva = min(minEva, eva)
        return minEva



game_tree = [[3, 5], [2, [9, 12]]]

print("Best value for Maximizer:", minimax(game_tree, 3, True))
