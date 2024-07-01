# Given a simple undirected graph represented as an adjacency list,
# implement a function that uses Breadth-First Search (BFS) to find if there
# is a path between a starting node and a target node.

#     A
#    / \
#   B   C
#  / \
# D   E

from collections import deque

graph = {"A": ["B", "C"], "B": ["A", "D", "E"], "C": ["A"], "D": ["B"], "E": ["B"]}


def dfs_rec(node, target, graph, vis):
    if node == target:
        return True
    vis.add(node)
    for n in graph.get(node, []):
        if n not in vis:
            if dfs_rec(n, target, graph, vis):
                return True
    return False

print(dfs_rec('A', 'C', graph, set()))
print(dfs_rec('A', 'E', graph, set()))
print(dfs_rec('A', 'F', graph, set()))
