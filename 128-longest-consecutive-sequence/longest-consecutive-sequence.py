class Solution(object):
    def longestConsecutive(self, nums):
        
        nums.sort()
        count = 1
        max_count = 0

        if len(nums) == 0:
            return 0

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                continue
            elif nums[i] == nums[i+1] - 1:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 1
        
        print(max_count)
        print(count)
        return max(count, max_count)
        