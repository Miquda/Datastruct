class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'data - {self.data}, next node - {self.next}'


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        remove = self.top
        self.top = self.top.next
        return remove.data

    def __repr__(self):
        return f'top - {self.top}'
