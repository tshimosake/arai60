1回目。答えを写した。

```py
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1, node2):
            if node1 and node2:
                root = TreeNode(node1.val + node2.val)
                root.left = dfs(node1.left, node2.left)
                root.right = dfs(node1.right, node2.right)
                return root
            else:
                return node1 or node2
        return dfs(root1, root2)
```

2回目。dfs を merge_two_nodes へリネームした。

```py
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge_two_nodes(node1, node2):
            if node1 and node2:
                root = TreeNode(node1.val + node2.val)
                root.left = merge_two_nodes(node1.left, node2.left)
                root.right = merge_two_nodes(node1.right, node2.right)
                return root
            else:
                return node1 or node2
        return merge_two_nodes(root1, root2)
```

3回目。補助関数にも型ヒントをつけた。

```py
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge_two_nodes(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> Optional[TreeNode]:
            if node1 and node2:
                root = TreeNode(node1.val + node2.val)
                root.left = merge_two_nodes(node1.left, node2.left)
                root.right = merge_two_nodes(node1.right, node2.right)
                return root
            else:
                return node1 or node2
        return merge_two_nodes(root1, root2)
```
