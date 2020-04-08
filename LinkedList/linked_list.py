class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def remove(self, index):
        node = self.head

        if index > 0:
            for i in range(index - 1):
                node = node.next
            node.next = node.next.next
        else:
            self.head = self.head.next
            node.next = None

    def append(self, value, index=-1):
        new_node = Node(value)
        node = self.head

        if index is -1:
            while node.next:
                node = node.next
            node.next = new_node
        else:
            if index > 0:
                for i in range(index):
                    node = node.next
                new_node.next = node.next
                node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node

    def print_list(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next


list = LinkedList()
list.push(5)
list.push(6)
list.push(7)
list.push(8)
list.append(10, 0)
list.remove(0)
list.append(11)
list.print_list()
