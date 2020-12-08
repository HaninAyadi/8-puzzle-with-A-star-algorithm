import heapq as hpq
import itertools


class PriorityQueueSet:
    """
    Combined priority queue and set data structure.

    The dictionary wrapper guarantees:
        - a unique set of items
        - the possibility to search for items

    and as a result:
        - the possibility to update the priority of an already existing item


    Provides O(1) membership test, O(log N) insertion and O(log N) removal of the smallest item.

    Important: the items of this data structure must be both comparable and
    hashable (i.e. must implement __cmp__ and __hash__). This is true of
    Python's built-in objects, but you should implement those methods if you
    want to use the data structure for custom objects.
    """

    # placeholder for a removed task
    REMOVED = '<removed-task>'

    def __init__(self, items=None):
        """
        Create a new PriorityQueueSet.

        Arguments:
        items (list): An initial item list - it can be unsorted and
        non-unique. The data structure will be created in O(N).

        Attributes:
            self.set: dictionary wrapper for the heap
            self.heap: the actual priority queue
            self.counter: unique sequence count
        """

        if items is None:
            items = []
        self.set = dict((item, []) for item in items)
        self.heap = list(self.set.keys())
        hpq.heapify(self.heap)
        self.counter = itertools.count()

    def has_item(self, item):
        """Check if ``item`` exists in the queue."""
        return item in self.set

    def get_priority(self, item):
        """Get the priority of ``item`` if it exists."""
        try:
            return self.set[item][0]
        except KeyError:
            print("Can't get priority of non-existing item")

    def pop(self):
        """Remove and return the lowest priority task. Raise KeyError if empty."""
        while self.heap:
            priority, count, smallest = hpq.heappop(self.heap)
            if smallest is not self.REMOVED:
                del self.set[smallest]
                return priority, smallest
        raise KeyError('pop from an empty priority queue')

    def remove(self, item):
        """Mark an existing task as REMOVED."""
        try:
            entry = self.set.pop(item)
            entry[-1] = self.REMOVED
        except KeyError:
            print("Can't remove a non-existing item")

    def add(self, item, priority=0):
        """Add a new item or update the priority of an existing task"""
        if item in self.set:
            self.remove(item)
        count = next(self.counter)
        entry = [priority, count, item]
        self.set[item] = entry
        hpq.heappush(self.heap, entry)
