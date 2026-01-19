class Solution(object):
    def countBits(self, n):
        
        ans = []

        for i in range(n+1):
            binary = bin(i)
            ones = binary.count('1')
            ans.append(ones)
        return ans
        