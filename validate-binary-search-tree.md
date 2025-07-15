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
