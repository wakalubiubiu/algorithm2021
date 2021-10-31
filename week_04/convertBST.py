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

    def levelOrder(self, root: 'Node') -> List[List[int]]:

        result = []
        queue = []

        if root:
            queue.append((root, 0))

        while len(queue):
            node_tuple = queue[0]
            if len(result) == node_tuple[1]:
                result.insert(node_tuple[1], [])
            result[node_tuple[1]].append(node_tuple[0].val)
            del queue[0]
            if node_tuple[0].children:
                for child in node_tuple[0].children:
                    queue.append((child, node_tuple[1] + 1))
        return result


if __name__ == '__main__':
    TreeNode_0 = TreeNode(0)
    TreeNode_1 = TreeNode(1)
    TreeNode_2 = TreeNode(2)
    TreeNode_3 = TreeNode(3)
    TreeNode_4 = TreeNode(4)
    TreeNode_6 = TreeNode(6)
    TreeNode_5 = TreeNode(5)
    TreeNode_7 = TreeNode(7)
    TreeNode_8 = TreeNode(8)
    TreeNode_4.left = TreeNode_1
    TreeNode_4.right = TreeNode_6
    TreeNode_1.left = TreeNode_0
    TreeNode_1.right = TreeNode_2
    TreeNode_2.right = TreeNode_3
    TreeNode_6.left = TreeNode_5
    TreeNode_6.right = TreeNode_7
    TreeNode_7.right = TreeNode_8

    #
    # TreeNode_3 = TreeNode(3)
    # TreeNode_2 = TreeNode(2)
    # TreeNode_4 = TreeNode(4)
    # TreeNode_1 = TreeNode(1)
    # TreeNode_3.left = TreeNode_2
    # TreeNode_3.right = TreeNode_4
    # TreeNode_2.left = TreeNode_1
    solution = Solution()
    solution.convertBST(TreeNode_4)
    print(solution.inorderTraversal(TreeNode_4))

