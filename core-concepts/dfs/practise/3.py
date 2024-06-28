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

def dfs(start, target, graph):
  stack = deque([start])
  vis = set()
  
  while stack:
    node = stack.pop()
    if node == target:
      return True
    if node not in vis:
      vis.add(node)
      for n in graph.get(node, []):
        if n not in vis:
          stack.append(n)
          
  return False

print(dfs('A', 'C', graph))
print(dfs('A', 'E', graph))
print(dfs('A', 'F', graph))