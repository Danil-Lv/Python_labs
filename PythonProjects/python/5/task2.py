class Node:
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # ссылка на предыдущий узел

class Queue:
    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None    # ссылка на конец очереди

    def pop(self):
        if self.start is None:
            return None
        val = self.start.data
        self.start = self.start.nref
        if self.start:
            self.start.pref = None
        else:
            self.end = None
        return val

    def push(self, val):
        new_node = Node(val)
        if self.start is None:
            self.start = self.end = new_node
        else:
            self.end.nref = new_node
            new_node.pref = self.end
            self.end = new_node

    def insert(self, n, val):
        if n <= 0 or self.start is None:
            new_node = Node(val)
            new_node.nref = self.start
            if self.start:
                self.start.pref = new_node
            self.start = new_node
            if self.end is None:
                self.end = new_node
            return
        cur = self.start
        i = 0
        while cur and i < n:
            cur = cur.nref
            i += 1
        if cur is None:
            self.push(val)
        else:
            new_node = Node(val)
            prev = cur.pref
            new_node.nref = cur
            new_node.pref = prev
            cur.pref = new_node
            if prev:
                prev.nref = new_node
            else:
                self.start = new_node

    def print(self):
        cur = self.start
        elems = []
        while cur:
            elems.append(str(cur.data))
            cur = cur.nref
        print(" ".join(elems))