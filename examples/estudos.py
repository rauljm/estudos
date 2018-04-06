from collections import defaultdict
import heapq


class PriorityQueue(object):

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def less_priority(self):
        return heapq.nsmallest(1, self._queue)

    def majority_priority(self):
        return heapq.nlargest(1, self._queue)


class People(object):
    def __init__(self, name):
        self._name = name


def save_priority_in_dicio(key, value, dicio=None):
    if not dicio:
        dicio = defaultdict(list)

    dicio[key].append(value)
    return dicio


def main():
    queue = PriorityQueue()
    p1 = People('Raul')
    p2 = People('Isabelli')

    queue.push(p1, 2)
    queue.push(p2, 1)

    dicio = save_priority_in_dicio('p1', 2)
    dicio = save_priority_in_dicio('p2', 1, dicio)
    dicio = save_priority_in_dicio('p2', 3, dicio)
    print (dicio)

    print (queue.less_priority()[0][2]._name)
    print (queue.majority_priority()[0][2]._name)
    print (queue.pop()._name)
    print (queue.pop()._name)
