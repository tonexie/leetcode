# Given a simple undirected graph represented as an adjacency list, 
# implement a function that uses Breadth-First Search (BFS) to find if there 
# is a path between a starting node and a target node.

#     A
#    / \
#   B   C
#  / \
# D   E

from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}


def bfs_path_exists(graph, start, target):
    # problem starts:
  
  
    # Create a queue to store the nodes to be checked
    queue = deque([start])
    # Create a set to store the visited nodes
    visited = set()

    while queue:
        # Dequeue the first node from the queue
        node = queue.popleft()

        # If this node is the target, return True
        if node == target:
            return True

        # If the node has not been visited
        if node not in visited:
            # Mark the node as visited
            visited.add(node)
            # Enqueue all unvisited neighbors of the node
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    # If there's no path between the start and target nodes
    return False

print(bfs_path_exists(graph, 'A', 'E'))  # Output: True
print(bfs_path_exists(graph, 'A', 'D'))  # Output: True
print(bfs_path_exists(graph, 'A', 'F'))  # Output: False
