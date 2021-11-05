from typing import List


class Solution:
    """
    高阶二分查找方法三,查找小于等于target的最后一个元素。
    """
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left +1 < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid

        return left


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([3, 5, 9, 13, 15, 19, 28], 16))
