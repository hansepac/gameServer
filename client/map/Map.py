from math import floor

class Map:
    def __init__(self):
        self.width = None
        self.height = None
        self.grid = [[]]
        self.basic_map()

    def empty_map(self):
        self.grid = [[None for _ in range(self.width)] for _ in range(self.height)]

    def display(self):
        """Displays the grid in a human-readable format."""
        for row in self.grid:
            print(" ".join(["." if cell is None else str(cell) for cell in row]))
        print()  # Blank line after the grid

    def basic_map(self, width: int = 20, height: int = 10):
        # Init
        self.width = width
        self.height = height
        self.empty_map()
        # Add Floor
        bottom_row_idx = self.height - 1
        for i in range(self.width):
            self.grid[bottom_row_idx][i] = "X"
        # Add two platforms
        half_way_idx = floor(self.height / 2) - 1
        for i in range(floor(self.width / 3)):
            self.grid[half_way_idx][i] = "X"
            self.grid[half_way_idx][(self.width-1) - i] = "X"

