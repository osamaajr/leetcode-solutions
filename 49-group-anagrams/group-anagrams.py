"""
combinations = {} 

loop through the array:
    loop through combinations:
    if in combinations:
        add value
    else:
        create new key
        add value


"""


class Solution(object):
    def groupAnagrams(self, strs):
        

        combinations = {}

        for word in strs:

            #get array of letters in the word
            letters = "".join(sorted(word))

            if letters not in combinations:
                combinations[letters] = []
            combinations[letters].append(word)



        return list(combinations.values())
            
        