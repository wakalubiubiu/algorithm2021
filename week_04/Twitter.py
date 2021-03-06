from typing import List
from heapq import heappop, heappush


class ListNode:
    def __init__(self, val=0, key=0, next=None):
        self.id = val
        self.key = -key
        self.next = next


class Twitter:

    def __init__(self):
        self.count = 0
        self.users = [ListNode(-1) for _ in range(501)]
        self.follow_list = [dict() for _ in range(501)]


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        head = self.users[userId]
        temp = head.next
        new_node = ListNode(tweetId, self.count)
        head.next = new_node
        new_node.next = temp


    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        count = 0
        result = []
        if self.users[userId].next:
            heappush(h, (self.users[userId].next.key, self.users[userId].next))
        for key in self.follow_list[userId]:
            if self.users[key].next:
                heappush(h, (self.users[key].next.key, self.users[key].next))
        while count <10:
            try:
                node = heappop(h)[1]
                result.append(node.id)
                if node.next:
                    heappush(h, (node.next.key, node.next))
                count += 1
            except IndexError:
                break
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_list[followerId][followeeId] = 1

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_list[followerId]:
            del self.follow_list[followerId][followeeId]


if __name__ == '__main__':
    twitter = Twitter()
    twitter.postTweet(1, 5)
    twitter.postTweet(1, 3)
    twitter.follow(1, 2)
    twitter.follow(1, 3)
    twitter.postTweet(2, 101)
    twitter.postTweet(2, 13)
    twitter.postTweet(3, 19)
    print(twitter.getNewsFeed(1))