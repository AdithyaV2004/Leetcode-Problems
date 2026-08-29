# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrderReverse(self, node, level, stack):
        if node==None:
            return 
        if level==len(stack):
            stack.append(node.val)
        self.preOrderReverse(node.right, level+1, stack)
        self.preOrderReverse(node.left, level+1, stack)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        self.preOrderReverse(root, 0, res)
        return res