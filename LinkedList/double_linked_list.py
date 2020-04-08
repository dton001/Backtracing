class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
        if not self.tail:
            self.tail = new_node
        if self.head.next:
            self.head.next.prev = new_node

    def append(self, value):
        new_node = Node(value)
        last_node = self.tail

        new_node.next = last_node.next
        new_node.prev = last_node
        last_node.next = new_node
        self.tail = new_node

    def remove(self, index):
        if not self.head:
            return

        node = self.head
        if index is 0:
            self.head = node.next
            node.next.prev = None
            node.next = None
        else:
            for i in range(index - 1):
                node = node.next
            node.next = node.next.next
            if node.next:
                node.next.prev = node
            else:
                self.tail = node

    def insert_after(self, value, index):
        node = self.head
        new_node = Node(value)

        for i in range(index):
            node = node.next
        new_node.next = node.next
        node.next = new_node
        new_node.prev = node

        if new_node.next:
            new_node.next.prev = new_node
        else:
            self.tail = new_node

    def print_forward(self):
        first = self.head
        print("Forward")
        while first:
            print(first.value, end=' ')
            first = first.next

    def print_backward(self):
        last = self.tail
        print("\nBackward")
        while last:
            print(last.value, end=' ')
            last = last.prev


list = DoubleLinkedList()
list.push(5)
list.push(6)
list.push(7)
list.push(9)
list.insert_after(8, 3)
list.remove(3)
list.push(10)
list.append(11)
list.print_forward()
list.print_backward()
