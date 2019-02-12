def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """

    if headA is None or headB is None:
        return None
    l1 = headA
    l2 = headB

    while l1 is not l2:
        l1 = headB if l1 is None else l1.next
        l2 = headA if l2 is None else l2.next

    return l1
