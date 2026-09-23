# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        temp=[]
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            
            temp.append(node.val)
            inorder(node.right)
        inorder(root)
        return temp==sorted(temp) and len(temp)==len(set(temp))

            
        