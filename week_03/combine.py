from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        chosen = []

        def recursion(nums, i, k):
            # 如果k比nums先耗尽，那么就把满足的结果返回
            if k == 0:
                result.append(chosen[:])
                return
            # 此处判断的意思就是看当前还需要的数的数量k和nums中剩余的数的数量是否相等，如果相等，直接把nums剩余的数全部加入就满足条件
            elif k == len(nums) - i:
                try:
                    delete_index = len(chosen)
                    chosen.extend(nums[i:])
                    result.append(chosen[:])
                    del chosen[delete_index:]
                except Exception as e:
                    print(e.args[0])
                return
            recursion(nums, i + 1, k)
            chosen.append(nums[i])
            recursion(nums, i + 1, k - 1)
            chosen.pop()

        nums = [i for i in range(1, n + 1)]
        recursion(nums, 0, k)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(4, 2))
