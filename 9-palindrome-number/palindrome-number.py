class Solution(object):
    def isPalindrome(self, x):
        
        strX = str(x)
        if x >= 0:
            revstrX = strX[::-1]

            if revstrX == strX:
                return True
        return False