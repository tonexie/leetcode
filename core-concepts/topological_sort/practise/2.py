graph = {
    'A': ['C', 'D'],
    'B': ['D'],
    'C': ['E'],
    'D': ['E'],
    'E': []
}


def top_sort(graph):
  def dfs(node, graph, topList, visited):
    visited.add(node)
    for n in graph.get(node, []):
      if n not in visited:
        dfs(n, graph, topList, visited)
    topList.append(node)
    
  visited = set()
  topList = []
  
  for node in graph:
    if node not in visited:
      dfs(node, graph, topList, visited)
  
  return topList[::-1]

print(top_sort(graph))