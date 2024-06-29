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

def bfs(start, target, graph):
  queue = deque([start])
  vis = set([start])
  
  while queue:
    node = queue.popleft()
    if node == target:
      return True
    for n in graph.get(node, []):
      if n not in vis:
        vis.add(n)
        queue.append(n)
  return False

print(bfs('A', 'C', graph))
print(bfs('A', 'E', graph))
print(bfs('A', 'F', graph))