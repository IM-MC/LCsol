def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    stack = []
    pre = None

    while root or len(stack) != 0:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()

        if pre != None and root.val <= pre.val:
            return False

        pre = root
        root = root.right

    return True
