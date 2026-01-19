class Solution(object):
    def isPalindrome(self, s):

        res = ""
        for char in s:
            if char.isalnum():
                res += char
        
        res = res.lower()
        resRev = res[::-1]
        
        if res == resRev:
            return True
        return False
        
         
        

        