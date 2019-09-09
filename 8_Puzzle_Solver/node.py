# Zoe Harris, Rachel Lewis
# CSCE405 Artificial Intelligence
# Programming Assignment #1


class Node:
    def __init__(self, val=None, pred=None, g=None, open_size=None, closed_size=None):
        self.val = val
        self.pred = pred
        self.open_size = open_size
        self.closed_size = closed_size
        self.g = g

    def set_pred(self, new_pred):
        self.pred = new_pred

    def set_open_size(self, new_size):
        self.open_size = new_size

    def set_closed_size(self, new_size):
        self.closed_size = new_size
