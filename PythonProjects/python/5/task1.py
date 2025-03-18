class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None

class Stack:
    def __init__(self):
        self.end = None

    def pop(self):
        if self.end is None:
            return None
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        node = Node(val)
        node.pref = self.end
        self.end = node

    def print(self):
        cur = self.end
        elems = []
        while cur:
            elems.append(str(cur.data))
            cur = cur.pref
        print(" ".join(elems))