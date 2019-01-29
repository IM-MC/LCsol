def isUnivalTree(root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    def traverseHelp(root, value):
        if root.val != value:
            return False

        checker1 = True
        checker2 = True

        if root.left:
            checker1 = traverseHelp(root.left, root.val)
        if root.right:
            checker2 = traverseHelp(root.right, root.val)

        if not checker1 or not checker2:
            return False
        else:
            return True

    return traverseHelp(root, root.val)
