from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        length = 0
        word_map = {}
        ans = []
        k = len(words[0])

        def valid(sub_string, limit):
            flag = True
            for j in range(limit, len(sub_string), k):
                sub_word = sub_string[j: j + k]
                if sub_word in sub_map:
                    sub_map[sub_word] +=1
                else:
                    sub_map[sub_word] = 1
            for key, value in word_map.items():
                if key not in sub_map or sub_map[key] != value:
                    flag = False
                    break
            return flag
        for word in words:
            if word in word_map:
                word_map[word] += 1
            else:
                word_map[word] = 1
            length += len(word)
        limit = len(s)-length +1

        # 此处把for循环按照单词的长度k进行分组循环，每组内按照步长k循环，这样就可以覆盖所有的循环。
        for j in range(k):
            # 每次重新运行一个分组的时候新建一个map，因为之前的分组和当前的分组没有关系。
            sub_map = dict()
            # 此处for循环的最后界限是limit，limit =len(s)-length +1，这么是因为到了limit这个位置后的所有位置，
            # 都已经不够words的整体长度了，再往后遍历是没有意义的，所以可以去除。
            for i in range(j, limit, k):
                sub_string = s[i: i+length]
                # 这个函数的第二个变量是为了去除重复的单词，因为每次循环的时候都是移动k步，而子串的长度是words数组的整体长度，
                # 中间会有length-k的重复部分，这部分是不需要往map中添加的。另外，第一次循环的时候需要从0开始，因为这时map中还没有元素。
                if valid(sub_string, 0 if i<k else length-k):
                    ans.append(i)
                # 此处就是删除本次循环之后应该删除的当前一个单词。
                sub_map[s[i: i+k]] -= 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
