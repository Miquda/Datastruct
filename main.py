from classes import Node, Stack

n1 = Node(5)
n2 = Node('a')
stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')
print(stack.top.data)
print(stack.top.next.data)
print(stack.top.next.data)
print(stack.top.next.next.next)
print(stack.top.next.next.next.data)
