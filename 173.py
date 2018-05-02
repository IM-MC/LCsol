class BSTIterator(object):
    def __init__(root):
        """
        :type root: TreeNode
        """

        stack = []
        self.pushAll(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """

        node = self.stack.pop()
        value = node.val
        self.pushAll(node.right)
        return value

    def pushAll(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left
