# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n = ListNode(l1.val + l2.val)
        head = n
        n1 = l1.next
        n2 = l2.next
        while n1 is not None or n2 is not None:
            if n1 is None:
                new_n = ListNode(n2.val)
            elif n2 is None:
                new_n = ListNode(n1.val)
            else:
                new_n = ListNode(n1.val + n2.val)
            n.next = new_n
            n = new_n
            if n1 is not None:
                n1 = n1.next
            if n2 is not None:
                n2 = n2.next
        # Processing carry bits
        n = head
        while n is not None:
            if n.val >= 10:
                n.val -= 10
                if n.next is not None:
                    n.next.val += 1
                else:
                    n.next = ListNode(1)
                    break
            n = n.next
        return head
