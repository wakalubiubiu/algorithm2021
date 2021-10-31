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

