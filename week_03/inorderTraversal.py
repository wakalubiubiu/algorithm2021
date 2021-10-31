from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def recursion(node):
            if not node:
                return
            recursion(node.left)
            result.append(node.val)
            recursion(node.right)
        recursion(root)
        return result

    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     res, stack = [], []
    #     while True:
    #         while root:
    #             stack.append(root)
    #             root = root.left
    #         if not stack:
    #             return res
    #         node = stack.pop()
    #         res.append(node.val)
    #         root = node.right
