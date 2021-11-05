class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.hash_map = dict()

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        node = self.hash_map[key]
        self.remove(node)
        self.insert(self.head, node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            # 如果存在，则需要更新值，然后把节点变为最新节点，方式就是先删除，后添加。
            node = self.hash_map[key]
            node.value = value
            self.remove(node)
        else:
            # 如果不存在，就需要新增一个节点，然后加入到hash_map中。
            node = Node(key, value)
            # 如果链表已经满了，就要把最老的节点删除，这里需要先删除hash_map中的key才行。
            if self.capacity == len(self.hash_map):
                del self.hash_map[self.tail.prev.key]
                self.remove(self.tail.prev)
            self.hash_map[key] = node
        self.insert(self.head, node)

    # 双向链表的插入删除的细节
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # 插入的话是先更新后一个节点，再更新前一个节点
    def insert(self, prev, node):
        prev.next.prev = node
        node.next = prev.next
        prev.next = node
        node.prev = prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == '__main__':
    obj = LRUCache(2)
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1))
