# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder:
            return None
        ind=0
        while inorder[ind]!=preorder[0]:
            ind+=1
        ls=preorder[1:ind+1]
        rs=preorder[ind+1:]
        lNode = self.buildTree(ls, inorder[:ind])
        rNode = self.buildTree(rs, inorder[ind+1:])
        return TreeNode(preorder[0], lNode, rNode)

        