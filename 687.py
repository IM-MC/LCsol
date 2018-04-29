def longestUnivaluePath(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    longest = [0]

    def traverse(node):
        if node == None:
            return 0
        len_left = traverse(node.left)
        len_right = traverse(node.right)

        left = 0
        right = 0
        if node.left and node.left.val == node.val:
            left = len_left + 1
        if node.right and node.right.val == node.val:
            right = len_right + 1

        longest[0] = max(longest[0], left+right)
        return max(left,right)
    traverse(root)
    return longest[0]
