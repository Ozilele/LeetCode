// Add Two Numbers Problem
// https://leetcode.com/problems/add-two-numbers/description/

package Linked_List;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(Integer.MIN_VALUE);
        ListNode newList = dummy;
        int next = 0;
        while(l1 != null && l2 != null) { // counting from jedności do setek
            int value = l1.val + l2.val + next;
            if(value > 9) {
                next = 1;
            } else {
                next = 0;
            }
            newList.next = new ListNode(value % 10, null);
            newList = newList.next;
            l1 = l1.next;
            l2 = l2.next;
            if(l1 == null && l2 == null && next == 1) {
                newList.next = new ListNode(next, null);
            }
        }

        if(l1 != null && l2 == null) {
            while(l1 != null) {
                int val = l1.val + next;
                if(val > 9) {
                    next = 1;
                } else {
                    next = 0;
                }
                newList.next = new ListNode(val % 10, null);
                newList = newList.next;
                l1 = l1.next;
                if(l1 == null && next == 1) {
                    newList.next = new ListNode(next, null);
                }
            }
        } else {
            while(l2 != null) {
                int val = l2.val + next;
                if(val > 9) {
                    next = 1;
                } else {
                    next = 0;
                }
                newList.next = new ListNode(val % 10, null);
                newList = newList.next;
                l2 = l2.next;
                if(l2 == null && next == 1) {
                    newList.next = new ListNode(next, null);
                }
            }
        }
        return dummy.next;
    }
}
