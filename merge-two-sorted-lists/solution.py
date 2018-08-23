# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val <= l2.val:
            n1 = l1
            n2 = l2
        else:
            n1 = l2
            n2 = l1

        head = n1

        while n1.next is not None and n2 is not None:
            if n1.next.val <= n2.val:
                n1 = n1.next
                continue

            tmp_n1_next = n1.next
            n1.next = n2
            tmp_n2_next = n2.next
            n2.next = tmp_n1_next

            n2 = tmp_n2_next
            n1 = n1.next

        if n1.next is None:
            n1.next = n2

        return head
