def dfs_solve_maze():
    """Performs DFS to solve the maze."""
    stack = [(0, 0)]
    visited = set()
    path = []  # keep path explored. 

    while stack:
        row, col = stack.pop()

        if (row, col) in visited:
            continue
          
        visited.add((row, col))
        path.append((row, col))

        # if reached the goal
        if (row, col) == (ROWS - 1, COLS - 1):
            print("Maze solved!")
            return True

        # Explore neighbors in given depth-first order
        for dr, dc in DIRECTIONS:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < ROWS and 0 <= new_col < COLS and maze[new_row][new_col] == 1:
                stack.append((new_row, new_col))

    print("No path found!")
    return False
