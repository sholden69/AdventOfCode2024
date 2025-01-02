from itertools import permutations
import os


# Parse the grid
def parse_grid(file_path):
    return {
        i + j * 1j: c
        for i, row in enumerate(open(file_path))
        for j, c in enumerate(row.strip())
    }

# Calculate antinodes
def calculate_antinodes(grid):
    anti = set()
    for r in [1], range(50):
        for freq in {*grid.values()} - {'.'}:
            antennas = [p for p in grid if grid[p] == freq]
            pairs = permutations(antennas, 2)
            for a, b in pairs:
                for n in r:
                    anti.add(a + n * (a - b))
    return anti

# Count valid antinodes
def count_valid_antinodes(grid):
    antinodes = calculate_antinodes(grid)
    return len(antinodes & set(grid))

# Main Execution
if __name__ == "__main__":
      # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the file path
    file_path = os.path.join(script_dir, "input.txt")
    grid = parse_grid(file_path)
    result = count_valid_antinodes(grid)
    print(f"Number of unique antinode locations: {result}")
