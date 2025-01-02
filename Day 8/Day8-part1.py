from itertools import combinations
import os

def parse_grid(file_path):
    """
    Parse the grid into a dictionary using complex numbers as keys.
    """
    return {i + j * 1j: c 
            for i, row in enumerate(open(file_path)) 
            for j, c in enumerate(row.strip())}


def calculate_antinodes(grid):
    """
    Calculate unique antinode positions based on antenna pairs.
    """
    # Group antenna positions by frequency
    antennas = {}
    for pos, freq in grid.items():
        if freq != '.':  # Ignore empty spaces
            antennas.setdefault(freq, []).append(pos)
    
    # Store unique antinode positions
    antinodes = set()
    
    # Check pairs of antennas with the same frequency
    for freq, positions in antennas.items():
        for a, b in combinations(positions, 2):
            midpoint = (a + b) / 2
            distance = abs(a - b)
            
            # Check if one antenna is twice as far from the midpoint as the other
            if distance % 2 == 0:
                offset = (b - a) / 2
                antinodes.add(midpoint + offset)
                antinodes.add(midpoint - offset)
    
    # Filter antinodes that are within the grid bounds
    grid_bounds = {pos for pos in grid.keys()}
    return {node for node in antinodes if node in grid_bounds}


def count_antinode_locations(file_path):
    """
    Parse the grid, calculate antinodes, and return their count.
    """
    grid = parse_grid(file_path)
    antinodes = calculate_antinodes(grid)
    return len(antinodes)


# Main Execution
if __name__ == "__main__":
       # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the file path
    file_path = os.path.join(script_dir, "input.txt")
    
    result = count_antinode_locations(file_path)
    print(f"Number of unique antinode locations: {result}")
