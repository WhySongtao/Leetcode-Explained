# Firstly, when seeing preorder, inorder, I will have a think about their property firstself.
# Preorder: we will visit the root node first.
# Inorder: we will visit all the left child first and then root node and then right child.
# So the idea is to find the value of root node from Preorder, then use this value to find the
# index of the root node from Inorder. Based on this index, we can figure out all the left child
# and the right child. Then we apply the same process for the left child and right child until there
# aren't any node or there are only one node.

def buildTree(preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    # Two base cases
    if len(preorder) == 0:
        return
    if len(preorder) == 1:
        return TreeNode(preorder[0])

    # Preorder: first element is the root.
    root_value = preorder[0]
    root = TreeNode(root_value)

    # Find the index of the root in inorder so that we can separate left and right child.
    index_of_root = inorder.index(root_value)

    # Find the left and right child from inorder
    left_inorder = inorder[:index_of_root] # index_of_root is the root node, we don't need that.
    right_inorder = inorder[index_of_root+1:]

    # Find the left and right child from preorder
    # One trick here to make sure the index are correct: the sub child from Preorder
    # and Inorder should have the same number of children.
    left_preorder = preorder[1:index_of_root+1]
    right_preorder = preorder[index_of_root+1:]

    root.left = buildTree(left_preorder, left_inorder)
    root.right = buildTree(right_preorder, right_inorder)

    return root
