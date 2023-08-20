
def is_strongly_connected(adj_list):
    for v in range(len(adj_list)):
        parent = dfs_tree(adj_list, v)
        parent[v] = v
        if None in parent : return False
    return True
