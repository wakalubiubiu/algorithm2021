from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        j=len(height)-1
        length = j
        high = min(height[0], height[j])
        max_area = length * high
        for i in range(len(height)):
            while i<j and height[j]<height[i]:
                j -= 1
            length = j - i
            high = min(height[i], height[j])
            max_area = max(max_area, length * high)
        return max_area


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))