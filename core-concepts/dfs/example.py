from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}

def main():
    print(dfs_path_exists(graph, 'A', 'E'))  # Output: True
    print(dfs_path_exists(graph, 'A', 'D'))  # Output: True
    print(dfs_path_exists(graph, 'A', 'F'))  # Output: False

def dfs_path_exists(graph, start, target):
    # Create a stack to store the nodes to be checked
    stack = [start]
    # Create a set to store the visited nodes
    visited = set()

    while stack:
        # Pop the last node from the stack
        node = stack.pop()

        # If this node is the target, return True
        if node == target:
            return True

        # If the node has not been visited
        if node not in visited:
            # Mark the node as visited
            visited.add(node)
            # Push all unvisited neighbors of the node onto the stack
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    stack.append(neighbor)

    # If there's no path between the start and target nodes
    return False

def dfs_rec(graph, start, target, visited):
    # If this node is the target, return True
    if start == target:
        return True

    # Mark the node as visited
    visited.add(start)

    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if dfs_rec(graph, neighbor, target, visited):
                return True

    # If no path is found, return False
    return False

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}

print(dfs_rec(graph, 'A', 'E', set()))  # Output: True
print(dfs_rec(graph, 'A', 'D', set()))  # Output: True
print(dfs_rec(graph, 'A', 'F', set()))  # Output: False



if __name__ == "__main__":
    main()
