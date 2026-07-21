class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i, num in enumerate(nums):
            temp = target - num
            if temp in mapping:
                return [mapping[temp], i]
            mapping[num] = i