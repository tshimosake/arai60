1回目。
nums[mid + 1] でエラーが起きると思ったが、範囲外をスライス記法で切り出した場合は空配列が返るのでOK。

```py
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 基本ケース
        if len(nums) == 0:
            return None
        # 再帰ケース
        mid = len(nums) // 2
        res = TreeNode(nums[mid])
        res.left = self.sortedArrayToBST(nums[:mid])
        res.right = self.sortedArrayToBST(nums[mid + 1:])
        return res
```

2回目。特に直すところは思いつかなかったので省略する（mid を mid_index にしてもよいが、好みの範囲か）。
1回目では nums の長さが偶数のときに右側を mid にしているが、左側を mid にもできる。
問題の description 上の例がこれに対応していて、 nums = [-10,-3,0,5,9] に対する
- 一つ目の回答 [0,-3,9,-10,null,5] は mid として右側を
- 二つ目の回答 [0,-10,5,null,-3,null,9] は mid として左側を
とったもの。
mid を右側にしたのは、単に len(nums) // 2 が (len(nums)  - 1) // 2 より簡潔だから。

3回目も特に変化なし。

提出後の追記：
nodchip さん、odaさんに指摘され、スライスによるコピーを作らないケースを実装した。
かなり高速化できたようで、実際、leetcode 上で計算速度は beats 100% と出た。

```py
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_bst_from_range(left_index: int, right_index: int) -> Optional[TreeNode]:
            # 基本ケース
            if left_index > right_index:
                return None
            # 再帰ケース
            mid = (left_index + right_index) // 2
            res = TreeNode(nums[mid])
            res.left = build_bst_from_range(left_index, mid - 1)
            res.right = build_bst_from_range(mid + 1, right_index)
            return res
        return build_bst_from_range(0, len(nums) - 1)
```
