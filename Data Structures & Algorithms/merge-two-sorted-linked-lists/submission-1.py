# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        ptr1, ptr2 = list1, list2
        while ptr1 is not None and ptr2 is not None:
            if ptr1.val <= ptr2.val:
                tail.next = ptr1
                ptr1 = ptr1.next
            else:
                tail.next = ptr2
                ptr2 = ptr2.next
            tail = tail.next
        
        tail.next = ptr1 if ptr1 is not None else ptr2
        
        return dummy.next