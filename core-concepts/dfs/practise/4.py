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
    vis.add(node)
    for n in graph.get(node, []):
      if n not in vis:
        stack.append(n)
        
  return False


def dfs_rec(start, target, graph, visited):
  if start == target:
    return True
  visited.add(start)
  for n in graph.get(start, []):
    if n not in visited:
      if dfs_rec(n, target, graph, visited):
        return True
  return False

print(dfs_rec('A', 'C', graph, set()))
print(dfs_rec('A', 'E', graph, set()))
print(dfs_rec('A', 'F', graph, set()))

print(dfs('A', 'C', graph))
print(dfs('A', 'E', graph))
print(dfs('A', 'F', graph))