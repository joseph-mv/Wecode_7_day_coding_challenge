# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
       Find the node in the BST that the node's value equals val and 
       return the subtree rooted with that node. If such a node does 
       not exist, return null
       """
        current=root
        while current and current.val!=val:
            if current.val>val:
                current=current.left
            else:
                current=current.right
        return current