def levelOrderBottom(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    arr = []

    def goDown(root, level, arr):
        if root:
            if len(arr) <= level:
                arr.insert(0, [])
            arr[-(level+1)].append(root.val)
            goDown(root.left, level+1, arr)
            goDown(root.right, level+1, arr)

    goDown(root, 0, arr)

    return arr
