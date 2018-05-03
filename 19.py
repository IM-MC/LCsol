def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """

    sub = head
    dupe = head

    for _ in range(n):
        sub = sub.next

    if sub == None:
        return head.next

    while sub.next != None:
        head = head.next
        sub = sub.next

    head.next = head.next.next

    return dupe
