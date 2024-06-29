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
  vis = set([start])
  
  while stack:
    node = stack.pop()
    if node == target:
      return True
    for n in graph.get(node, []):
      if n not in vis:
        stack.append(n)
        vis.add(n)
  return False

def dfs_rec(node, target, graph, visited):
  visited.add(node)
  if node == target:
    return True
  for n in graph.get(node, []):
    if n not in visited:
      if dfs_rec(n, target, graph, visited):
        return True
  return False


print(dfs('A', 'C', graph))
print(dfs('A', 'E', graph))
print(dfs('A', 'F', graph))
print(dfs_rec('A', 'C', graph, set()))
print(dfs_rec('A', 'E', graph, set()))
print(dfs_rec('A', 'F', graph, set()))
    