# Thought: The insight lies on that we always compare the leftmost child with the
# rightmost child; second leftmost child with second rightmost child. etc.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return self.mirror(root.left, root.right)

    def mirror(self, left, right):
        # Need to make sure children are not None because we are calling left and
        # right attribute on them.

        if not left and not right:
            # If we are at leave node.
            return True
        if not left or not right:
            # If one of leftmost or rightmost child is empty( Not both!)
            return False

        if left.val == right.val:
            out_pair = self.mirror(left.left, right.right)
            in_pair = self.mirror(left.right, right.left)
            return out_pair and in_pair

        return False
