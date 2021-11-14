class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        max_lis = 0
        count = 0
        lis = [1 for i in nums]
        lis_count = [1 for i in nums]
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if lis[i] == lis[j] + 1:
                        lis_count[i] += lis_count[j]
                    elif lis[i] < lis[j] + 1:
                        lis_count[i] = lis_count[j]
                        lis[i] = lis[j] + 1
        for i, e  in enumerate(lis):
            if e > max_lis:
                max_lis = e
                count = lis_count[i]
            elif e == max_lis:
                count += lis_count[i]
        # print(max_lis)
        print(lis_count)
        return count