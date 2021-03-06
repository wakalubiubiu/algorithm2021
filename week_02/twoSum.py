from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.insert(0, -9999)
        i=0
        j=len(numbers)-1
        for m in range(len(numbers)):
            if i>=j:
                break
            if numbers[i] + numbers[j] > target:
                j -=1
            elif numbers[i] + numbers[j] < target:
                i+=1
            else:
                return [i, j]
        """
    result_map = dict()
    for i, num in enumerate(nums):
        if target - num in result_map:
            return [result_map[target - num], i]
        else:
            result_map[num] = i
    return [0, 0]

        """


if __name__=='__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
