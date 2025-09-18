## step1

高校数学を思い出して、とりあえず解けた。

```py
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        kaijou = [1] * (m + n)
        for i in range(m + n):
            if i == 0:
                kaijou[0] = 1
                continue
            kaijou[i] = kaijou[i-1] * i

        return kaijou[-2] // (kaijou[m - 1] * kaijou[n - 1])
```

## step2

ただの再帰だとTLEだったが、キャッシュデコレータを使ったら通った。キャッシュを使わないとO(2^(m+n))なので、TLEは妥当。

```python3
class Solution:
    @lru_cache
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        return self.uniquePaths(m, n-1) + self.uniquePaths(m-1, n)
```

ボトムアップDPも考えた。

```py
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_of_path = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                num_of_path[i][j] = num_of_path[i-1][j] + num_of_path[i][j-1]
        return num_of_path[m-1][n-1]
```

最初の解法は二項係数のライブラリを使って簡潔に書けると知った：

```py
import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m+n-2, m-1)
```

## step3
すべてを3回そらで書けるようにした。
