def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    return root == None or helper(root.left, root.right)

def helper(left, right):
    if left == None or right == None:
        return left == right
    if left.val != right.val:
        return False
    return helper(left.left, right.right) and (left.right, right.left)
