from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        chosen = []

        def recursion(n):
            # 递归边界，递归到最后一个数后返回
            if n == len(nums):
                # 注意python中的写法， 此处需要针对chosen使用chosen[:]进行拷贝，否则每次chosen的改变，都会改变整个result中的所有结果
                result.append(chosen[:])
                return
            # 本层逻辑，针对该位置的数，对于该数是否加入集合分别进入两个分支
            recursion(n+1)
            chosen.append(nums[n])
            recursion(n+1)
            # 还原现场，因为chosen是一个共享变量，每一次添加元素后都应该进行还原
            chosen.pop()

        recursion(0)

        return result


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    print(solution.subsets(nums))
