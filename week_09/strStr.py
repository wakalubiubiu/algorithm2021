class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        h = [0 for _ in range(n+1)]
        b = 131
        p = int(1e9 + 7)
        # p = 1e9 + 7
        bn = 1
        hash_needle = 0
        for i in range(1, n+1):
            h[i] = (h[i-1]*b + ord(haystack[i-1]) - ord('a') + 1) % p
        for i in range(m):
            hash_needle = (hash_needle * b + ord(needle[i]) - ord('a') + 1) % p
            bn = bn * b % p
        for l in range(1, n - m + 2):
            r = l + m - 1
            # print(h[r]- h[l-1] * bn% p, r, l-1)
            print(((h[r]- h[l-1] * bn % p)) % p, h[r], h[l-1], h[l-1] * bn, h[l-1] * bn % p, r, l-1)
            if ((h[r]- h[l-1] * bn % p )) % p == hash_needle:
                    # and haystack[l-1: m] == needle:
                return l-1
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.strStr("mississippi", "ssip"))
