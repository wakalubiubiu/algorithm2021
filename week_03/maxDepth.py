# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # def recursion(node: TreeNode, max_depth=0, current_depth=0):
        #     if node:
        #         current_depth += 1
        #     else:
        #         max_depth = max(max_depth, current_depth)
        #         return max_depth
        #     max_depth = recursion(node.left, max_depth, current_depth)
        #     max_depth = recursion(node.right, max_depth, current_depth)
        #     return max_depth
        #
        # return recursion(root, 0, 0)
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1