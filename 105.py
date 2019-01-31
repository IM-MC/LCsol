def buildTree(preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """

    if len(inorder) == 0 or len(preorder) == 0:
        return None

    indx = inorder.index(preorder.pop(0))
    root = TreeNode(inorder[indx])
    root.left = buildTree(preorder, inorder[:indx])
    root.right = buildTree(preorder, inorder[indx+1:])
    return root
