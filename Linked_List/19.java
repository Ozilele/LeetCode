// Remove Nth Node From End of List Problem
// https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
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

    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(Integer.MIN_VALUE);
        ListNode curr = head;
        int listCount = 1;
        while(curr.next != null) {
            listCount += 1;
            curr = curr.next;
        }
        
        dummy.next = head;
        int count = 0;
        ListNode prev = dummy;
        while(head != null) {
            if(listCount - n == count) {
                prev.next = head.next;
                // remove the node
                break;
            }
            count += 1;
            prev = head;
            head = head.next;
        }
        return dummy.next;
    }

}
