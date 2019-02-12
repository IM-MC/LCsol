def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """

    if not head or not head.next:
        return False

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow.val == fast.val:
            return True

    return False
