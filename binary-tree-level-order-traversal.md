1回目。25分で解けた。

```py
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs だねえ、てことはキューか？
        if root is None:
            return []
        
        queue = [(root, 0)]
        res = [[]]
        while queue:
            node, depth = queue.pop(0)
            # 1 level 下のを queue に入れる
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
            
            # res[depth] していいのは、len(res) > depth のとき
            if len(res) > depth:
                res[depth].append(node.val)
            else:
                res.append([node.val])
        return res            
```

2回目。Gemini に聞いて、level ごとに for ループを回したほうが level order traversal としては標準的だし直観的と指摘される。
3回目も同様。

```py
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            current_level_vals = []
            current_level_size = len(queue)
            for _ in range(current_level_size):
                node = queue.popleft()
                current_level_vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(current_level_vals)
        return res
```
