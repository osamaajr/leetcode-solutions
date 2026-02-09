"""
hashtable --> char, index (last seen)

firm my left pointer in 0

my right is ohing to loop over each char in s:
    if char has been seen before --> 
    1. shift left piinter to char
    2. update our dict (last seen index)

    else:
        hasnt been seen before -->
        update max --> maxLen = max(maxLen, right - left + 1)


    seen = {
        a : 0,
        b : 1,
        c : 4,
        d : 5
    }

"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        seen = {} #seen char --> char, last seen index
        left = 0
        maxLen = 0

        #right pointer
        for index, value in enumerate(s): #abcccd
            if value in seen and seen[value] >= left:
                left = seen[value] + 1
            
            seen[value] = index
            maxLen = max(maxLen, index - left + 1) # maxLen = 3   left = 3
        return maxLen 

        
            



        
        



        