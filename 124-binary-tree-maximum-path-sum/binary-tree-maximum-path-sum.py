# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans=float('-inf')
        def dfs(node):
            if not node:
                return 0
            left=max(0,dfs(node.left))   # max path sum we can get from left subtree
            right=max(0,dfs(node.right))  # max pathsum we can get from right subtree
            self.ans=max(self.ans,node.val+left+right)  # doing left+node+right
            return node.val+max(left,right)  # can only give either left or right from node if we move upwards towards its parents
        dfs(root)
        return self.ans

        