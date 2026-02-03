# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
starting at root -->
left subtree values must all be less than root
right subtree values must all be more than root
must contain both children (or none for when it reaches the end)

SOLUTION:

LEFT SUBTREE LOOP:
loops through all children in right subtree (starting at left child)-->
    checks if less -> returns True

RIGHT SUBTREE LOOP:
loops through all children in right subtree (starting at right child) -->
    checks if more -> returns True


COMBINE:
    check all children --> recur that one function
"""

class Solution(object):
    def isValidBST(self, root):

        """
        if root is None:
            return True

        if root.left is not None and root.right is not None:
            if root.val > root.left.val and root.val < root.right.val:
                self.isValidBST(root.left)
                self.isValidBST(root.right)
                return True
            else:
                return False
        else:
            return False

        return ??
        """

        """
        def leftSubTree(leftNode):
            if leftNode.left is None and leftNode.right is None:
                return True
            if leftNode.left is None or leftNode.right is None:
                return False

            if leftNode.left.val < root.val and leftNode.right.val < root.val:
                if self.leftSubTree(leftNode.left) and self.leftSubTree(leftNode.right):
                    return True
                else: return False
            else:
                return False
        
        def rightSubTree(rightNode):
            if rightNode.left is None and rightNode.right is None:
                return True

            print("rightSubTree",rightNode.left, rightNode.right)
            if rightNode.left.val > root.val and rightNode.right.val > root.val:
                self.rightSubTree(rightNode.left)
                self.rightSubTree(rightNode.right)
                return True
            else:
                return False
        
        def callBoth(right, left):
            if right and left:
                rightSubTree(right)
                leftSubTree(left)
            elif right is None and left is None:
                return True
            else:
                return False
 
        return callBoth(root.right, root.left)
        """
        """
        def leftSubTree(leftNode):
            if leftNode is None:
                return True

            if leftNode.val >= root.val:
                return False

            return self.leftSubTree(leftNode.left) and self.leftSubTree(leftNode.right)

        
        def rightSubTree(rightNode):
            if rightNode is None:
                return True

            if rightNode.val <= root.val:
                return False

            return self.rightSubTree(rightNode.left) and self.rightSubTree(rightNode.right)

    
        return rightSubTree(root.right) and leftSubTree(root.left)
        """
        
        def validate(node, low, high):
            if node is None:
                return True

            if not (low < node.val < high):
                return False

            return (
                validate(node.left, low, node.val) and
                validate(node.right, node.val, high)
            )

        return validate(root, float('-inf'), float('inf'))



        
        

        