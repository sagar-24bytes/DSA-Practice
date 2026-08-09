# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res=[]
        def length():
            count=0
            temp=head
            while temp:
                count+=1
                temp=temp.next
            return count
        def reverse(node):
            temp=node
            prev=None
            while temp:
                nxxt=temp.next
                temp.next=prev
                prev=temp
                temp=nxxt
            res.append(prev)

        l=length()
        m=l//k
        temp=head
        
        for i in range(m):
            p=None
            h=temp
            count=0
            while temp and count<k:
                count+=1
                p=temp
                temp=temp.next
            p.next=None
            reverse(h)
        new_head=res[0]
        for j in range(len(res)):
            t=res[j]
            while t.next:
                t=t.next
            if j+1<len(res):
                t.next=res[j+1]
        t.next=temp
        return new_head
            


            

        