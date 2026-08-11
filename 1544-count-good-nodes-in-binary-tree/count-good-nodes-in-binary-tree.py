# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def func(root,max_val):
            if not root:
                return 0
            ans=0
            if root.val>=max_val:
                ans=1
            max_val=max(max_val,root.val)
            ans+=func(root.left,max_val)
            ans+=func(root.right,max_val)
            return ans
        return func(root,root.val)