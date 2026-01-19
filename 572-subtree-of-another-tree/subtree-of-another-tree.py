# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):

        def sameNode (a, b):
            if not a and not b:
                return True
            elif not a or not b:
                return False
            elif a.val != b.val:
                return False
        
            return sameNode(a.left, b.left) and sameNode(a.right, b.right)

        if not root:
            return False

        if sameNode(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
            



        


        