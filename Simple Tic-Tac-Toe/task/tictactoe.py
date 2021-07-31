class TicTacToe:
    """
    A class to represent TicTacToe game.

    ...

    Attributes
    ----------
        grid : list
            contains the cells of the game and their current status.
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
        self.grid = list(cells)

    def __str__(self):
        """
        Return a representation of the current status of the game.
        """
        line_of_dashes = 9 * "-"
        row_1 = f"| {self.grid[0]} {self.grid[1]} {self.grid[2]} |"
        row_2 = f"| {self.grid[3]} {self.grid[4]} {self.grid[5]} |"
        row_3 = f"| {self.grid[6]} {self.grid[7]} {self.grid[8]} |"
        return line_of_dashes + "\n" + row_1 + "\n" + row_2 + "\n" + row_3 + "\n" + line_of_dashes


game = TicTacToe()
cells = input("Enter cells: ")
game.update(cells)
print(game)
