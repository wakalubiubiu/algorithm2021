# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def recursion(l1, r1, l2, r2):
            if l1 > r1:
                return None
            root = TreeNode(postorder[r2])
            mid = l1
            while inorder[mid] != root.val:
                mid += 1
            # 这道题范围的确定很重要，中序的位置应该是从最左侧l1开始，到找到的mid的前一个为左子树的中序部分，
            # 这道题给的是后序遍历，因此后序遍历的左子树部分应该是从l2开始，包含的元素数应该是在中序遍历的集合中计算，中序遍历
            # 中包含的元素数是mid - 1 - l1 + 1 = mid -l1。跟前序遍历不同的是，根节点在后序遍历的最后，因此后序遍历的子集和应
            # 该是 l2 + mid - l1 -1，因为包含了l2这个元素。这个就是左子树的范围
            root.left = recursion(l1, mid - 1, l2, l2 + mid - l1-1)
            # 右子树的范围：中序是从mid+1开始，直到r1结束，而后序的范围是从左子树后序的结束+1开始，因此是l2 + mid - l1，结束
            # 也是直到结尾为止。
            root.right = recursion(mid + 1, r1, l2 + mid - l1, r2-1)
            return root
        root = recursion(0, len(inorder) - 1, 0, len(postorder) - 1)
        return root


if __name__ == '__main__':
    solution = Solution()
    print(solution.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]))
