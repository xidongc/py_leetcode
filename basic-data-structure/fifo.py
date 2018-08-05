import queue


class DataStructure(object):

    # should define some abstract method
    pass


class Queue(object):

    def __init__(self):
        self.q = queue.PriorityQueue

    def push(self, item):
        self.q.put(item)

    def push(self, item):
        self.q.get()
        self.q.task_done()



