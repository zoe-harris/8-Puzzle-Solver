from node import Node

class PriorityQueue:
    def __init__(self):
        self.queue = []

    """Function checks if the queue is empty."""
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False

    """Function inserts an item to the queue IF f changes."""
    # This method inserts elements in order of associated priority (f)
    def enqueue(self, ele):
        # If empty, just add to the front of the queue
        if self.is_empty():
            self.queue.append(ele)
        # Else, loop through the queue and insert where needed
        else:
            for x in range(len(self.queue)):
                if ele.f < self.queue[x].f:
                    self.queue.insert(x, ele)
                    return
            self.queue.append(ele)

    """Function inserts an item to the queue if F does not change."""
    def enqueue_bfs(self, ele):
        self.queue.append(ele)

    """Function removes and returns the first item of the queue"""
    # This method removes and returns the first element in the queue,
    # which is also the element with the highest priority
    def dequeue(self):
        return self.queue.pop(0)
