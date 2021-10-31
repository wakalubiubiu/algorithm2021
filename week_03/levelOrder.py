
# Definition for a Node.
class Node:

from typing import List


class Solution:
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


