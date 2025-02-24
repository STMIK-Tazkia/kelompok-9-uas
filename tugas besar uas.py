import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Contoh graf (merepresentasikan lokasi dan jarak antar lokasi)
graph = {
    'Gudang': {'Lokasi A': 10, 'Lokasi B': 5},
    'Lokasi A': {'Lokasi C': 15, 'Lokasi D': 20},
    'Lokasi B': {'Lokasi D': 10, 'Lokasi E': 25},
    'Lokasi C': {'Lokasi F': 5},
    'Lokasi D': {'Lokasi F': 10},
    'Lokasi E': {'Lokasi F': 10},
    'Lokasi F': {}
}

# Menjalankan algoritma Dijkstra dari gudang
shortest_paths = dijkstra(graph, 'Gudang')

# Menampilkan hasil
print("Jalur terpendek dari Gudang ke lokasi lain:")
for location, distance in shortest_paths.items():
    print(f"{location}: {distance}")