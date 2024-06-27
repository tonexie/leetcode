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

def main():
  print(dfs_path_exists(graph, 'A', 'E'))  # Output: True
  print(dfs_path_exists(graph, 'A', 'D'))  # Output: True
  print(dfs_path_exists(graph, 'A', 'F'))  # Output: False

def dfs_path_exists(graph, start, target):
    # problem starts:
    stack = deque([start])
    vis = set()
    
    while stack:
      node = stack.pop()
      if node == target:
        return True
      if node not in vis:
        vis.add(node)
        for neighbour in graph.get(node, []):
          if neighbour not in vis:
            stack.append(neighbour)
    
    return False
  
  
if __name__ == "__main__":
  main()
    