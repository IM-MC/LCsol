 def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    array = []
    queue = []
    queue.insert(0,root)
    while len(queue) != 0:
        curr = []
        for _ in range(len(queue)):
            node = queue.pop()
            if node != None:
                queue.insert(0,node.left)
                queue.insert(0,node.right)
                curr.append(node.val)
        if len(curr) > 0:
            array.append(curr)
    return array
