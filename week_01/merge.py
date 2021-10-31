from typing import List


class Solution:
    """
    88. 合并两个有序数组
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # p1 = m - 1
        # p2 = n - 1
        # # set pointer for nums1
        # p = m + n - 1
        #
        # # while there are still elements to compare
        # while p1 >= 0 and p2 >= 0:
        #     if nums1[p1] < nums2[p2]:
        #         nums1[p] = nums2[p2]
        #         p2 -= 1
        #     else:
        #         nums1[p] = nums1[p1]
        #         p1 -= 1
        #     p -= 1
        #
        # # add missing elements from nums2
        # nums1[:p2 + 1] = nums2[:p2 + 1]


        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        # while there are still elements to compare
        while p1 >= 0 or p2 >= 0:
            if p1 < 0 or (p2>=0 and nums1[p1] < nums2[p2]):
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3))