class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)

        # new node is before head
        new_node.next = self.head

        # new node before head is now head
        self.head = new_node

    def remove(self, index):
        node = self.head

        if index > 0:
            # move node by index - 1
            for i in range(index - 1):
                node = node.next

            # skip next node since we are removing it
            node.next = node.next.next
        else:
            # removing first item so move head up by one
            self.head = self.head.next
            node.next = None

    def append(self, value, index=-1):
        new_node = Node(value)
        node = self.head

        # default adding node to end of list
        if index is -1:

            # go to end of list
            while node.next:
                node = node.next

            # add node to end of list
            node.next = new_node

        # adding node by index
        else:
            if index > 0:

                # go to node by index
                for i in range(index):
                    node = node.next

                # match next nodes
                new_node.next = node.next

                # curr node next is set to new node
                node.next = new_node

            # index = 0 so we adding node to beginning of list
            else:
                self.push(value)

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
