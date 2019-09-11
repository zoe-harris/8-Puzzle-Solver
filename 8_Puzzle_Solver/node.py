# Zoe Harris, Rachel Lewis
# CSCE405 Artificial Intelligence
# Programming Assignment #1


class Node:
    def __init__(self, val=None, pred=None, g=None, h=None, f=None):
        self.val = val
        self.pred = pred
        self.g = g
        self.h = h
        self.f = f
