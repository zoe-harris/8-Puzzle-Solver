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

    """Function deletes the first item of the queue."""
    def dequeue(self):
        self.queue.pop(0)
