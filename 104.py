def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """

    def height(root):
        if not root:
            return 0

        return max(height(root.left)+1, height(root.right)+1)

    return height(root)
