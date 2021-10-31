# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def recursion(node: TreeNode, left_value, right_value):
            if not node:
                return True
            if node.val <= left_value or node.val >= right_value:
                return False
            return recursion(node.left, left_value, node.val) and recursion(node.right, node.val, right_value)

        return recursion(root, (-1 << 31)-1, (1 << 31))

if __name__ == '__main__':
    treeNode = TreeNode(2147483647)
    solution = Solution()
    solution.isValidBST(treeNode)