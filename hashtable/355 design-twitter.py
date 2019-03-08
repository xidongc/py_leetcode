# heapq.merge(*iterables)¶
# Merge multiple sorted inputs into a single sorted output (for example,
# merge timestamped entries from multiple log files). Returns an iterator over the sorted values.
#
# Similar to sorted(itertools.chain(*iterables)) but returns an iterable, does not pull the data into memory all at once,
#  and assumes that each of the input streams is already sorted (smallest to largest).

# The *args will give you all function parameters as a tuple:
# [1]: def foo(*args):
#    ...:     for a in args:
#    ...:         print a
# foo(1,2,3) 1 2 3

# collections.deque appendleft popleft

# >>> sequence = count(start=0, step=1)
# >>> next(sequence)
# 0
# >>> next(sequence)
# 1
# >>> next(sequence)
# 2

# itertools.islice(iterable, stop)
# itertools.islice(iterable, start, stop)

# set.add(dup) would not throw an error
# set.discard(nonexists) would not throw an error
# set.remove(nonexists) would throw an error

# a.update('python') set(['b', 'h', 'o', 'n', 'p', 't', 'y'])
import collections
import itertools
import heapq
class Twitter(object):

    def __init__(self):
        # self.timer = itertools.count()
        self.timer = itertools.count(step=-1)
        self.tweets = collections.defaultdict(collections.deque)
        self.followers = collections.defaultdict(set)

        """
        Initialize your data structure here.
        """

    def postTweet(self, userId, tweetId):
        self.tweets[userId].appendleft((next(self.timer), tweetId))
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """

    def getNewsFeed(self, userId):
        """
                Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
                :type userId: int
                :rtype: List[int]
        """
        # tweets = reverse(sorted(itertools.chain(*(self.tweets[u] for u in self.followers[userId] | {userId}))))
        #  self.followers[userId] | {userId} means in followee or userId
        tweets = heapq.merge(*(self.tweets[u] for u in self.followers[userId] | {userId}))
        # print([_ for _,tweetId in tweets])
        return [tweetId for _,tweetId in itertools.islice(tweets, 10) ]


    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followers[followerId].remove(followeeId)
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """

# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1,5)
obj.postTweet(2,6)
obj.postTweet(1,3)
obj.follow(1,2)

param_2 = obj.getNewsFeed(1)
# obj.unfollow(followerId,followeeId)