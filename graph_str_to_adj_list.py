def adjacency_list(graph_str):
    lines = graph_str.splitlines()
    
    directed = "D" in lines[0]
    
    size = int(lines[0].split()[1])
    adj = [[] for i in range(size)]

    for i in range(1, len(lines)):
        edge = lines[i].split()

        from_index, to_index = (int(edge[0]), int(edge[1]))
        weight = None if len(edge) <= 2 else int(edge[2])

        adj[from_index].append((to_index, weight))
        if not directed : adj[to_index].append((from_index, weight))
    return adj
