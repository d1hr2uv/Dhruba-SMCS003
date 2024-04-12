'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def kosaraju_scc(graph):
    def dfs_iterative(v, graph, visited, stack=None):
        """Perform an iterative DFS, either to fill the stack or collect SCC."""
        s = []
        s.append(v)
        result = []
        while s:
            node = s[-1]
            if node not in visited:
                visited.add(node)
                result.append(node)
                s.extend([x for x in graph[node] if x not in visited])
            else:
                if stack is not None and node in visited:
                    stack.append(node)
                s.pop()
        return result

    # Step 1: Reverse the graph
    reverse_graph = {v: [] for v in graph}
    for v in graph:
        for w in graph[v]:
            reverse_graph[w].append(v)

    # Step 2: First pass to fill the order stack
    visited = set()
    stack = []
    for v in graph:
        if v not in visited:
            dfs_iterative(v, reverse_graph, visited, stack)

    # Step 3: Second pass to get the SCCs
    visited.clear()
    scc_list = []
    while stack:
        v = stack.pop()
        if v not in visited:
            scc = dfs_iterative(v, graph, visited)
            scc_list.append(scc)

    # Calculate sizes and return the five largest
    scc_sizes = sorted([len(scc) for scc in scc_list], reverse=True)
    return scc_sizes[:5]

# Example graph structure: adjacency list
complex_graph = {
    0: [1],
    1: [2],
    2: [3, 4],  # Makes a cycle back to 0 through 4
    3: [0],
    4: [5],  # Connection to another SCC
    5: [6],
    6: [7],
    7: [5],  # Completes the cycle for 5, 6, 7
    8: [9],
    9: [10],  # Linear connection, not forming a cycle
    10: [],
    11: [11],  # Self-loop, trivial SCC
    12: [13],
    13: [14],
    14: [15],
    15: [12, 14],  # Complex cycle involving 12, 13, 14, 15
    16: []  # Isolated node
}


biggest_scc_sizes = kosaraju_scc(complex_graph)

print("Sizes of the five largest SCCs:", biggest_scc_sizes)
