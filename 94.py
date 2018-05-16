
# Recursive

def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    arr = []
    helper(root, arr)

    def helper(root, arr):
        if root.left != None:
            inorderTraversal(root.left)

        arr.append(root.val)

        if root.right != None:
            inorderTraversal(root.right)

    return arr


# Iterative

def inorderTraversal(root):
    arr, stack = [], []

    while root or len(stack) != 0:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        arr.append(root.val)
        root = root.right

    return arr
