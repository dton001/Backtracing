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

        # new node is placed in front of head
        new_node.next = self.head

        # new node in front of head becomes head
        self.head = new_node

        # when new list is made, new node also becomes tail
        if not self.tail:
            self.tail = new_node

        # if list has more than one node
        if self.head.next:

            # the second node's prev needs to be set properly
            self.head.next.prev = new_node

    def append(self, value):
        new_node = Node(value)
        last_node = self.tail

        # match next of new node and tail
        new_node.next = last_node.next

        # new node prev is set to tail
        new_node.prev = last_node

        # tail's next is set to new node
        last_node.next = new_node

        # new node is after tail, so it will become tail
        self.tail = new_node

    def remove(self, index):
        if not self.head:
            return

        # remove first item, set move head up by one
        if index is 0:
            self.head = self.head.next
        else:
            node = self.head

            # travel list until we hit the index - 1
            for i in range(index - 1):
                node = node.next

            # skip next node
            node.next = node.next.next

            # if we did not reach the end then node.next needs prev set up
            if node.next:
                node.next.prev = node

            # we are at end of list so last node becomes tail
            else:
                self.tail = node

    def insert_after(self, value, index):
        node = self.head
        new_node = Node(value)

        # travel list until we hit the index
        for i in range(index):
            node = node.next

        # match new node and curr node next
        new_node.next = node.next

        # curr node next becomes new node
        node.next = new_node

        # new node prev becomes current node
        new_node.prev = node

        # if not at end of list, then new node.next.prev needs to be set to new_node
        if new_node.next:
            new_node.next.prev = new_node

        # at end of list, so last node becomes tail
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
list.insert_after(8, 0)
list.remove(3)
list.push(10)
list.append(11)
list.print_forward()
list.print_backward()
