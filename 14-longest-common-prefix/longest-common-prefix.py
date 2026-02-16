class Solution(object):
    def longestCommonPrefix(self, strs):

        res = ""
        
        for prefix in range(len(strs[0])):
            for word in strs:
                if word == "":
                    return res
                if (prefix == len(word)) or (word[prefix] != strs[0][prefix]):
                    return res  
            res += strs[0][prefix]
        
        return res
    

            




            

        