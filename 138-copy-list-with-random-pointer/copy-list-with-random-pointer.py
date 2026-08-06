"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy={}
        temp=head
        i=0
        temp2=head
        dummy=Node(0)
        temp=dummy
        while temp2:
            new_node=Node(temp2.val)
            temp.next=new_node
            temp=temp.next
            copy[temp2]=new_node
            i+=1
            temp2=temp2.next
        
        t=head
        new_t=dummy.next

        while t:
            if t.random==None:
                new_t.random=None
            elif t.random in copy:
                new_t.random=copy[t.random]
            
            new_t=new_t.next
            t=t.next
        return dummy.next


        