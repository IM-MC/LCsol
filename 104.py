def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """

    if not root:
        return 0
    else:
        return max(maxDepth(root.left), maxDepth(root.right))
