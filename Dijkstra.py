######### calculate shortest path using dijkstra algorithm
nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
unvisited = {node: None for node in nodes}
# print(unvisited)
shortest_path = {}

def dijkstra(s_node):
    current = s_node
    currentDistance = 0
    unvisited[current] = currentDistance
    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited:
                continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        shortest_path[current] = currentDistance
        del unvisited[current]
        if not unvisited: 
            break
        candidates = [node for node in unvisited.items() if node[1]]
#         print(candidates)
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
#         print(current)
#         print(currentDistance)
    
distances = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}

print('Given nodes : ',nodes)
initial_node=input('Enter a starting node : ').upper()
dijkstra(initial_node)
print('shortest distance from  {} node to other nodes are :'.format(initial_node))
print(shortest_path)