from typing import List


class Solution:
    """
    高阶二分查找方法1.2, 前驱型
    """
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            # 此处使用了上取整，因为在剩余两个元素的时候，如果进入left分支，而不是上取整的话，那么left永远等于它自己，会陷入无限循环。因为需要上取整。
            mid = (left + right + 1) //2
            # 如果查找lower_bound就用小于等于，如果查找upper_bound,就用小于
            if nums[mid] <= target:
                left = mid
            else:
                right = mid -1
        return right


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([3, 5, 9, 13, 15, 19, 28], 16))
