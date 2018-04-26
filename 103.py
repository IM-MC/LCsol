def zigzagLevelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    array = []
    queue = []
    queue.insert(0,root)
    while len(queue) != 0:
      curr = []
      for i in range(0,len(queue)):
        node = queue.pop()
        if node != None:
          queue.insert(0, node.right)
          queue.insert(0, node.left)
          if len(array)%2 == 0:
            curr.insert(0, node.val)
          else:
            curr.append(node.val)
      if len(curr) > 0:
        array.append(curr)
    return array
