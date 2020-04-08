public class DoubleLinkedList {
	public class Node{
		int data;
		Node next;
		Node prev;

		public Node(int value) {
			this.data = value;
			this.next = null;
			this.prev = null;
		}
	}

	Node head;
	Node tail;

	public DoubleLinkedList() {
		this.head = null;
		this.tail = null;
	}

	public void push(int value) {
		Node new_node = new Node(value);

		// new node placed in front of head
		new_node.next = this.head;

		// new node in front of head becomes head
		this.head = new_node;

        // list has more than one node, second node of list needs prev set up
		if(this.head.next != null)
			this.head.next.prev = new_node;

		// when new list is made, first node also becomes tail
		if(this.tail == null)
			this.tail = new_node;
	}

	public void remove(int index) {
		Node curr = this.head;

		// iterate through list until we hit index
		for(int i = 1; i < index; i++, curr = curr.next);

		// setup curr.next to skip next node
		curr.next = curr.next.next;

        // if not at end of list, curr.next needs prev setup
		if(curr.next != null)
			curr.next.prev = curr;

		// end of list, so last node becomes tail
		else
			this.tail = curr;
	}

	public void append(int value) {
		Node new_node = new Node(value);
		Node curr = this.tail;

        // match new node and tail next
		new_node.next = curr.next;

		// tail next becomes new node
		curr.next = new_node;

		// new node prev becomes tail
		new_node.prev = curr;

		// new node after tail becomes tail
		this.tail = new_node;
	}

	public void insert(int value, int index) {
		Node new_node = new Node(value);
		Node curr = this.head;

        // iterate through list until we hit index
        for(int i = 1; i < index; i++, curr = curr.next);

        // match new node and curr next
        new_node.next = curr.next;

        // curr next is set to new node
        curr.next = new_node;

        //new node prev is set to curr
        new_node.prev = curr;

        // if not at end of list, then new node.next.prev needs to be set to new_node
        if(new_node.next != null) {
            new_node.next.prev = new_node;

        // end of list, so last node needs to becomes tail
        else
            this.tail = new_node;
    }

	public void print_forward() {
		System.out.println("Forward");
		for(Node n = this.head; n != null; n = n.next)
			System.out.print(n.data + " ");
	}

	public void print_backward() {
		System.out.println("\nBackward");
		for(Node n = this.tail; n != null; n = n.prev)
			System.out.print(n.data + " ");
	}

	public static void main(String[] args) {
		DoubleLinkedList ll = new DoubleLinkedList();
		ll.push(1);
		ll.push(2);
		ll.push(3);
		ll.push(4);
		ll.push(5);
		ll.remove(3);
		ll.append(6);
		ll.append(8);
		ll.append(9);
		ll.insert(7, 7);
		ll.print_forward();
		ll.print_backward();
	}
}
