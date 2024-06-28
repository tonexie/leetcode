graph = {
    'A': ['C', 'D'],
    'B': ['D'],
    'C': ['E'],
    'D': ['E'],
    'E': []
}


def top_sort(graph):
  topList = []
  
  def dfs(node, visited, graph):
    visited.add(node)
    for n in graph.get(node, []):
      if n not in visited:
        dfs(n, visited, graph)

    topList.append(node)
  
  visited = set()
  for node in graph: # this goes through the keys
    if node not in visited:
      dfs(node, visited, graph)
  
  res = topList[::-1]
  return res


print(top_sort(graph))