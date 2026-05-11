# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = ListNode()
        ans = tmp
        ptr1, ptr2 = list1, list2
        while ptr1 is not None and ptr2 is not None:
            if ptr1.val<=ptr2.val:
                ans.next = ptr1
                ptr1 = ptr1.next
                ans = ans.next
            else:
                ans.next = ptr2
                ptr2 = ptr2.next
                ans = ans.next
        
        if ptr1 is not None:
            ans.next = ptr1
        
        else:
            ans.next = ptr2
        
        ans = tmp.next
        return ans