# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        now = head

        while now is not None and now.next is not None:
            if now.val == now.next.val:
                now.next = now.next.next
                continue
            now = now.next

        return head
