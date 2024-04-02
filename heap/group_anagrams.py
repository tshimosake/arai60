class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_word_to_words = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in sorted_word_to_words:
                sorted_word_to_words[sorted_word] = []
            sorted_word_to_words[sorted_word].append(word)
        return list(sorted_word_to_words.values())