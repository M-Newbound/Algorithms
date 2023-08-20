
def distance_matrix(adj_list):
    returned_m = [ [float('inf')] * len(adj_list) for _ in adj_list]

    for i in range(len(adj_list)):
        returned_m[i][i] = 0
        for j, e_w in adj_list[i]:
            returned_m[i][j] = e_w            
    return returned_m


import copy
def floyd(distance):
    dis = copy.deepcopy(distance)
    size = len(distance[0])

    for k in range(size):
        for i in range(size):
            for j in range(size):
                if dis[i][j] > dis[i][k] + dis[k][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]
    return dis

