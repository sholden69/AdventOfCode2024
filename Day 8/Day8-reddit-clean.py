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
def calculate_antinodes(grid, steps):
    antinodes = []
    
    for freq in {*grid.values()} - {'.'}:
        antennas = [pos for pos in grid if grid[pos] == freq]
        for a, b in permutations(antennas, 2):
            antinodes += [a + n * (a - b) for n in steps]
    
    return set(antinodes)

# Count valid antinodes
def count_valid_antinodes(grid):
    total_antinodes = 0
    
    for steps in ([1], range(50)):
        antinodes = calculate_antinodes(grid, steps)
        valid_antinodes = antinodes & set(grid)
        total_antinodes += len(valid_antinodes)
    
    return total_antinodes

# Main Execution
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "input.txt")
    
    grid = parse_grid(file_path)
    result = count_valid_antinodes(grid)
    print(f"Number of unique antinode locations: {result}")
