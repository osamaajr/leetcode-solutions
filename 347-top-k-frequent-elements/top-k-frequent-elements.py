




class Solution(object):
    def topKFrequent(self, nums, k):
        
        """
        seen = set()
        sorted_nums = sorted(nums)
        for i in range(1, len(sorted_nums)+1):
            if sorted_nums[i] != sorted_nums[i-1]
                seen.add()
        """

        seen = {}

        for i in sorted(nums):
            if i not in seen:
                seen[i] = 0
            seen[i] += 1

        sorted_keys = sorted(seen, key=seen.get, reverse=True)
        return sorted_keys[:k]
                
                


        
        