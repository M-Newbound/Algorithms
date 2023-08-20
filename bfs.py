from collections import deque


def bfs_tree(adj_list : list[], start_v):
    size = len(adj_list)
    parent = [None] * size
    state = ["U"] * size #Undiscoved Discovered Processed
    
    bfs_queue = deque()
    bfs_queue.append(start_v)
    state[start_v] = "D"
    
    return bfs_loop(parent, state, bfs_queue, adj_list)


def bfs_loop(parent, state, bfs_queue, adj_list):
    while len(bfs_queue) > 0:
        focus = bfs_queue.popleft()
        
        for (edge_v, edge_w) in adj_list[focus]:
            if state[edge_v] != "U" : continue
            state[edge_v] = "D"
            parent[edge_v] = focus
            bfs_queue.append(edge_v)
        
        state[focus] = "P"
        
    return parent
