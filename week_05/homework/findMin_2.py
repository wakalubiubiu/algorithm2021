from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        nums_copy = nums[:]

        for i, e in enumerate(nums_copy):
            if nums_copy[len(nums) - 1] == nums[i]:
                nums_copy[i] += 1
            else:
                break
        while left < right:
            mid = (left + right)//2
            if nums_copy[mid] <= nums_copy[len(nums)-1]:
                right = mid
            else:
                left = mid + 1
        return nums[right]
