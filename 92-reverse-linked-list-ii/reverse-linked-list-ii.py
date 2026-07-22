# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        dummy.next=head
        temp=dummy
        for i in range(left-1):
            temp=temp.next
        curr=temp.next
        temp2=curr
        prev=None
        for j in range(right-left+1):
            nxxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxxt
        temp.next=prev
        temp2.next=curr
        return dummy.next

        