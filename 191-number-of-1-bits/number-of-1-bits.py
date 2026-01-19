class Solution(object):
    def hammingWeight(self, n):
        
        count = 0
        for i in (bin(n)[2:]):
            if i == "1":
                count += 1
        return count

        