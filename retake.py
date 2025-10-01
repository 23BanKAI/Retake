import heapq
from collections import defaultdict

def dijkstra(graph, start):
    # Собираем все вершины: источники и назначения
    vertices = set(graph.keys())
    for edges in graph.values():
        for v, w in edges:
            vertices.add(v)

    dist = {v: float('inf') for v in vertices}
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    
    return dist

def build_graph():
    graph = defaultdict(list)
    
    # Ввод складов
    warehouses = input("Введите номера складов через пробел: ").split()
    warehouses = [w.strip() for w in warehouses]
    
    # Ввод пунктов выдачи
    stores = input("Введите номера пунктов выдачи через пробел: ").split()
    stores = [s.strip() for s in stores]
    
    # Ввод рёбер
    n = int(input("Введите количество дорог/путей: "))
    print("Введите дороги в формате: источник пункт_назначения время_доставки")
    for _ in range(n):
        u, v, w = input().split()
        w = float(w)
        graph[u].append((v, w))
    
    return graph, warehouses, stores

def main():
    graph, warehouses, stores = build_graph()
    
    print("\nКратчайшее время доставки от складов до пунктов выдачи:")
    print(f"{'Склад':<10}", end='')
    for store in stores:
        print(f"{store:<10}", end='')
    print()
    
    for w in warehouses:
        dist = dijkstra(graph, w)
        print(f"{w:<10}", end='')
        for s in stores:
            time = dist.get(s, float('inf'))
            if time == float('inf'):
                print(f"{'∞':<10}", end='')
            else:
                print(f"{time:<10}", end='')
        print()

if __name__ == "__main__":
    main()
