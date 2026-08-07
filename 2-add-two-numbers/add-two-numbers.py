# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy=ListNode(0)
        temp=dummy
        while l1 or l2:
            total=carry
            if l1:
                total+=l1.val
            if l2:
                total+=l2.val
            if total>9:
                carry=total//10
                curr=total%10
            else:
                curr=total
                carry=0
            new_node=ListNode(curr)
            temp.next=new_node
            temp=temp.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        if carry!=0:
            new_node=ListNode(carry)
            temp.next=new_node



        return dummy.next

        