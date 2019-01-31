def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    def goThrough(left,right):
        if not right and not left:
            return True
        if not left or not right:
            return False

        if left.val == right.val:
            firstPair = goThrough(left.left, right.right)
            secondPair = goThrough(left.right, right.left)
            return firstPair and secondPair
        else:
            return False

    return root == None or goThrough(root.left, root.right)
