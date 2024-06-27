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
  stack = deque([start])
  visited = set()
  
  while stack:
    node = stack.pop()
    if node == target:
      return True
    if node not in visited:
      visited.add(node)
      for neighbour in graph.get(node, []):
        if neighbour not in visited:
          stack.append(neighbour)
  return False

if __name__ == "__main__":
  main()