class Solution(object):
    def removeDuplicates(self, nums):

        if not nums:
            return 0

        index = 1  # position to place next unique number

        for i in range(1, len(nums)):
            if nums[i] != nums[index - 1]:
                nums[index] = nums[i]
                index += 1

        return index
        