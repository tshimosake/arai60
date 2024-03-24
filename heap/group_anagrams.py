class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        temp_dict = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in temp_dict:
                temp_dict[sorted_word] = []
            temp_dict[sorted_word].append(word)
        return temp_dict.values()