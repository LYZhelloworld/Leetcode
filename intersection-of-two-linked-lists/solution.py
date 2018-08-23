# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        pA = headA
        pB = headB

        while pA is not None and pB is not None and pA != pB:
            pA = pA.next
            pB = pB.next

            if pA == pB:
                return pA
            if pA is None:
                pA = headB
            if pB is None:
                pB = headA

        return pA
