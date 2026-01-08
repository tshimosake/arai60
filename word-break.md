## step1

5分でわからず ChatGPT に答えを聞いた。以下の回答のような方針は頭によぎったが、二重ループで大丈夫なのかとか、実装が大変そうだななどの不安から手が動かなかった。

```py
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        can_split: list[bool] = [False] * (len(s) + 1)
        can_split[0] = True

        for right in range(1, len(s) + 1):
            for left in range(right):
                if can_split[left] and s[left:right] in word_set:
                    can_split[right] = True
                    break

        return can_split[len(s)]
```

## step2

特に直すところは思いつかないので、ChatGPTにほかの解法を聞く。まず再帰 + メモ化（トップダウンDP）。左端からsを舐めて、その文字から右側を分割できるかを再帰的に求める。

変数名にindexを使っていないのは、indexだと、s内の各文字のindexなのか、文字の間の境界が何番目なのかのどちらかで混乱しそうだったため。

```py
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        longest_word_length = max((len(word) for word in word_set), default=0)
        can_split_from_prefix_length : dict[int, bool] = {}

        def can_split_from(prefix_length: int) -> bool:
            if prefix_length == len(s):
                return True
            if prefix_length in can_split_from_prefix_length:
                return can_split_from_prefix_length[prefix_length]
            max_possible_end = min(len(s), prefix_length + longest_word_length)

            for next_prefix_length in range(prefix_length + 1, max_possible_end + 1):
                if (s[prefix_length:next_prefix_length] in word_set
                    and can_split_from(next_prefix_length)
                ):
                    can_split_from_prefix_length[prefix_length] = True
                    return True
            can_split_from_prefix_length[prefix_length] = False
            return False

        return can_split_from(0)
```

次にBFS。BFSの一般的な形を知れたのはよかった（ノードとエッジを定義し、queueを初期化し、queueが空でない間whileを回し、whileの中ではベースケースか調べ、そうでないなら popleft したノードから遷移できるノードを調べ、queueに追加する。whileが回り切ったらFalseを返す）

例えば `s="leetcode", wordDict = ["leet", "code"]` の場合、0から8までのノードがあり、0から探索を始める。探索の結果、0→4→8という経路が見つかる、という仕組み

```py
from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        max_word_length = max((len(word) for word in word_set), default=0)

        goal_prefix_length: int = len(s)

        visited_prefix_lengths: set[int] = set({0})
        queue = deque([0])

        while queue:
            prefix_length = queue.popleft()
            if prefix_length == goal_prefix_length:
                return True

            max_possible_end = min(goal_prefix_length, prefix_length + max_word_length)
            for next_prefix_length in range(prefix_length + 1, max_possible_end + 1):
                if s[prefix_length:next_prefix_length] not in word_set:
                    continue
                if next_prefix_length not in visited_prefix_lengths:
                    visited_prefix_lengths.add(next_prefix_length)
                    queue.append(next_prefix_length)
        return False
```

Trie というデータ構造を使うのもいいらしいが、すでにだいぶ時間をかけたので後回しにする。

## step3

以下のように再帰+メモ化で3度書いた…が、can_break_from にキャッシュが使えることに気づき、より簡潔にできた

```py
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        longest_word_length: int = max((len(w) for w in word_set), default = 0)

        @cache
        def can_break_from(prefix_length: int) -> bool:
            # 基本ケース
            if prefix_length == len(s):
                return True

            # 再帰ケース
            max_possible_end = min(len(s), prefix_length + longest_word_length)
            for next_prefix_length in range(prefix_length + 1, max_possible_end + 1):
                if (s[prefix_length:next_prefix_length] in word_set 
                and can_break_from(next_prefix_length)
                ):
                    return True
            return False
        return can_break_from(0)
```
