def partition(head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """

    l1 = head1 = ListNode(0)
    r1 = head2 = ListNode(0)

    while head:
        if head.val < x:
            l1.next = head
            l1 = l1.next
        else:
            r1.next = head
            r1 = r1.next
        head = head.next

    r1.next = None
    l1.next = head2.next

    return head1.next
