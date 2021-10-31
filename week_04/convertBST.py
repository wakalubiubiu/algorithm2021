# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sum = 0

        def convert(root):
            nonlocal sum
            if not root:
                sum += 0
                return
            convert(root.right)
            sum += root.val
            root.val = sum
            convert(root.left)
        convert(root)
        return root
