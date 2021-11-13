class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        def recursion(root, now_depth: int):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1

            if root.left:
                now_depth = min(recursion(root.left, now_depth), now_depth)
            if root.right:
                now_depth = min(recursion(root.right, now_depth), now_depth)
            return now_depth + 1
        return recursion(root, 10**5)


if __name__ == '__main__':
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)
    node_2.right = node_3
    node_3.right = node_4
    node_4.right = node_5
    node_5.right = node_6
    # node_3 = TreeNode(3)
    # node_9 = TreeNode(9)
    # node_20 = TreeNode(20)
    # node_15 = TreeNode(15)
    # node_7 = TreeNode(7)
    # node_3.left = node_9
    # node_3.right = node_20
    # node_20.left = node_15
    # node_20.right = node_7
    solution = Solution()
    print(solution.minDepth(node_3))