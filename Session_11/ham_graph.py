def is_safe(v, adj, path, pos, visited):
    if v not in adj[path[pos - 1]]:
        return False
    if visited[v]:
        return False

    return True


def hamiltonian_cycle_util(adj, path, pos, visited, n):
    if pos == n:
        return path[0] in adj[path[pos - 1]]
    for v in range(1, n):
        if is_safe(v, adj, path, pos, visited):
            path[pos] = v
            visited[v] = True

            if hamiltonian_cycle_util(adj, path, pos + 1, visited, n):
                return True
            visited[v] = False
            path[pos] = -1

    return False

    
def hamiltonian_cycle(adj):
    n = len(adj)
    path = [-1] * n
    visited = [False] * n

    path[0] = 0
    visited[0] = True

    if not hamiltonian_cycle_util(adj, path, 1, visited, n):
        print("No Hamiltonian Cycle")
        return

    for v in path:
        print(v, end=" ")
    print(path[0])  
adj = [
    [1, 3],
    [0, 2, 3, 4],
    [1, 4],
    [0, 1, 4],
    [1, 2, 3]
]

hamiltonian_cycle(adj)

