"""
2 loops:

1) outside loop: left pointer
2) inside loop: right pointer
left pointer only moves across the string ones the right pointer scans the scans the string after the pointer

for each scan:
    check if = [::-1]

    if it is, count += 1

abcd

“Although the loops look O(n²), the string slicing and reversal inside make the overall complexity O(n³).”

"""


"""
        count = 0

        for left in range(len(s)):
            for right in range(left, len(s)):
                spliced_s = s[left:right+1]
                if spliced_s == spliced_s[::-1]:
                    count += 1

        return count 
"""

'--------------------------------------------------------------'

"""
EXPANDING AROUND THE CENTRE
left pointer = l
right pointer = r

# ODD PALIDROMES
for loop through each char in s:
    l, r = char were on

    WHILE
    1. check if theyre in bounds --> l > 0 && r < len(s)
    2. if l and r are EQUAL

        increment l -= 1 r += 1
        count += 1

#EVEN PALINDROMES
for loop through each char in s:
    l = i
    r = i+1

    WHILE
    1. check if theyre in bounds --> l > 0 && r < len(s)
    2. if l and r are EQUAL

        increment l -= 1 r += 1
        count += 1


"""
class Solution(object):
    def countSubstrings(self, s):

        if len(s) < 1:
            return len(s)
        
        count = 0
        
        #abad


        for i in range(len(s)): #traverse indexes (not values)

            #ODD
            l = i # left = 0
            r = i # right = 0

            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1 
                l -= 1
                r += 1
            
            # count = 1

            #EVEN
            l = i   # left = 0
            r = i+1 # right = 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count 


        