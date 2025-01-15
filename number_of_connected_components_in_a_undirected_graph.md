(この問題は leetcode だと課金しないと見られないので、以下の neetcode 内で解いた。https://neetcode.io/problems/count-connected-components)
(ただし、テストケースが19と少ない)

1回目はわからず答えを見た。

```py
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 一つの連結成分内を走査する
        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)

        # 複数（かもしれない）の連結成分それぞれに対し走査する        
        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        return res
```

2回目。変数名を改良した。

```py
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_nodes = [[] for _ in range(n)]
        visited = [False] * n
        for u, v in edges:
            adj_nodes[u].append(v)
            adj_nodes[v].append(u)
        
        def visit_a_node(node):
            for neighbor in adj_nodes[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    visit_a_node(neighbor)
        
        res = 0
        for node in range(n):
            if not visited[node]:
                visit_a_node(node)
                visited[node] = True
                res += 1
        return res
```

3回目。
ある node に隣接した node たちを adj_nodes と呼んだり neighbor と呼んだり呼称が統一されていなかったので、neighbor(s) に統一した。

```py
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors = [[] for _ in range(n)]
        visited = [False] * n
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
    
        def visit_neighbors(node):
            for neighbor in neighbors[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    visit_neighbors(neighbor)
        
        res = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                visit_neighbors(node)
                res += 1
        return res
```
