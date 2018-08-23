# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        last = head
        while last.next:
            last = last.next
        self.reverse(head, None)
        return last

    def reverse(self, head, target):
        if head is not None:
            self.reverse(head.next, head)
            head.next = target
