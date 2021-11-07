class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:

        def get_next(root, val):
            ans = None
            current = root
            while current:
                if current.val == val:
                    if current.right:
                        # 这是视频课中的一个技巧，就是把ans直接更新为当前节点的右节点，然后使用while循环，不断向左寻找，同时
                        # 更新答案，指导答案的左节点不存在为止
                        ans = current.right
                        while ans.left:
                            ans = ans.left
                    break
                elif current.val > val:
                    if not ans or ans.val > current.val:
                        ans = current
                    current = current.left
                else:
                    current = current.right
            return ans

        result = get_next(root, p.val)
        return result


if __name__ == '__main__':
    tree_node_2 = TreeNode(2)
    tree_node_1 = TreeNode(1)
    tree_node_3 = TreeNode(3)
    tree_node_2.left = tree_node_1
    tree_node_2.right = tree_node_3
    solution = Solution()
    print(solution.inorderSuccessor(tree_node_2, tree_node_1).val)