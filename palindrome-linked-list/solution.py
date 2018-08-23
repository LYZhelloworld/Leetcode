# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

		# Inspired by: https://leetcode.com/problems/palindrome-linked-list/discuss/160547/Java-Solution-beat-99

        if not head or not head.next:
            return True

        fast = slow = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next

        last = slow.next
        pre, end = head, self.reverse(last)
        while end:
            if pre.val != end.val:
                return False
            pre, end = pre.next, end.next

        return True

    def reverse(self, node):
        if not node.next:
            return node
        prevNode, temp = self.reverse(node.next), node.next
        temp.next = node
        node.next = None
        return prevNode
