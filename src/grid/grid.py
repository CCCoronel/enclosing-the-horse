class Grid:
    def __init__(self, grid: List[List[Cell]]):
        self.grid = grid
        self.n = len(grid)
        self.m = len(grid[0])

        self.horse_pos = self._find_horse()

    def _find_horse(self) -> Tuple[int, int]:
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == Cell.HORSE:
                    return (i, j)
        raise ValueError("Horse not found")

    def in_bounds(self, i: int, j: int) -> bool:
        return 0 <= i < self.n and 0 <= j < self.m

    def is_border(self, i: int, j: int) -> bool:
        return i == 0 or j == 0 or i == self.n - 1 or j == self.m - 1

    def neighbors(self, i: int, j: int):
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i + di, j + dj
            if self.in_bounds(ni, nj):
                yield ni, nj
