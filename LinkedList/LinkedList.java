public class LinkedList {
	public class Node{
		int data;
		Node next;

		public Node(int value) {
			this.data = value;
			this.next = null;
		}
	}

	Node head;

	public LinkedList() {
		this.head = null;
	}

	public void push(int value) {
		Node new_node = new Node(value);

		// new node is placed in front of head
		new_node.next = this.head;

		// node in front of head becomes head
		this.head = new_node;
	}

	public void remove(int index) {
		Node curr = this.head;

		if(index == 0) {
		    // remove first index, so move head up by one
			this.head = curr.next;
			curr.next = null;
		}
		else {
		    // iterate through list until we hit index -
			for(int i = 0; i < index - 1; i++, curr = curr.next);

			// set curr.next to skip next node
			curr.next = curr.next.next;
		}
	}

	public void append(int value) {
		Node new_node = new Node(value);
		Node curr = this.head;

        // go to end of list
		for(; curr.next != null; curr = curr.next);

		// add node to end of list
		curr.next = new_node;
	}

	public void insert(int value, int index) {
		Node new_node = new Node(value);
		Node curr = this.head;

        // iterate through list until we hit index
		for(int i = 0; i < index - 1; i++, curr = curr.next);

		//match new node and curr next
		new_node.next = curr.next;

		// curr next becomes new node
		curr.next = new_node;
	}

	public void print_list() {
		for(Node n = this.head; n != null; n = n.next)
			System.out.print(n.data + " ");
	}

	public static void main(String[] args) {
		LinkedList ll = new LinkedList();
		ll.push(1);
		ll.push(2);
		ll.push(3);
		ll.push(4);
		ll.push(5);
		ll.remove(4);
		ll.append(6);
		ll.insert(7, 2);
		ll.print_list();
	}
}
