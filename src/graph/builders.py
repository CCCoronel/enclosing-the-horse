def build_graph_from_grid(grid: Grid) -> Graph:
    g = Graph()

    for i in range(grid.n):
        for j in range(grid.m):
            if grid.grid[i][j] == Cell.WATER:
                continue

            u = cell_id(i, j, grid.m)

            for ni, nj in grid.neighbors(i, j):
                if grid.grid[ni][nj] == Cell.WATER:
                    continue

                v = cell_id(ni, nj, grid.m)

                # custo de bloquear essa conexão
                g.add_edge(u, v, capacity=1)
                g.add_edge(v, u, capacity=1)

    return g
