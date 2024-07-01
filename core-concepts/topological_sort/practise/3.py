graph = {
    'A': ['C', 'D'],
    'B': ['D'],
    'C': ['E'],
    'D': ['E'],
    'E': []
}

def top_sort(graph):
  res = []
  def dfs(node, graph, vis):
    vis.add(node)
    for n in graph.get(node, []):
      if n not in vis:
        dfs(n, graph, vis)
    res.append(node)
  
  vis = set()
  
  for node in graph:
    if node not in vis:
      dfs(node, graph, vis)
  
  return res[::-1]

print(top_sort(graph))