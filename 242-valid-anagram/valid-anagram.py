class Solution(object):
    def isAnagram(self, s, t):
        
        if len(t) != len(s):
            return False

        for char in s:
            if char in t:
                t = t.replace(char, " ", 1)
            else:
                return False
        return True
        
        
        
        
        