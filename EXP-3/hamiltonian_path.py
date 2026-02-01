class Solution:
    def check(self, n, m, edges):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        def dfs(node, visited, count):
            if count == n:
                return True
            for next_node in adj[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    if dfs(next_node, visited, count + 1):
                        return True
                    visited[next_node] = False 
            return False
        for i in range(n):
            visited = [False] * n
            visited[i] = True
            if dfs(i, visited, 1):
                return 1
        return 0

                    