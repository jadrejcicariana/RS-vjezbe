#Djikstra
import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

def djikstra(graph, start):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    queue = [(0, start)]
    heapq.heapify(queue)

    while queue:
        distance, node = heapq.heappop(queue)

        if distance > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            new_distance = distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))
    return distances

print(djikstra(graph, 'A'))