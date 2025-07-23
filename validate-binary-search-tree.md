1回目。Gemini に聞いた

```py
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode], lower_bound: float, upper_bound: float) -> bool:
            if node is None:
                return True
            if not (lower_bound < node.val < upper_bound):
                return False
            
            is_left_valid = validate(node.left, lower_bound, node.val)
            is_right_valid = validate(node.right, node.val, upper_bound)
            return is_left_valid and is_right_valid
        return validate(root, float("-inf"), float("inf"))
```

2回目。ほかの人のコードを見る。
- これはとても勉強になる：https://github.com/quinn-sasha/leetcode/pull/27/files#r2200377284
- in-order に探索する方法を知った：https://discord.com/channels/1084280443945353267/1192736784354918470/1234120299008491581
  - 以下は Gemini による回答
  ```py
  class Solution:
      def isValidBST(self, root: TreeNode) -> bool:
          # 直前に訪れたノードの値を保持する。
          # 初期値はマイナス無限大にしておく。
          # リストを使っているのは、再帰呼び出し間で値を共有・変更可能にするため。
          self.prev_val = float('-inf')

          def inorder_traversal(node):
              if not node:
                  return True

              # 1. 左の部分木を探索
              if not inorder_traversal(node.left):
                  return False

              # 2. 現在のノードを処理
              #    現在のノードの値が直前の値以下なら、BSTではない
              if node.val <= self.prev_val:
                  return False
              # 直前の値を現在のノードの値で更新
              self.prev_val = node.val

              # 3. 右の部分木を探索
              if not inorder_traversal(node.right):
                  return False
            
              return True

          return inorder_traversal(root)
    ```
  - 他人のコードを読むのつらいなあ...

3回目。1回目のまま終了。
