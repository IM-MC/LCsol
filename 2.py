def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    carry = 0
    n = root = ListNode(0)

    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next

        car, value = divmod((v1+v2+carry), 10)
        carry = car
        n.next = ListNode(val)
        n = n.next

    return root.next