def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = None

        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp

        return prev
