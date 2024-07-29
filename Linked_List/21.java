// Merge Two Sorted Lists Problem
// https://leetcode.com/problems/merge-two-sorted-lists/description/
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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy1 = new ListNode(Integer.MIN_VALUE);
        ListNode dummy2 = new ListNode(Integer.MIN_VALUE);
        // dummy1.next = list1;
        // dummy2.next = list2;

        ListNode mergedList = dummy1; // INT_MIN
        ListNode curr1 = list1;
        ListNode curr2 = list2;
        while(curr1 != null && curr2 != null) {
            if(curr2.val <= curr1.val) {
                // mergedList.next = curr2;
                mergedList.next = new ListNode(curr2.val, null);
                curr2 = curr2.next;
            }
            else { // curr1 < curr2
                mergedList.next = new ListNode(curr1.val, null);
                curr1 = curr1.next;
            }
            mergedList = mergedList.next;
        }

        while(curr1 != null) {
            mergedList.next = new ListNode(curr1.val, null);
            curr1 = curr1.next;
            mergedList = mergedList.next;
        }

        while(curr2 != null) {
            mergedList.next = new ListNode(curr2.val, null);
            curr2 = curr2.next;
            mergedList = mergedList.next;
        }
        return dummy1.next;
    }
}
