def sortedListToBST(self, head):
    """
    :type head: ListNode
    :rtype: TreeNode
    """

    def buildTree(head,tail):
        fast = head
        slow = head
        if head == tail:
            return None

        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next

        temp = TreeNode(slow.val)
        temp.left = buildTree(head, slow)
        temp.right = buildTree(slow.next, tail)

        return temp

    return buildTree(head, None)
