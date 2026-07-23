# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        max_val=float('-inf')
        def reverse(node):
            prev=None
            while node:
                nxxt=node.next
                node.next=prev
                prev=node
                node=nxxt
            return prev
        temp=new_head=reverse(head)
        dummy=ListNode(0)
        dummy.next=new_head
        prev=dummy
        while temp:
            max_val=max(max_val,temp.val)
            if temp.val<max_val:
                prev.next=temp.next
            else:
                prev=temp
            temp=temp.next
        ans=reverse(dummy.next)
        return ans

            

                
            
            
        