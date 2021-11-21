class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        word1 = ' ' + word1
        word2 = ' ' + word2

        result = [[10**9 for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            result[i][0] = i
        for i in range(n+1):
            result[0][i] = i
        for i in range(1, m+1):
            for j in range(1, n+1):
                # 对于某一个i长度的字符串，变为j长度，可以有三种操作第一种添加，第二种删除，第三种是替换或者不操作。
                # 第一种添加就要让j-1个字符和i个字符一样，然后添加一个字符。第二种就是要让i-1个字符和j个字符一样，这样就是从
                # i个删除最后一个字符，第三种就是替换，在result[i-1][j-1]的基础上，针对最后一个字符进行替换，如果一样，不用动，不一样就加1。
                result[i][j] = min(result[i][j-1] + 1, result[i-1][j] + 1, result[i-1][j-1] + (0 if word1[i] == word2[j] else 1))
        print(result)
        return result[m][n]
