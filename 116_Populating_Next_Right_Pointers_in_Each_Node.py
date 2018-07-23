'''
Some thought before writing the code:
1. How to go to the next level? If we have a pointer pointing to the left most child and it is already
connected with its pair, we can traverse the level. So in the parent level, we should connect the
child level already and have a pointer points to the first node of next level.
2. When do we stop? When there is not left child becasue it is a perfect balanced tree, no left child
means there is no next level.
'''
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


def connect(root):
    while root and root.left: # Point 2 above
        next = root.left # Point 1 above
        while root: # Have we finished this level yet?
            root.left.next = root.right
            # Next line means if there is not another node in current level,
            # root.right.next will point to None.
            root.right.next = root.next and root.next.left
            root = root.next
        root = next
