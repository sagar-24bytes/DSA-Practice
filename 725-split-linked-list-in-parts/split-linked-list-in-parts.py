# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def size(node):
            if not node:
                return 0
            count=0
            temp=head
            while temp:
                count+=1
                temp=temp.next
            return count
        s=size(head)
        temp=head
        base=s//k
        extra=s%k
        ans=[]
        prev=None
        for i in range(k):
            curr_size=base+(1 if i<extra else 0)
            dummy=temp
            x=0
            while temp and x<curr_size:
                x+=1
                prev=temp
                temp=temp.next
            if prev:
                prev.next=None
            ans.append(dummy)
            
        return ans 


        