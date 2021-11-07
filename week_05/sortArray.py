import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, arr, l, r):
        if l>=r:
            return
        pivot = self.partition(arr, l, r)
        self.quickSort(arr, l, pivot)
        self.quickSort(arr, pivot + 1, r)

    def partition(self, a, l, r):
        pivot = random.randint(l, r)
        pivotVal = a[pivot]
        while l <= r:
            while a[l]< pivotVal:
                l += 1
            while a[r]> pivotVal:
                r-= 1
            if l == r:
                break
            if l<r:
                a[l], a[r]=a[r], a[l]
                l += 1
                r -= 1
        return r


if __name__ == '__main__':
    solution = Solution()
    print(solution.sortArray([5, 3, 6, 8, 4, 6, 1]))
