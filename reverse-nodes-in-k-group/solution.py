# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 2 or head is None:
            return head

        result = []
        result_temp = []
        now = head
        i = 0
        while now != None:
            result_temp += [now]
            if (i + 1) % k == 0:
                result_temp.reverse()
                result += result_temp
                result_temp = []
            now = now.next
            i += 1
        result += result_temp
        new_head = result[0]
        for i in range(len(result)):
            if i == len(result) - 1:
                result[i].next = None
            else:
                result[i].next = result[i + 1]
        return new_head
