from node import Node

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False

    def insert(self, ele):
        if self.isEmpty():
            self.queue.append(ele)
        else:
            for x in range(len.self.queue):
                if ele.f < self.queue[x].f:
                    self.queue.insert(x, ele)

    def insert_bfs(self, ele):
        self.queue.append(ele)

    def delete(self):
        self.queue.pop(0)



