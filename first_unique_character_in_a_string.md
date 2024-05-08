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

4回目。nodchipさんの意見を参考に、char_nums -> char_to_counts にrenameした。
以前、変数名に前置詞を入れないというtipsをどこかで見て、それに機械的に従い、dict を表すために to を入れるのを避けていた。

```py
from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_counts = defaultdict(int)
        for c in s:
            char_to_counts[c] += 1
        for index, c in enumerate(s):
            if char_to_counts[c] == 1:
                return index
        return -1
```
