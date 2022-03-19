class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
    
    def append(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.val)
            current_node = current_node.next

class LinkedStack(LinkedList):
    def pop(self):
        current_node = self.head
        if not current_node:
            raise ValueError('it is not set head')
        prev_node = current_node
        current_node = current_node.next
        while current_node.next:
            prev_node = current_node
            current_node = current_node.next
        val = current_node.val
        prev_node.next = None
        return val

class LinkedQueue(LinkedList):
    def deque(self):
        current_node = self.head
        if not current_node:
            raise ValueError('it is not set head')
        next_node = current_node.next
        val = current_node.val
        self.head = next_node
        return val

if __name__ == '__main__':
    stack = LinkedStack()
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.print()
    print('-------------')
    print(stack.pop())
    stack.append(4)
    print('-------------')
    stack.print()
    print('###################')
    que = LinkedQueue()
    que.append(14)
    que.append(15)
    que.append(16)
    que.print()
    print('-------------')
    print(que.deque())
    que.append(17)
    print('-------------')
    que.print()
