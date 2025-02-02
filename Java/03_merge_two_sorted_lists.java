/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode merged_head = null;
        ListNode merged_curr = null;

        while (list1 != null || list2 != null) {
            ListNode appendNode = null;
            if (list1 != null && list2 != null) {
                if (list1.val < list2.val) {
                    appendNode = list1;
                    list1 = list1.next;
                } else {
                    appendNode = list2;
                    list2 = list2.next;
                }
            } else if (list1 != null) {
                appendNode = list1;
                list1 = list1.next;
            } else if (list2 != null) {
                appendNode = list2;
                list2 = list2.next;
            }
            if (merged_head == null) {
                merged_head = appendNode;
                merged_curr = merged_head;
            } else {
                merged_curr.next = appendNode;
                merged_curr = merged_curr.next;
            }
        }
        return merged_head;
    }
}