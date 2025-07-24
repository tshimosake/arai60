答えを見た。1回目

```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i:int, j:int) -> None:
            # 範囲外または海なら返す
            if not 0 <= i < len(grid) \
            or not 0 <= j < len(grid[0]) \
            or grid[i][j] == '0':
                return
            
            grid[i][j] = '0'

            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)
        
        num_of_islands = 0
        for i, row in enumerate(grid):
            for j, num in enumerate(grid[i]):
                if grid[i][j] == '1':
                    num_of_islands += 1
                    dfs(i, j)
        return num_of_islands
```

2回目と3回目。

```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0]))\
            or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
            return
        
        res = 0
        for i, _ in enumerate(grid):
            for j, char in enumerate(grid[i]):
                if char == '1':
                    res += 1
                dfs(i,j)
        return res
```
