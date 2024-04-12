def kosaraju_scc(graph):
    def dfs(v, graph, visited, stack):
        visited.add(v)
        for neighbor in graph.get(v, []):
            if neighbor not in visited:
                dfs(neighbor, graph, visited, stack)
        stack.append(v)
    
    def dfs_assign(v, graph, visited, component):
        visited.add(v)
        component.add(v)
        for neighbor in graph.get(v, []):
            if neighbor not in visited:
                dfs_assign(neighbor, graph, visited, component)

    # First pass: order vertices by finish time
    visited = set()
    stack = []
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex, graph, visited, stack)
    
    # Second pass: process nodes in reverse postorder
    visited.clear()
    sccs = []
    reverse_graph = {v: [] for v in graph}
    for v in graph:
        for w in graph[v]:
            reverse_graph[w].append(v)
    while stack:
        v = stack.pop()
        if v not in visited:
            component = set()
            dfs_assign(v, reverse_graph, visited, component)
            sccs.append(component)
    
    return sccs

def solve_2sat(variables, clauses):
    graph = {}
    # Build the graph
    for x, y in clauses:
        if x not in graph:
            graph[x] = []
        if -x not in graph:
            graph[-x] = []
        if y not in graph:
            graph[y] = []
        if -y not in graph:
            graph[-y] = []
        graph[-x].append(y)
        graph[-y].append(x)
    
    # Find SCCs
    sccs = kosaraju_scc(graph)
    scc_lookup = {}
    for scc in sccs:
        for node in scc:
            scc_lookup[node] = scc
    
    # Check for contradictions
    for v in range(1, variables + 1):
        if scc_lookup[v] == scc_lookup[-v]:
            return False
    return True

# Example usage
variables = 3
clauses = [(1, 2), (-1, 3), (-2, -3)]  # x1 ∨ x2, ¬x1 ∨ x3, ¬x2 ∨ ¬x3
print(solve_2sat(variables, clauses))
