def kthSmallest(self, root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """

    if not root:
        return 0

    stack = []
    count = 0
    smallest = root.val

    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        count += 1

        if count == k:
            return root.val

        root = root.right
