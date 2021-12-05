import collections
import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        m = len(beginWord)
        visited_front = dict()
        visited_end = dict()
        visited_front[beginWord] = 1
        visited_end[endWord] = 1
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        queue_front = collections.deque()
        queue_front.append(beginWord)
        queue_end = collections.deque()
        queue_end.append(endWord)
        self.result = 0

        def bfs(queue, visited, visited_other):
            node = queue.popleft()
            for i in range(m):
                for char in string.ascii_lowercase:
                    if node[i] == char:
                        continue
                    new_node = node[0:i] + char + node[i+1:]
                    if new_node not in word_set:
                        continue
                    if new_node in visited:
                        continue
                    if new_node in visited_other:
                        # 注意此处的一个错误，当前的new_node在两边已经都存在了，那么证明两边都已经走到了，这时结果是visited[node] + visited_other[new_node]，不能使用visited[node] + visited_other[new_node] + 1，因为new_node只要一边走到了就可以了，再加1相当于又走了一次，这样就多了一次，结果是不对的。
                        self.result = visited[node] + visited_other[new_node]
                        return
                    visited[new_node] = visited[node] + 1
                    queue.append(new_node)

        # while 循环的判断跟视频课中不太一样，我用的是两个同时不为空，视频课中说的是有一个不为空即可，然后再bfs的方法内部判断队列是否为空，如果空就返回-1，我觉得这样写更简洁点？
        while queue_front and queue_end:
            bfs(queue_front,visited_front, visited_end)
            if self.result > 0:
                return self.result
            bfs(queue_end, visited_end, visited_front)
            if self.result > 0:
                return self.result
        return 0
