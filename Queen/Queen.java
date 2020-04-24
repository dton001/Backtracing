// Given NxN grid place N queens on the board
// without them being able to attack each other
// change variable when initializing Queen class


public class Queen {
	int[][] board;
	int amount = 0;

//	setup NxN empty board
	public Queen(int amount) {
		this.amount = amount;
		this.board = new int[amount][amount];

		for(int i = 0; i < amount; i++) {
			int[] row = new int[amount];
			for(int j = 0; j < amount; j++)
				row[j] = 0;
			this.board[i] = row;
		}
	}

//	print board
	public void print_board() {
		for(int i = 0; i < this.amount; i++) {
			for(int j = 0; j < this.amount; j++)
				System.out.print(this.board[i][j] + " ");
			System.out.println();
		}
	}

	public boolean check_safe(int x, int y) {
//		checks if row is safe for queen
		for(int i = 0; i < this.amount; i++)

//			queen is found in row
			if(this.board[i][y] == 1)
				return false;

//		list of all diagonal directions
		int[][] daigonal = {{1, 1}, {-1, 1}, {1, -1}, {-1, -1}};

//		checks if all diagonal directions are safe for queen
		for(int i = 0; i < 4; i++) {

//			continue looking at current diagonal direction until out of bounds
			for(int temp_x = x, temp_y = y; (temp_x >= 0 && temp_x < this.amount) && (temp_y >= 0 && temp_y < this.amount);
				temp_x += daigonal[i][0], temp_y += daigonal[i][1]) {

//				queen is found in current diagonal
				if(this.board[temp_x][temp_y] == 1)
					return false;
			}
		}

//		queen is safe from row and all diagonal directions
		return true;
	}

	public boolean unique_queen() {
//		calls main recursion function
		return this.queen_rec(0);
	}

	public boolean queen_rec(int column) {
//		when number of queen equal column number, we have placed all the queens
		if(this.amount == column)
			return true;

//		make array of possible spots in current column
		int[][] possible_spots = new int[this.amount][2];
		int spots_length = 0;
		for(int i = 0; i < this.amount; i++)

//			verify that a safe spot is added to possible spots
			if(this.check_safe(column, i)) {
				int[] spot = {column, i};
				possible_spots[spots_length] = spot;
				spots_length++;
			}

//		test each possible stop in column
		for(int i = 0; i < spots_length; i++) {

//			make current a queen
			this.board[possible_spots[i][0]][possible_spots[i][1]] = 1;

//			see if this placement works with future placements
			if(this.queen_rec(column + 1))
				return true;

//			future placements did not work so remove queen from spot
			this.board[possible_spots[i][0]][possible_spots[i][1]] = 0;
		}

		return false;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Queen q = new Queen(8);
		if(q.unique_queen())
			q.print_board();
		else
			System.out.println("Not possible");
	}

}
