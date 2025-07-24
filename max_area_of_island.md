1回目。変数名などのコードの作法は気にしていない。

```py
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            nonlocal count
            if (
                not (0 <= i < m and 0 <= j < n)
                or grid[i][j] == 0
            ):
                return 
            count += 1
            grid[i][j] = 0
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
        
        res = 0
        for i in range(m):
            for j in range(n):
                count = 0
                dfs(i, j)
                res = max(res, count)
        return res
```

2,3回目

```py
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()

        def count_area(i, j) -> int:
            if (
                not (0 <= i < m and 0 <= j < n) 
                or (i, j) in visited 
                or grid[i][j] == 0
            ):
                return 0

            visited.add((i, j))
            area = 1
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for delta_i, delta_j in directions:
                area += count_area(i + delta_i, j + delta_j)
            return area

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, count_area(i, j))
        return res
```
