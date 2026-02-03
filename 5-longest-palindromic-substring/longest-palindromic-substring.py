"""
ODD
loop over each character w/ left and right pointer:
    while charcters are equal and in bound:
        update max string
        expand either way
        

EVEN


"""


class Solution(object):
    def longestPalindrome(self, s):
        maxString = ''

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(maxString) < (r-l+1):
                    maxString = s[l:r+1]
                l -= 1
                r += 1

            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(maxString) < (r-l+1):
                    maxString = s[l:r+1]
                l -= 1
                r += 1

        return maxString





        
        
        