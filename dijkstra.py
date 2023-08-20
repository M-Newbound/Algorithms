
def next_vertex(in_tree, distance):
    next_v = None
    for i in range(len(in_tree)):
        if in_tree[i] : continue
        if next_v is None : next_v = i
        if distance[next_v] > distance[i] : next_v = i
    return next_v


def dijkstra(adj_list, start_v):
    size = len(adj_list)
    in_tree = [False] * size
    distance = [float('inf') for _ in size]
    parent = [None] * size
    
    distance[start_v] = 0
    
    while False in in_tree:
        next_v = next_vertex(in_tree, distance)
        in_tree[next_v] = True
        
        for (edge_v, edge_w) in adj_list[next_v]:
            if in_tree[edge_v] : continue
            if edge_w > distance[edge_v] : continue
            distance[edge_v] = edge_w
            parent[edge_v] = next_v
