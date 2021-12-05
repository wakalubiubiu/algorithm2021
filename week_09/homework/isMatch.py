class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        f = [[False] * (n+1) for _ in range(m+1)]
        f[0][0]=True

        def match(i, j):
            if i == 0:
                return False
            if p[j-1] == '?':
                return True
            return s[i-1] == p[j-1]

        for i in range(m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    f[i][j] = f[i-1][j] or f[i][j-1]
                else:
                    if match(i, j):
                        f[i][j] = f[i-1][j-1]
        return f[m][n]