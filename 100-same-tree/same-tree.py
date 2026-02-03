# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
compare p and q

TRAVERSE
if same:
    go left on both --> compare
    go right on both --> compare

    left and right comparitions == true
    recur traverse


if not same:
    return False


EDGE CASES
p is in q (or viceversa)
both empty

"""

class Solution(object):
    def isSameTree(self, p, q):
        

        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    