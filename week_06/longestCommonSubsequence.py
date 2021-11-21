class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = ' ' + text1
        text2 = ' ' + text2
        m = len(text1)
        n = len(text2)
        max_len = 0
        len_list = [[0 for j in range(0, n+1) ] for i in range(0,m+1)]
        for i in range(1, m):
            for j in range(1, n):
                if text1[i] == text2[j]:
                    len_list[i][j] = len_list[i-1][j-1] + 1
                else:
                    len_list[i][j] = max(len_list[i-1][j], len_list[i][j-1])
        return len_list[i][j]