class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        inverse_dict = {}
        for i, val in enumerate(nums):
            if target - val in inverse_dict:
                return [inverse_dict[target - val], i]
            inverse_dict[val] = i