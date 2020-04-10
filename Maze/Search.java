# Given a maze from a textfile
# Staring position is b, ending position is x, 0 are walls and 1 is a path tile
# Find the length from b to x

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Search {
	public class Node{
		int[] index = new int[2];
		Node parent = null;
		int g;
		int f;

		public Node(int[] index, Node parent) {
			this.index[0] = index[0];
			this.index[1] = index[1];
			this.parent = parent;
			this.g = 0;
			this.f = 0;
		}

		public boolean equals(Node n) {
			 return this.index[0] == n.index[0] && this.index[1] == n.index[1] ? true : false;
		}
	}

	char[][] grid;
	Node[] open_arr;
	Node[] closed_arr;
	Node[] path;
	int row_num = 0;
	int column_num = 0;
	int open_counter = 0;
	int closed_counter = 0;

	public Search2(String filename) throws IOException {
		// setup maze puzzle
		this.read_file(filename);

		this.open_arr = new Node[this.row_num * this.column_num];
		this.closed_arr = new Node[this.row_num * this.column_num];
	}

	public void read_file(String file_name) throws IOException {
		File f = new File(file_name);
		BufferedReader br = new BufferedReader(new FileReader(f));
		String row_input;

		// get number of row and columns and set up grid from those numbers
		int row_num = 0;
		for(; (row_input= br.readLine()) != null; row_num++) {
			if(row_num == 1) {
				String values[] = row_input.split(" ");
				this.column_num = values.length;
			}
		}
		this.row_num = row_num;
		this.grid = new char[this.row_num][this.column_num];
		br.close();

		br = new BufferedReader(new FileReader(f));
		for(row_num = 0; (row_input= br.readLine()) != null; row_num++) {
		    String values[] = row_input.split(" ");
		    char[] row = new char[this.column_num];

		    for(int i = 0; i < values.length; i++)
		    	row[i] = values[i].charAt(0);

		    this.grid[row_num] = row;
		}

		br.close();
	}

	public int[] find_point(String s) {
		// find start and end point
		char c = s.equals("begin") ? 'b' : 'x';
		int[] index = new int[2];

		for(int i = 0; i < this.row_num; i++)
			for(int j = 0; j < this.column_num; j++)
				if(this.grid[i][j] == c) {
					index[0] = i;
					index[1] = j;
				}

		return index;
	}

	private int find_shortest_distance() {
		// find index of the node with the smallest f cost
		int max = Integer.MAX_VALUE, index = -1;

		for(int i = 0; i < this.open_counter; i++) {
			if(max > this.open_arr[i].f) {
				max = this.open_arr[i].f;
				index = i;
			}
		}
		return index;
	}

	private Node[] remove_index(Node[] list, int index) {
		// remove node at index from the list
		Node[] new_list = new Node[list.length];
		int counter = 0;

		for(int i = 0; i < this.open_counter; i++) {
			if(index == i) {
				// index is hit, so increase counter and loop back to for loop
				counter++;
				continue;
			}
			// if we did not hit index then makes no difference
			// if we did hit index, then after skip, we need to go back one in new list
			new_list[i - counter] = list[i];
		}
		return new_list;
	}

	private int index(String arr_name, Node n) {
		// find index of node in array
		Node[] temp = arr_name.equals("open") ? this.open_arr : this.closed_arr;
		int counter = arr_name.equals("open") ? this.open_counter : this.closed_counter;

		for(int i = 0; i < counter; i++)
			if(temp[i].equals(n))
				return i;
		return -1;
	}

	private Node[] find_neighbor(Node curr) {
		// look viablity of each neighbor to current node
		Node[] neighbor = new Node[4];

		for(int i = 0, neighbor_counter = 0; i < 4; i++) {
			int x = curr.index[0], y = curr.index[1];
			switch(i) {
				case 0: x++;
					break;
				case 1: x--;
					break;
				case 2: y++;
					break;
				case 3: y--;
					break;
			}

			// make sure x and y are both still in bounds of grid
			if((x < 0 || x >= this.row_num) || (y < 0 || y >= this.column_num))
				continue;

			// see if index is a wall
			if(this.grid[x][y] == '0')
				continue;

			int[] index = {x, y};
			Node new_node = new Node(index, curr);

			// check that new node is not in closed array
			if(this.index("closed", new_node) != -1)
				continue;

			// index is within bounds and node is not in closed array, so add it to neighbor array
			neighbor[neighbor_counter] = new_node;
			neighbor_counter++;
		}
		return neighbor;
	}

	public int distance(Node n1, Node n2) {
		// calculate the distance between two nodes
		return Math.abs(n1.index[0] - n2.index[0]) + Math.abs(n1.index[1] - n2.index[1]);
	}

	public boolean search_path() {
		// find the start and end points
		Node start_node = new Node(this.find_point("begin"), null);
		Node end_node = new Node(this.find_point("end"), null);

		// append start_node to open_list to start the loop
		this.open_arr[this.open_counter] = start_node;
		this.open_counter++;

		while(this.open_counter != 0) {
			// find node with the lowest f cost
			int index = this.find_shortest_distance();
			Node curr = this.open_arr[index];

			// current node is removed from open array and appended to closed array
			this.open_arr = this.remove_index(this.open_arr, index);
			this.open_counter--;
			this.closed_arr[this.closed_counter] = curr;
			this.closed_counter++;
			Node[] neighbors;

			// we hit the end point
			if(curr.equals(end_node)) {
				// worst case for path length is number of nodes in closed path
				this.path = new Node[this.closed_counter];
				int i = 0;

				// construct the array of indexes hit
				for(Node iter = curr; iter != null; iter = iter.parent, i++)
					this.path[i] = iter;
				return true;
			}
			else {
				// not at endpoint so look at neighbors
				neighbors = this.find_neighbor(curr);
			}
			for(int i = 0; i < neighbors.length; i++) {
				// only look at elements in neighbors that have a value
				if(neighbors[i] != null) {

					// updating distance from neighbor to start
					neighbors[i].g++;

					// updating distance from neighbor to start + neighbor to distance
					neighbors[i].f = neighbors[i].g + this.distance(neighbors[i], end_node);

					// see if node is already in open array
					index = this.index("open", neighbors[i]);
					if(index != -1)
						// if node in open list but has higher f cost then ignore current neighbor
						if(neighbors[i].f > this.open_arr[index].f)
							continue;

					// neighbor either is not in open list or has a shorter f cost we add neighbor
					this.open_arr[this.open_counter] = neighbors[i];
					this.open_counter++;
				}
			}
		}
		return false;
	}

	public void print_path() {
		int size = 0;
		for(int i = this.path.length - 1; i != 0; i--)
			if(this.path[i] != null) {
				System.out.println(this.path[i].index[0] + " " + this.path[i].index[1]);
				size++;
			}
		System.out.println(size);
	}

	public static void main(String[] args) {
		try {
			String filename = "path_to\\maze.txt";
			Search search = new Search(filename);
			if(search.search_path())
				search.print_path();
			else
				System.out.print("no solution");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
