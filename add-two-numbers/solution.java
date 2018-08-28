/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode n = new ListNode(l1.val + l2.val);
        ListNode head = n, n1 = l1.next, n2 = l2.next, new_n;

        for(; n1 != null || n2 != null;) {
            new_n = new ListNode((n1 != null ? n1.val : 0) + (n2 != null ? n2.val : 0));
            n.next = new_n;
            n = new_n;

            if(n1 != null) {
                n1 = n1.next;
            }
            if(n2 != null) {
                n2 = n2.next;
            }
        }

        // Processing carry bits
        n = head;
        for(; n != null; n = n.next) {
            if(n.val >= 10) {
                n.val -= 10;
                if(n.next != null) {
                    n.next.val++;
                } else {
                    n.next = new ListNode(1);
                    break;
                }
            }
        }
        return head;
    }
}
