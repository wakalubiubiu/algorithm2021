# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.result = []

        def recursion(root):
            if not root:
                self.result.append("null")
                return
            self.result.append(str(root.val))
            recursion(root.left)
            recursion(root.right)

        recursion(root)
        return ",".join(self.result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.current = 0
        self.result = data.split(",")

        def recursion():
            if self.current < len(self.result):
                if self.result[self.current] == "null":
                    self.current += 1
                    return None
            else:
                return None
            root = TreeNode(int(self.result[self.current]))
            self.current += 1
            root.left = recursion()
            root.right = recursion()
            return root

        return recursion()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))