from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []

        def recursion(node):
            if not node:
                return
            result.append(node.val)
            if node.children:
                for sub_node in node.children:
                    recursion(sub_node)

        recursion(root)
        return result


if __name__ == '__main__':
    root = Node(1)
    solution = Solution()
    print(solution.preorder(root))
