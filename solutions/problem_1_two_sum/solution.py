class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mapping = {}
        for i,num in enumerate(nums):
            second_num = target - num
            if second_num in mapping:
                return [mapping[second_num], i]
            mapping[num] = i