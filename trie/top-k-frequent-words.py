class Words(object):

    def __init__(self, val):
        self.key = val[0]
        self.val = val[1]

    def __gt__(self, other):
        if self.val > other.val:
            return False
        elif self.val < other.val:
            return True
        else:
            return self.key > other.key

    def __eq__(self, other):
        if self.val == other.val and self.key == other.key:
            return True
        else:
            return False

    def get_item(self):
        return self.key


class Solution(object):

    def __init__(self):
        self.word_to_count = dict()
        self.root = dict()

    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        if not words or len(words) < k:
            return None

        self.build_trie(words)
        return self.__dict_to_cmp__(self.word_to_count.items(), k)

    def build_trie(self, words):
        _end = "_end_"
        for word in words:
            current_word = self.root
            for w in word:
                current_word = current_word.setdefault(w, {})
            current_word['_end'] = _end
            self.word_to_count[word] = self.word_to_count.setdefault(word, 0) + 1

    def __dict_to_cmp__(self, dic, k):
        a = []
        print(a)
        for d in dic:
            a.append(Words(d))
        a.sort()
        return [x.get_item() for x in a[0: k]]


# Sol-2 by Xidong
class Solution(object):

    def topKFrequent(self, words: 'List[str]', k: 'int') -> 'List[str]':
        dic = dict()
        for word in words:
            dic[word] = dic.get(word, 0) + 1

        dic = sorted(dic.items(), key=lambda x:(-x[1], x[0]))
        return [x[0] for x in dic[0:k]]








