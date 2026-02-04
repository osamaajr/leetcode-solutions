"""
for left in arr[int]:
    for right in (left --> end):
        volume = max(maxVol, ((right - left) * min(height[left], height[right])))
 

"""

class Solution(object):
    def maxArea(self, height):
        
        """
        if len(height) < 1:
            return len(height)
        
        maxVol = 0

        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                volume = (right - left) * min(height[left], height[right])
                maxVol = max(maxVol, volume)

        return maxVol
        """


        l = 0
        r = len(height) - 1
        maxVol = 0

        while l < r:
            volume = (r - l) * min(height[l], height[r])
            maxVol = max(maxVol, volume)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxVol

        