# Iterative
def inorderTraversal(root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, result = [], []
        while True:
            while root:
                # Keep going to the left child until we reach the leaf node.
                stack.append(root)
                root = root.left # In order means We need to go to the most left node.
            if not stack:
                return result
            # Now we are at the most left node which should be added first
            node = stack.pop()
            result.append(node.val)
            root = node.right



# Recursive

# Remeber to check base case where the input can be None. I was using root.left and root.right to
# check if there is a left and right child. But in this way i didn't check the empty input case.
def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        self.inorder(root, answer)

        return answer

    def inorder(self, root, answer):
        if root:
            self.inorder(root.left, answer)
            answer.append(root.val)
            self.inorder(root.right, answer)

            
