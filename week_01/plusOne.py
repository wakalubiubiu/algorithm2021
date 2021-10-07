from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        for i in range(length-1, -1, -1):
            result = digits[i] + 1
            if result == 10:
                digits[i] = 0
            else:
                digits[i] = result
                break
        return digits
