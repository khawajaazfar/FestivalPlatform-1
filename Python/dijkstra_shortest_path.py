import heapq

def dijkstra(graph, start):
    """
    Compute shortest paths from a start node to all other nodes in the graph.
    Graph is represented as an adjacency list:
    { 'A': [('B', 4), ('C', 2)], 'B': [('C', 5), ('D', 10)], ... }
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # (distance, node)

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        # Skip outdated distances
        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

if __name__ == "__main__":
    print("🚀 Dijkstra’s Shortest Path Finder 🚀")
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 5), ('D', 10)],
        'C': [('E', 3)],
        'D': [('F', 11)],
        'E': [('D', 4)]
    }
    start = input("Enter the starting node (A-F): ").upper()
    if start not in graph:
        print("Invalid node!")
    else:
        result = dijkstra(graph, start)
        print("\n📍 Shortest distances from", start)
        for node, dist in result.items():
            print(f"{node}: {dist}")
