package test;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Search {
	char[][] grid;
	int row_num = 0;
	int column_num = 0;
	int path_length = Integer.MAX_VALUE;

	private int UP = 0;
	private int DOWN = 1;
	private int LEFT = 2;
	private int RIGHT = 3;

	public Search(String filename) throws IOException {
		// setup maze puzzle
		this.read_file(filename);
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

	public void print_path_length() {
		System.out.println(this.path_length);
	}

	private int[] remove_from_array(int[] l, int value) {
		int[] removed = new int[l.length - 1];
		// removes value from array
		for(int i = 0; i < l.length; i++)
			if(l[i] == value) {
				 System.arraycopy(l, 0, removed, 0, i);
				 System.arraycopy(l, i+1, removed, i, l.length - i - 1);
			}
		return removed;
	}

	private int[] search_for_start() {
		// search for start point
		int[] start_index = new int[2];
		for(int i = 0; i < this.row_num; i++)
			for(int j = 0; j < this.column_num; j++)
				if(this.grid[i][j] == 'b') {
					start_index[0] = i;
					start_index[1] = j;
				}
		return start_index;
	}

	private int[] valid_moves(char[][] grid, int x, int y, int[] moves) {
		// remove moves that will be out of bounds or hit a wall
		for(int i = 0; i < 4; i++) {
			int[] new_index = this.preform_move(x, y, i);
			if(
			    (new_index[0] < 0 || new_index[0] == this.row_num) ||
			    (new_index[1] < 0 || new_index[1] == this.column_num)
			) {
				moves = this.remove_from_array(moves, i);
				continue;
			}

			if(grid[new_index[0]][new_index[1]] == '0')
				moves = this.remove_from_array(moves, i);
		}
		return moves;
	}

	private int[] preform_move(int x, int y, int move) {
		switch(move) {
			case 0: x++;	//up
				break;
			case 1: x--;	//down
				break;
			case 2: y--;	//left
				break;
			case 3: y++;	//right
				break;
		}
		int[] new_index = {x, y};
		return new_index;
	}

	public boolean search_path() {
		boolean found_path = false;
		int[] start_index = this.search_for_start();

		// priority movements will determine path lengths
		int[][] movements = {
			{this.RIGHT, this.DOWN, this.LEFT, this.UP}, {this.LEFT, this.DOWN, this.RIGHT, this.UP},
			{this.RIGHT, this.UP, this.LEFT, this.DOWN}, {this.LEFT, this.UP, this.RIGHT, this.DOWN},
			{this.UP, this.RIGHT, this.DOWN, this.LEFT}, {this.DOWN, this.RIGHT, this.UP, this.LEFT},
			{this.UP, this.LEFT, this.DOWN, this.RIGHT}, {this.DOWN, this.LEFT, this.UP, this.RIGHT}
		};

		for(int m = 0; m < movements.length; m++) {
			// deep copy of grid for multiple executions
			char[][] recur_grid = new char[this.row_num][this.column_num];
			for(int i = 0; i < this.row_num; i++) {
				char[] temp_row = new char[this.column_num];
				for(int j = 0; j < this.column_num; j++)
					temp_row[j] = this.grid[i][j];
				recur_grid[i] = temp_row;
			}

			found_path = this.solve_maze(recur_grid, start_index[0], start_index[1], 0, movements[m]);
		}
		return found_path;
	}

	private boolean solve_maze(char[][] grid, int x, int y, int length, int[] moves) {
		// keep valid moves
		int[] valid_moves = this.valid_moves(grid, x, y, moves);

		for(int i = 0; i < valid_moves.length; i++) {
			// perform move
			int[] index = this.preform_move(x,  y,  valid_moves[i]);

			// when endpoint is found, then we are done
			if(grid[index[0]][index[1]] == 'x') {

				// maintain the shortest path
				if(this.path_length > length)
					this.path_length = length;
				return true;
			}

			// spot has been visited so we will close it
			grid[index[0]][index[1]] = '0';

			// main recursion path finding method
			if(this.solve_maze(grid, index[0], index[1], length + 1, moves))
				return true;

			// spot visited does not lead to endpoint so we open it
			grid[index[0]][index[1]] = '1';

		}
		return false;
	}

	public static void main(String[] args) {
		try {
			String filename = "path_to\\maze.txt";
			Search search = new Search(filename);
			if(search.search_path())
				search.print_path_length();
			else
				System.out.print("no solution");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
