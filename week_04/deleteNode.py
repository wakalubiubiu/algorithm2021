# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 如果找不到时，证明已经下探到底，这时无需更新。
        if not root:
            return None
        # 等于表示key已经找到了
        if root.val == key:
            # 如果找到的root没有左节点，那么可以直接把它的右节点更新为root本身，返回即可。
            if not root.left:
                return root.right
            # 右节点不存在同理，更新为左节点即可
            if not root.right:
                return root.left
            # 如果左右节点都存在，那么就要找到这个root的节点的后继节点，后继节点就是大于root的val值的第一个节点，所以需要在root的右子树中一直下探，直到左子树为空为止，这个点就是后继。
            next_node = root.right
            while next_node.left:
                next_node = next_node.left
            # 更新root的后继，将这个后继删除掉
            root.right = self.deleteNode(root.right, next_node.val)
            # root的val等于后继。
            root.val = next_node.val
        # 如果当前点的值大于key，需要向左下探，反之同理，向右下探
        elif root.val > key:
            # 下探的同时如果root的左节点是key 的话，root的left就会被更新，因此这里需要返回然后更新root的left，右节点同理。
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
