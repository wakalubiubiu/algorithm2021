# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def recursion(l1, r1, l2, r2):
            if l1 > r1:
                return None
            root = TreeNode(preorder[l1])
            mid = l2
            while inorder[mid] != root.val:
                mid += 1

            root.left = recursion(l1 + 1, l1 + (mid - l2), l2, mid - 1)
            root.right = recursion(l1 + (mid - l2) + 1, r1, mid + 1, r2)
            return root

        root = recursion(0, len(preorder) - 1, 0, len(inorder) - 1)
        return root


