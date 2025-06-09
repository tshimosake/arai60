1回目Add commentMore actions

```py
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        is_left_to_right = True
        while queue:
            current_level_size = len(queue)
            current_level_vals = []
            next_level_nodes = []
            for _ in range(current_level_size):
                node = queue.popleft()

                current_level_vals.append(node.val)
                # 一段下の node を集め、あとで queue へ追加する
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if is_left_to_right:
                res.append(current_level_vals)
            else:
                res.append(current_level_vals[::-1])
            print(current_level_vals)
                    
            is_left_to_right = not is_left_to_right
        return res
```

2回目
（この文はコードを書いた数日後に書いている。2回目では各レベル（深さ）のノードに対し append する向きを
反転させているが、1回目のコードのように、各レベルのノードを集めてから反転させたほうが直観的な気がする。
なぜ２回目のほうを当時選んだのかは思い出せない...）
（左右を depth の偶奇で判定する[方法](https://github.com/olsen-blue/Arai60/pull/27/files)もあるが、
欲しいのは向き（偶奇）の情報だけなので、最初から bool 値を使うほうが混乱が少ないと思う。）

```py
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        is_left_to_right = True
        while queue:
            current_level_size = len(queue)
            current_level_values = deque()
            for _ in range(current_level_size):
                node = queue.popleft()
                if is_left_to_right:
                    current_level_values.append(node.val)
                else:
                    current_level_values.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(list(current_level_values))
            is_left_to_right = not is_left_to_right
        return result
```

3回目

```py
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])
        left_to_right = True
        while queue:
            current_values = deque()
            current_level_size = len(queue)
            for _ in range(current_level_size):
                node = queue.popleft()
                if left_to_right:
                    current_values.append(node.val)
                else:
                    current_values.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(list(current_values))
            left_to_right = not left_to_right
        return result
```
