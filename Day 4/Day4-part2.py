import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path
input_file = os.path.join(script_dir, 'input.txt')


def count_x_mas_patterns(grid):
    """
    Count all valid X-MAS patterns in the grid.
    The pattern is shaped like an X, and each 'MAS' can be forwards or backwards.
    """
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Define relative positions for the X-MAS pattern
    patterns = [
        # Standard X-MAS
        [(-1, -1), (-1, 1), (1, -1), (1, 1)],
        # Reverse X-MAS
        [(-1, 1), (-1, -1), (1, 1), (1, -1)]
    ]

    # Iterate through the grid, considering each cell as a potential 'A' center
    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            if grid[x][y] == 'A':  # Check if center is 'A'
                for pattern in patterns:
                    try:
                        # Check if the diagonal matches the 'X-MAS' pattern
                        if (
                            grid[x + pattern[0][0]][y + pattern[0][1]] == 'M' and
                            grid[x + pattern[1][0]][y + pattern[1][1]] == 'S' and
                            grid[x + pattern[2][0]][y + pattern[2][1]] == 'M' and
                            grid[x + pattern[3][0]][y + pattern[3][1]] == 'S'
                        ):
                            count += 1
                    except IndexError:
                        # Skip invalid coordinates
                        continue
    return count


def read_grid_from_file(file_path):
    """
    Read the word search grid from a file.
    Each line is stripped of whitespace and added as a row to the grid.
    """
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]
    return grid


# Example usage
if __name__ == "__main__":
    # Read the grid from the input file
    grid = read_grid_from_file(input_file)
    
    # Search for X-MAS patterns in the grid
    total_occurrences = count_x_mas_patterns(grid)
    
    # Display the total count of X-MAS patterns found
    print(f"Total occurrences of 'X-MAS' pattern: {total_occurrences}")
