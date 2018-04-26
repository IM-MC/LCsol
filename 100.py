 def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    return same(p,q)

def same(p, q):
    if p == None and q == None:
        return True
    if p == None or q == None:
        return False
    if p.val == q.val:
        return same(p.left, q.left) and same(p.right, q.right)
    return False
