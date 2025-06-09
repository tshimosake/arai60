1回目。答えを見た。
変数名がキャメルケースなのは違和感があるが、入力がキャメルケースなので少し納得した。

```py
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
                
            for i in range(len(word)):
                for ch in range(26):
                    transformed = word[:i] + chr(ord('a') + ch) + word[i+1:]
                    if transformed in wordSet:
                        wordSet.remove(transformed)
                        queue.append((transformed, steps + 1))
        return 0
```

2回目。変数をリネームした（入力はそのままキャメルケースだが、新たに宣言する変数はスネークケースにした。混在するのは欠点だが、入力とローカル変数の区別がしやすい利点もある）。

```py
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, num_steps = queue.popleft()

            if word == endWord:
                return num_steps
                
            for i in range(len(word)):
                for alpha_offset in range(26):
                    transformed_word = word[:i] + chr(ord('a') + alpha_offset) + word[i + 1:]
                    if transformed_word in word_set:
                        word_set.remove(transformed_word)
                        queue.append((transformed_word, num_steps + 1))
        return 0
```

3回目。

```py
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        queue = deque([(beginWord, 1)])

        while queue:
            word, num_steps = queue.popleft()
            if word == endWord:
                return num_steps
            for i in range(len(word)):
                for alpha_offset in range(26):
                    transformed_word = word[:i] + chr(ord('a') + alpha_offset) + word[i + 1:]
                    if transformed_word in word_set:
                        word_set.remove(transformed_word)
                        queue.append((transformed_word, num_steps + 1))
        return 0
```
