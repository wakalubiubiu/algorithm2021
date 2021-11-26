class Node:
    def __init__(self):
        self.count = 0
        self.children = [None] * 26

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        self.find(word, True, False, False)

    def search(self, word: str) -> bool:
        return self.find(word, False, True, False)

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix, False, False, True)

    def find(self, word, is_insert, is_search, is_prefix):
        current = self.root
        for i in word:
            if not current.children[ord(i) - 97]:
                if is_insert:
                    current.children[ord(i) - 97] = Node()
                else:
                    return False
            current = current.children[ord(i) - 97]
        if is_insert:
            current.count += 1
        if is_prefix:
            return True
        return current.count > 0

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)