class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        sortedList = sorted(nums)
        for index, value in enumerate(sortedList):
            if index != value:
                print (index, value)
                return index
                
        return (sortedList[-1]+1)
            
        