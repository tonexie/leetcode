def topological_sort_util(node, visited, stack, graph):
    # Mark the current node as visited
    visited.add(node)
    
    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[node]:
        if neighbor not in visited:
            topological_sort_util(neighbor, visited, stack, graph)
    
    # Push current vertex to stack which stores the result
    stack.append(node)

def topological_sort(graph):
    visited = set()  # Set to keep track of visited nodes
    stack = []       # Stack to store the topological sort order

    # Call the recursive helper function for all vertices
    for node in graph:
        if node not in visited:
            topological_sort_util(node, visited, stack, graph)
    
    # Return the reverse of the stack to get the topological order
    return stack[::-1]

# Example usage
graph = {
    'A': ['C', 'D'],
    'B': ['D'],
    'C': ['E'],
    'D': ['E'],
    'E': []
}

print(topological_sort(graph)) 
