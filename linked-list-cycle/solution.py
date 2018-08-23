# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is not None:
            fast = head.next
        else:
            return False
        slow = head
        while fast is not None and slow is not None:
            if fast == slow:
                return True
            if fast.next is not None:
                fast = fast.next.next
            else:
                return False
            slow = slow.next
        return False
