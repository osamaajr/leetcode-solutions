class Solution(object):
    def twoSum(self, nums, target):
        
        for index1, value1 in enumerate(nums):
            for index2, value2 in enumerate(nums[index1 + 1:]):
                if value1 + value2 == target:
                    return index1, index1 + 1 + index2
        