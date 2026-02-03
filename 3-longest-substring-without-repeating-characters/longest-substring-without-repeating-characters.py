class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        '''
        if len(s) < 2:
            return len(s)

        for x in range(len(s)):
            seen = set()
            count = 0
            max_count = 0
            print(s[x:])
            for i in s[x:]:
                if i not in seen:
                    seen.add(i)
                    count += 1
                else:
                    max_count = max(count, max_count)
                    count = 1 
                    seen = set()

        return max(count, max_count)
        '''

        
        seen = {}
        max_len = 0
        left = 0

        for right in range(len(s)): #abac
            char = s[right]

            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            
            seen[char] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len



        