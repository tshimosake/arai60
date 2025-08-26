1回目。自分で解くのにこだわり、数時間かかってなんとか解いた。変数名はstep2で改良する。
ただ、しばらく考えて再帰構造に気づいたりして、だんだんと答えに迫っていくのは楽しかった。

```py
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    
        # 基本ケース
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
    
        # 再帰ケース
        root_val = preorder[0]
        # print(f"{root_val=}")
        root = TreeNode(root_val)
    
        index = inorder.index(root_val)
        len_left = len(inorder[:index])
        len_right = len(inorder[index + 1 :])
        # print(f"{index=}, {len_left=}, {len_right=}")
    
        root.left = self.buildTree(
            preorder[1 : len_left + 1],
            inorder[:index],
        )
        root.right = self.buildTree(
            preorder[-len_right:] if len_right > 0 else [],
            inorder[index + 1 :],
        )
    
        return root
```

2,3回目。inorder.index() のせいで時間計算量が O(n^2) だが、自分で解けた解法なのでこのまま行った。
ただ他人のコード（出典失念）を調べていて、配列の値がすべて相異なることから、index -> 値の逆写像を作って、O(n)にできることを知った（後述）。
あまりコードに本質的な変更はなく簡単だが、ヘルパー関数なしで buildTree() のみで再帰できるこっちのほうが（見た目は）好みだった。

```py
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 基本ケース
        if not preorder:
            return None

        # 再帰ケース
        root_val = preorder[0]
        root_index = inorder.index(root_val)
        root = TreeNode(root_val)

        root.left = self.buildTree(
            preorder[1 : 1 + root_index],
            inorder[:root_index],
        )
        root.right = self.buildTree(
            preorder[1 + root_index :],
            inorder[root_index + 1 :],
        )

        return root
```

上述の、O(n) の解法。

```py
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 値 -> inorder 上のインデックスを事前計算
        index_map = {val: i for i, val in enumerate(inorder)}
        n = len(preorder)
        pre_index = 0

        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            nonlocal pre_index
            if in_left > in_right:
                return None

            root_val = preorder[pre_index]
            root_index = index_map[root_val]
            pre_index += 1

            root = TreeNode(root_val)
            root.left = helper(in_left, root_index - 1)
            root.right = helper(root_index + 1, in_right)
            return root

        return helper(0, n - 1)
```
