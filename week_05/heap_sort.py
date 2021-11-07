import heapq
from typing import List


class Solution:
    def heap_sort(self, nums: List[int])-> List[int] :
        h = []
        sorted_list = []
        for num in nums:
            heapq.heappush(h, num)
        for i in range(len(nums)):
            sorted_list.append(heapq.heappop(h))

        return sorted_list


if __name__ == '__main__':
    solution = Solution()
    print(solution.heap_sort([5,3,6,8,4,6,1]))