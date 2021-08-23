class TicTacToe:
    """
    A class to represent TicTacToe game.

    ...

    Attributes:
        grid : list
            contains the cells of the game and their current status.
            It is stored as 3 nested lists, one per row.
            Accepted symbols are 'X', 'O' and '_'.
        turn : str
            stores the next turn 'X' or 'O'
    """

    def __init__(self):
        """The constructor to initialize the object."""
        empty_row = ['_', '_', '_']
        self.grid = [list(empty_row), list(empty_row), list(empty_row)]
        self.turn = 'X'  # first player is 'X'

    def update(self, cells):
        """
        Updates the grid with the new status passed in argument 'cells'.

        Parameters:
            cells : str
                Status of all the cells of the game.
                Accepted symbols are 'X', 'O' and '_'.
        """
        self.grid = [list(cells[0:3]), list(cells[3:6]), list(cells[6:9])]

    def new_move(self, row, column):
        """
        Updates the grid with the new move passed in arguments 'row'-'column' and
        returns if move is valid or not. Each new move is assigned to the next player
        'X' or 'O'.

        Parameters:
            row : str
                Row coordinate. Accepted values '1' to '3'
            column : str
                Columns coordinate. Accepted values '1' to '3'

        Return:
            valid : bool
                True if valid move, False if invalid move
        """
        valid = False

        try:
            if self.grid[int(row) - 1][int(column) - 1] in ('X', 'O'):
                print("This cell is occupied! Choose another one!")
            else:
                self.grid[int(row) - 1][int(column) - 1] = self.turn
                self.turn = 'O' if self.turn == 'X' else 'X'  # update next player
                valid = True
        except (TypeError, ValueError):
            print("You should enter numbers!")
        except IndexError:
            print("Coordinates should be from 1 to 3!")

        return valid

    def result(self):
        """
        Analyzes the grid to print the game result.

        Return:
            finished : bool
                True if game is finished
        """
        finished = False
        x_wins = False
        o_wins = False
        empty_cells = False
        x_total = 0
        o_total = 0

        # Check rows
        for row in self.grid:
            if all(cell == 'X' for cell in row):
                x_wins = True
            if all(cell == 'O' for cell in row):
                o_wins = True
            if any(cell == '_' for cell in row):
                empty_cells = True
            x_total += row.count('X')
            o_total += row.count('O')

        # Check columns
        if all(cell == 'X' for cell in (self.grid[0][0], self.grid[1][0], self.grid[2][0])) or \
                all(cell == 'X' for cell in (self.grid[0][1], self.grid[1][1], self.grid[2][1])) or \
                all(cell == 'X' for cell in (self.grid[0][2], self.grid[1][2], self.grid[2][2])):
            x_wins = True
        if all(cell == 'O' for cell in (self.grid[0][0], self.grid[1][0], self.grid[2][0])) or \
                all(cell == 'O' for cell in (self.grid[0][1], self.grid[1][1], self.grid[2][1])) or \
                all(cell == 'O' for cell in (self.grid[0][2], self.grid[1][2], self.grid[2][2])):
            o_wins = True

        # Check diagonals
        if all(cell == 'X' for cell in (self.grid[0][0], self.grid[1][1], self.grid[2][2])) or \
                all(cell == 'X' for cell in (self.grid[0][2], self.grid[1][1], self.grid[2][0])):
            x_wins = True
        if all(cell == 'O' for cell in (self.grid[0][0], self.grid[1][1], self.grid[2][2])) or \
                all(cell == 'O' for cell in (self.grid[0][2], self.grid[1][1], self.grid[2][0])):
            o_wins = True

        # Analyze result
        if (x_wins and o_wins) or (x_total > o_total + 1) or (o_total > x_total + 1):
            print("Impossible")
        elif not empty_cells and not x_wins and not o_wins:
            print("Draw")
            finished = True
        elif x_wins:
            print("X wins")
            finished = True
        elif o_wins:
            print("O wins")
            finished = True

        return finished

    def __str__(self):
        """
        Return a representation of the current status of the game.
        """
        line_of_dashes = 9 * "-"
        row_1 = "| " + " ".join(self.grid[0]) + " |"
        row_2 = "| " + " ".join(self.grid[1]) + " |"
        row_3 = "| " + " ".join(self.grid[2]) + " |"
        return "\n".join([line_of_dashes, row_1, row_2, row_3, line_of_dashes])


game = TicTacToe()
print(game)

# Game loop
while True:
    valid_move = False
    move = input("Enter the coordinates: ").split()
    try:
        valid_move = game.new_move(*move)
    except TypeError:
        print("You should enter numbers!")
    if valid_move:
        print(game)
        if game.result():
            break
