# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Finding middle element
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        curr=slow.next
        slow.next=None
        # reversing second half
        prev=None
        while curr:
            nxxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxxt
        
        # putting both halfs alternatively
        left=head
        right=prev
        while right:
            l=left.next
            r=right.next
            left.next=right
            right.next=l
            left=l
            right=r
    
        


        