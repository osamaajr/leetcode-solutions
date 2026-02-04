"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
starting with node given:
    add it to out hashmap (to make sure were not recalling it)
        --> if its in the hashmap -> return asssosciated value
    if new:
        create a clone of that node & add to hashmap
        loop through its neighbors appending them to the clone node
        THAT were gonna recur

"""
class Solution(object):
    def cloneGraph(self, node):

        seen = {}

        def dfs(current):

            if not node:
                return None

            if current in seen:
                return seen[current]
            
            clone = Node(current.val)
            seen[current] = clone

            for neighbors in current.neighbors:
                clone.neighbors.append(dfs(neighbors))
            
            return clone 

        return dfs(node)


        
        
        