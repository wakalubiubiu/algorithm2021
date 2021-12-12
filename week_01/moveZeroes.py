from typing import List


class Solution:
    """
    283. 移动零
    """
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        position = 0
        for i, e in enumerate(nums):
            # 如果一开始不是0的话，position和i一起移动，每次都会让本身进行一次交换。
            if nums[i] != 0:
                nums[position], nums[i] = nums[i], nums[position]
                position += 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.moveZeroes([0,1,0,3,12]))
