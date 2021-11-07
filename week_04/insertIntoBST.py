# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # if not root:
        #     return TreeNode(val)
        #
        # if val < root.val:
        #     root.left = self.insertIntoBST(root.left, val)
        # elif val > root.val:
        #     root.right = self.insertIntoBST(root.right, val)
        # return root

        def recursion(root):
            if val < root.val:
                if root.left:
                    recursion(root.left)
                else:
                    root.left = TreeNode(val)
            elif val > root.val:
                if root.right:
                    recursion(root.right)
                else:
                    root.right = TreeNode(val)
        if not root:
            root = TreeNode(val)
        recursion(root)
        return root
