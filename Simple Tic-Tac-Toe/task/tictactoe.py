class TicTacToe:
    """
    A class to represent TicTacToe game.

    ...

    Attributes
    ----------
        grid : list
            contains the cells of the game and their current status.
            It is stored as 3 nested lists, one per row
            Accepted symbols are 'X', 'O' and '_'
    """

    def __init__(self):
        """The constructor to initialize the object."""
        self.grid = []

    def update(self, cells):
        """
        Updates the grid with the new status passed in argument 'cells'.

        Parameters
        ----------
        cells : str
            Status of all the cells of the game.
            Accepted symbols are 'X', 'O' and '_'
        """
        self.grid = [list(cells[0:3]), list(cells[3:6]), list(cells[6:9])]

    def result(self):
        """
        Analyzes the grid to print the game result.
        """
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

        # Print result
        if (x_wins and o_wins) or (x_total > o_total + 1) or (o_total > x_total + 1):
            print("Impossible")
        elif not x_wins and not o_wins:
            if empty_cells:
                print("Game not finished")
            else:
                print("Draw")
        elif x_wins:
            print("X wins")
        elif o_wins:
            print("O wins")

    def __str__(self):
        """
        Return a representation of the current status of the game.
        """
        line_of_dashes = 9 * "-"
        row_1 = f"| {self.grid[0][0]} {self.grid[0][1]} {self.grid[0][2]} |"
        row_2 = f"| {self.grid[1][0]} {self.grid[1][1]} {self.grid[1][2]} |"
        row_3 = f"| {self.grid[2][0]} {self.grid[2][1]} {self.grid[2][2]} |"
        return line_of_dashes + "\n" + row_1 + "\n" + row_2 + "\n" + row_3 + "\n" + line_of_dashes


game = TicTacToe()
cells = input("Enter cells: ")
game.update(cells)
print(game)
game.result()
