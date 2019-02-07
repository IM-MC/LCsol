import heapq

def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    dummy = temp = ListNode(0)

    H = [(node.val, node) for node in lists if node]
    heapify(H)

    while H:
        v, n = H[0]
        if not n.next:
            heappop(H)
        else:
            heapreplace(H,(n.next.val, n.next))
        temp.next = n
        temp = temp.next

    return dummy.next
