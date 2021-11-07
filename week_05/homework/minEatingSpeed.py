import time
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def validate(speed):
            count_h = 0
            for pile in piles:
                if speed >= pile:
                    count_h +=1
                else:
                    count_h += (pile + speed -1)//speed
            return count_h <= h

        sum = 0
        for pile in piles:
            sum += pile
        left = (sum + h-1)//h
        right = sum
        while left < right:
            mid = (left + right) //2
            if validate(mid):
                right = mid
            else:
                left = mid + 1
        return right


if __name__ == '__main__':
    solution = Solution()
    print(solution.minEatingSpeed([312884470], 312884469))