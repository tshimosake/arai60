問題リンク：https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

## step1
5分考えて答えを見た。価格をチャートで想像すれば、単に貪欲にやればよいとわかった

```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        for today in range(1, len(prices)):
            if prices[today] > prices[today - 1]:
                total_profit += prices[today] - prices[today - 1]
        return total_profit
```

いや、貪欲でできる理由がよくわかっていなかった。最適解を $\sum_{k=1}^{n-1} \max(0, p_k - p_{k-1})$ と分解できることが本質だった。

## step2
ほかの回答は長くてなかなか読む気にならない…

二状態DP：各日で株を持っている/持っていない場合の最大利益を更新していって、最後に持っていない場合の最大利益を返す。関数呼び出しが頻繁にあるからか、少し遅くなった

```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_without_stock = 0
        profit_with_stock = -prices[0]
        for today in range(1, len(prices)):
            next_profit_without_stock = max(
                profit_without_stock, # そのまま買わない
                profit_with_stock + prices[today]    # 売る
            )
            next_profit_with_stock = max(
                profit_with_stock,  # 売らずに持ち続ける
                profit_without_stock - prices[today]    # 新たに買う
            )
            profit_without_stock, profit_with_stock = (
                next_profit_without_stock, next_profit_with_stock
            )
        return profit_without_stock
```

## step3
最初の step1 がもっとも素直だと思ったので、これを採用する
