// Swap Nodes in Pairs Problem
// https://leetcode.com/problems/swap-nodes-in-pairs/description/
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
    public ListNode swapPairs(ListNode head) {
        if(head == null || head.next == null) {
            return head;
        }
        ListNode dummy = new ListNode(Integer.MIN_VALUE);
        dummy.next = head;
        ListNode curr = head;
        ListNode adjacent = head.next;

        while(curr != null) {
            if(adjacent == null) {
                break;
            }
            ListNode prev = dummy;
            while(prev.next != curr) {
                prev = prev.next;
            }
            // swaps of adjacent nodes
            ListNode tmp = adjacent.next;
            prev.next = adjacent;
            adjacent.next = curr;
            curr.next = tmp;
            // Actualization 
            curr = tmp;
            if(curr == null) {
                break;
            }
            adjacent = curr.next;
        }
        return dummy.next;
    }
}
