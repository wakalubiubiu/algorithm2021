from typing import List


class Solution:
    """
    leetcode 26. 删除有序数组中的重复项
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j+1


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
