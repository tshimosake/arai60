一回目。答えを見た。

```py
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        queue = [(root, 1)]
        while queue:
            node, depth = queue.pop(0)
            if node.left is None and node.right is None:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
```

2回目と3回目。子ノードが None かどうかの判定は（1つ目と2, 3個目で）そろえたほうがよいと判断した。

```py
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = [(root, 1)]
        while queue:
            node, depth = queue.pop(0)
            if node.left is None and node.right is None:
                return depth
            if node.left is not None:
                queue.append((node.left, depth + 1))
            if node.right is not None:
                queue.append((node.right, depth + 1))
```
