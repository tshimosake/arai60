step0. 試行錯誤したが解けなかった。chatGPT にヒントを求めると、貪欲に最長の増加列を取ってもダメだよと言われ納得。

```python3
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = 1
        # 始点を一つ決め、それ以降の部分配列を1個ずつ見ていく
        for i, num in enumerate(nums):
            increasing_nums = [num]
            for later in nums[i+1:]:
                if increasing_nums[-1] < later:
                    increasing_nums.append(later)
            result = max(result, len(increasing_nums))
        return result
```

step1. chatGPTに聞いた（ヒントを求めるうちに回答までたどり着いてしまった、変数名は step2 で調整する）

```py
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i, num in enumerate(nums):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
```

step2. 問題文に O(nlogn)で解けるとあったので、ちょっと考えるが検討もつかず。olsen-blue さんのPRをみてみる。二部探索とあるが、どの配列に対して、何を探すために二部探索するんだ...?
cahtGPTによると tails 法とかいうらしい（ググってもヒットしないが）。なぜこれで答えが求まるのか？しばらく実例を触ったが、なんでこれが思いつくのかしっくりこない。まずdpの解法を3回そらで書けるようにしたほうがいいかも。
→ step1 をちょっとリネームして、わかりやすくした

```python3
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis_length_ending_at = [1] * n
        for i, num in enumerate(nums):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis_length_ending_at[i] = max(
                        lis_length_ending_at[i], 1 + lis_length_ending_at[j]
                    )
        return max(lis_length_ending_at)
```

いくつかあるLISのうち、末尾が最小のものがもっとも伸びしろがあるので、各長さごとにそういうLISの末尾を持っておく、というのが少ししっくりきた。
DPは賢い再帰とのスローガンのもと、再帰問題としてとらえてみる。0 <= i < n に対して、L(i) = 1 + max({L(j) | j < i, nums[j] < nums[i]}) が成り立つことが本質っぽい（ただしL(i)は nums[i] で終わる増加部分列の長さ）。
このあたりを考えていたら、すらすら tails法？が3回書けるようになった。

```py
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for x in nums:
            i = bisect_left(tails, x)
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x
        return len(tails)
```
