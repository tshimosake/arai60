1回目。

```py
from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_nums = defaultdict(int)
        for c in s:
            char_nums[c] += 1
        for index, c in enumerate(s):
            if char_nums[c] == 1:
                return index
        return -1
```

2回目。char_nums -> char_counts と rename した。 3回目も同じ。

```py
from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_counts = defaultdict(int)
        for c in s:
            char_counts[c] += 1
        for index, c in enumerate(s):
            if char_counts[c] == 1:
                return index
        return -1
```
