from math import inf

def minimax(node, depth, isMaximizingPlayer, alpha, beta, stats=None):
    
    if stats is None:
        stats = {'visited': 0, 'pruned': 0}
    stats['visited'] += 1

    # if node is a leaf node: return value of the node
    if not isinstance(node, list):
        return node

    # if isMaximizingPlayer:
    if isMaximizingPlayer:
        bestVal = -inf
        for child in node:
            value = minimax(child, depth + 1, False, alpha, beta, stats)
            # bestVal = max(bestVal, value)
            if value > bestVal:
                bestVal = value
            # alpha = max(alpha, bestVal)
            if bestVal > alpha:
                alpha = bestVal
            # if beta <= alpha: break
            if beta <= alpha:
                stats['pruned'] += 1
                break
        return bestVal

    # else (minimizing player)
    else:
        bestVal = inf
        for child in node:
            value = minimax(child, depth + 1, True, alpha, beta, stats)
            # bestVal = min(bestVal, value)
            if value < bestVal:
                bestVal = value
            # beta = min(beta, bestVal)
            if bestVal < beta:
                beta = bestVal
            # if beta <= alpha: break
            if beta <= alpha:
                stats['pruned'] += 1
                break
        return bestVal

# ---------------------------
# Example usage

if __name__ == "__main__":
    
    example_tree = [
        [3, 5, 6],          
        [9, [2, 0], 1],     
        [0, 7, 4]           
    ]

    stats = {'visited': 0, 'pruned': 0}
    result = minimax(example_tree, 0, True, -inf, inf, stats)
    print("Minimax value at root:", result)
    print("Nodes visited:", stats['visited'])
    print("Pruning events:", stats['pruned'])
