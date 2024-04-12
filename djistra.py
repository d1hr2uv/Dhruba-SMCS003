import heapq

def dijkstra(graph, start):
    # Min-heap priority queue
    min_heap = []
    # Initial distances are set to infinity
    distances = {node: float('inf') for node in graph}
    # Distance to the start node is 0
    distances[start] = 0
    # Push the start node onto the queue with a priority of 0
    heapq.heappush(min_heap, (0, start))
    
    visited = set()
    
    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)
        
        # Nodes can get added to the heap multiple times. We only process a vertex the first time we remove it from the heap.
        if current_vertex in visited:
            continue
        
        # Mark the current vertex as visited
        visited.add(current_vertex)
        
        # Check potential paths from the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))
    
    return distances

# Example graph represented as an adjacency list with weights
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {},
    'E': {'D': 1}
}

# Running Dijkstra's algorithm from vertex 'A'
shortest_paths = dijkstra(graph, 'A')
print("Shortest paths from A:", shortest_paths)
