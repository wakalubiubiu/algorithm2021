from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        new_nums = sorted(nums)
        result = []
        for i, e in enumerate(new_nums):
            # 这个跳出循环的判断要写在前面，因为如果写在了判断重复的if语句后面，这个判断就失效了，因此这里我觉得写成
            # i >= len(new_nums) - 3,可能更合适。
            if i == len(new_nums) - 3:
                break
            if i > 0 and e == new_nums[i-1]:
                continue
            target_1 = target - e
            # 内层循环要从外层循环的下一个数开始，从同一数开始，则会出现重复。我的写法是截掉了数组包括位置i和i前面那部分
            # 这时就会有另一个问题，这样的循环j是从0开始的，这样，在下面的while循环中取位置和判断元素是否重复都会存在问题，因此
            # 在这个位置，我加了一个偏移量，计算当前的元素在new_nums中的真正位置，偏移量就是i+1，因为是从i+1的位置开始的循环。
            for j, e1 in enumerate(new_nums[i+1:]):
                # k就是加完偏移量之后的真实位置
                k = j + i + 1
                if k > i+1 and e1 == new_nums[k-1]:
                    continue
                target_2 = target_1 - e1
                # 此处用的依然是双指针法，左侧指针，指向的就是内层循环当前元素的下一个位置，右侧位置就是数组的末尾。
                m = k + 1
                n = len(new_nums) - 1
                while m < n:
                    # 注意如果元素重复，此处也要跳过。这个地方错了，也会让结果重复。
                    if m > k+1 and new_nums[m] == new_nums[m-1]:
                        m += 1
                        continue
                    if new_nums[m]+ new_nums[n] > target_2:
                        n -= 1
                    elif new_nums[m] + new_nums[n] < target_2:
                        m += 1
                    else:
                        result.append([e, e1, new_nums[m], new_nums[n]])
                        m += 1
        return result

