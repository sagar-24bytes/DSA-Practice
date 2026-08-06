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
        dummy=Node(0)
        temp=dummy
        ori=head
        while ori:
            new_node=Node(ori.val)
            temp.next=new_node
            copy[ori]=new_node
            ori=ori.next
            temp=temp.next
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
        