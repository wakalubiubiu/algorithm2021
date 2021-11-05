from typing import List


class Solution:
    """
    高阶二分查找方法1.1, 后继型
    """
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) //2
            # 如果查找lower_bound就用大于等于，如果查找upper_bound,就用大于
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return right


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([3, 5, 9, 13, 15, 19, 28], 13))
