from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_dict = dict()
        ans = []
        for word in strs:
            new_word = sorted(word)
            new_word = "".join(new_word)
            if new_word not in hash_dict:
                hash_dict[new_word] = []
            hash_dict[new_word].append(word)
        for key, value in hash_dict:
            ans.append(value)
        return ans
