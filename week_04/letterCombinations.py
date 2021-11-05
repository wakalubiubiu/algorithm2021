from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        char = dict()
        char["2"] = "abc"
        char["3"] = "def"
        char["4"] = "ghi"
        char["5"] = "jkl"
        char["6"] = "mno"
        char["7"] = "pqrs"
        char["8"] = "tuv"
        char["9"] = "wxyz"
        ans = []

        if not digits:
            return []

        def recursion(index, string):
            if index == len(digits):
                ans.append(string)
                return
            for s in char[digits[index]]:

                # 注释的写法和直接传参的写法，本质上没有什么区别，但是注释的写法需要做一次递归需要的还原现场操作，全排列那道
                # 问题之所以选择了共享变量还原现场的做法，是因为其中需要的是一个数组，而不仅仅是一个字符串， 内存开销比较大。
                # string += s
                # recursion(index+1, string)
                # string = string[:-1]
                recursion(index+1, string+s)

        recursion(0, "")
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations("23"))

