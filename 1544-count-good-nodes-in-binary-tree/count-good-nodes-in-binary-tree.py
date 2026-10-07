# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def func(node,maxval):
            if not node:
                return 0
            count=0
            if node.val>=maxval:
                count=1
                maxval=node.val
            count+=func(node.left,maxval)
            count+=func(node.right,maxval)
            return count
        return func(root,root.val)
        