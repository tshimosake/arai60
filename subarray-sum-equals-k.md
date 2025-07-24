自分で書いてTLEしたもの。

```py
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        for index, num in enumerate(nums):
            sum = 0
            j = 0
            while index + j <= len(nums) - 1:
                sum += nums[index + j]
                j += 1
                if sum == k:
                    res += 1
        return res
```

1回目：解答を見てなんとかアクセプト。

```py
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        sum_to_counts = defaultdict(int)
        sum_to_counts[0] = 1
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum - k in sum_to_counts:
                res += sum_to_counts[current_sum - k]
            sum_to_counts[current_sum] += 1
        return res
```

2回目：renameとif節の削除。

```py
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        current_sum = 0
        sum_count = defaultdict(int)
        sum_count[0] = 1
        for num in nums:
            current_sum += num
            res += sum_count[current_sum - k]
            sum_count[current_sum] += 1
        return res
```

3回目：current -> cur とrename.

```py
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        sum_count = defaultdict(int)
        sum_count[0] = 1
        for num in nums:
            cur_sum += num
            res += sum_count[cur_sum - k]
            sum_count[cur_sum] += 1
        return res
```
