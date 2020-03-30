package test;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Sudoku {
	char[][] grid;

	public Sudoku(String filename) throws IOException {
		// setup sudoku puzzle
		this.read_file(filename);
	}

	public void read_file(String file_name) throws IOException {
		File f = new File(file_name);
		BufferedReader br = new BufferedReader(new FileReader(f));
		String row_input;
		this.grid = new char[9][9];

		for(int row_num = 0; (row_input= br.readLine()) != null; row_num++) {
		    String values[] = row_input.split(" ");
		    char[] row = new char[9];

		    for(int i = 0; i < values.length; i++)
		    	row[i] = values[i].charAt(0);

		    this.grid[row_num] = row;
		}

		br.close();
	}

	public void print_puzzle() {
		for(int i = 0; i < 9; i++) {
			for(int j = 0; j < 9; j++) {
				System.out.print(this.grid[i][j]);
				System.out.print(' ');
			}
			System.out.println();
		}}

	public boolean search_for_empty(int[] index) {
		// changes index and returns true if there is another unassigned spot else return false
		for(int i = 0; i < 9; i++)
			for(int j = 0; j < 9; j++)
				if(this.grid[i][j] == '0') {
					index[0] = i;
					index[1] = j;
					return true;
				}
		return false;
	}

	public char[] remove_duplicates(char[] l, int x, String version){
		// depending on version, will remove numbers that already used in row or column
		for(int i = 0; i < 9; i++) {
			char num = version.equals("rows") ? this.grid[x][i] : this.grid[i][x];
			if(this.in_array(l, num))
				l = this.remove_from_array(l, num);
		}
		return l;
	}

	public char[] remove_duplicates_from_square(char[] l, int x, int y){
		// start and end for 3x3 box
		int[] x_range = this.box_range(x);
		int[] y_range = this.box_range(y);

		// will remove numbers that already used in 3x3
		for(int i = x_range[0]; i < x_range[1]; i++)
			for(int j = y_range[0]; j < y_range[1]; j++) {
				char num = this.grid[i][j];
				if(this.in_array(l, num))
					l = this.remove_from_array(l, num);
			}
		return l;
	}

	public int[] box_range(int num) {
		int[] range = new int[2];
        for(int i = 0; i < 4; i++)
            if(i * 3 <= num && num < (i + 1) * 3) {
            	range[0] = i * 3;
            	range[1] = (i + 1) * 3;
            }
        return range;
	}

	public boolean in_array(char[] l, char value) {
		// return true if array contains value else return false
		for(int i = 0; i < l.length; i++)
			if(l[i] == value)
				return true;
		return false;
	}

	public char[] remove_from_array(char[] l, char value) {
		char[] removed = new char[l.length - 1];
		// removes value from array
		for(int i = 0; i < l.length; i++)
			if(l[i] == value) {
				 System.arraycopy(l, 0, removed, 0, i);
				 System.arraycopy(l, i+1, removed, i, l.length - i - 1);
			}
		return removed;
	}

	public boolean solve_sudoku() {
		int[] index = {0, 0};

		// looks for empty spot and gives coordinates in index
		// if there are no more spots then we are finished
		if(!this.search_for_empty(index))
			return true;

		int x = index[0];
		int y = index[1];

		char[] possible_values = new char[9];
		for(int i = 1; i < 10; i++)
			possible_values[i - 1] = (char) (i + '0');

		// remove values are used in specific row, column, and 3x3 box
		possible_values = this.remove_duplicates(possible_values, x, "rows");
		possible_values = this.remove_duplicates(possible_values, y, "columns");
		possible_values = this.remove_duplicates_from_square(possible_values, x, y);

		for(int i = 0; i < possible_values.length; i++) {
			// assign spot with a valid input
			this.grid[x][y] = possible_values[i];

			//continues until all spots have valid assignments
			if(this.solve_sudoku())
				return true;

			// assigned input is not valid so we reset
			this.grid[x][y] = '0';
		}
		return false;
	}

	public static void main(String[] args) {
		try {
			String filename = "path_to\\puzzle.txt";
			Sudoku sudoku = new Sudoku(filename);
			if(sudoku.solve_sudoku())
				sudoku.print_puzzle();
			else
				System.out.print("no solution");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
