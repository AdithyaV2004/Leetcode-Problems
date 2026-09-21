# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if root==None:
            return True
        def helper(node, low, high):
            l = node.val>low and node.val < high and helper(node.left, low, node.val) if node else True
            r = node.val<high and node.val>low and helper(node.right, node.val, high) if node else True
            return l and r
        return helper(root, float('-inf'), float('inf'))