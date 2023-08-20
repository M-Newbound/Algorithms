
def dfs_tree(adj_list, start_v):
    size = len(adj_list)
    parent = [None] * size
    state = ["U"] * size
    
    state[start_v] = "D"
    dfs_loop(adj_list, state, parent, start_v)
    return parent
    

def dfs_loop(adj_list, state, parent, vertex):
    
    for (edge_v, edge_w) in adj_list[vertex]:
        if state[edge_v] != "U": continue
        state[edge_v] = "D"
        parent[edge_v] = vertex
        dfs_loop(adj_list, state, parent, edge_v)
    
    state[vertex] = "P"
