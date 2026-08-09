# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr=[]
        for i in range(len(lists)):
            temp=lists[i]
            while temp:
                arr.append(temp.val)
                temp=temp.next
        arr.sort()
        dummy=ListNode(0)
        temp=dummy
        for j in range(len(arr)):
            new_node=ListNode(arr[j])
            temp.next=new_node
            temp=temp.next
        return dummy.next

        