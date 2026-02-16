class Solution(object):
    def lengthOfLastWord(self, s):
        
        res = ''

        for i in reversed(s):
            if not res and i == ' ': # if res is empty (hasnt come across any lettrs yet)
                continue
            elif i == ' ' and res:
                break
            res += i
        return len(res)