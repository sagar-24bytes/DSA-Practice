# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def func(node):
            if not node or node.val==p.val or node.val==q.val:
                return node
            left=func(node.left)
            right=func(node.right)
            if left and right:
                return node
            return left if left else right
        return func(root)
        