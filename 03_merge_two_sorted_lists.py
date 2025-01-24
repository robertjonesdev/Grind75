from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list_head = None
        merged_list_curr = None
        while list1 or list2:
            node_to_append = None
            if list1 and list2:
                if list1.val < list2.val:
                    node_to_append = list1
                    list1 = list1.next
                else:
                    node_to_append = list2
                    list2 = list2.next
            elif list1:
                node_to_append = list1
                list1 = list1.next
            elif list2:
                node_to_append = list2
                list2 = list2.next

            if not merged_list_head:
                merged_list_head = node_to_append
                merged_list_curr = merged_list_head
            else:
                merged_list_curr.next = node_to_append
                merged_list_curr = merged_list_curr.next

        return merged_list_head