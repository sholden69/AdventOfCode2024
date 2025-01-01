import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path
input_file = os.path.join(script_dir, 'input.txt')


def count_word_in_direction(grid, word, dx, dy):
    """
    Count occurrences of a word in a specific direction.
    dx: Direction step for x-axis (horizontal movement)
    dy: Direction step for y-axis (vertical movement)
    """
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    
    for x in range(rows):
        for y in range(cols):
            # Check if the word fits in the grid in the given direction
            if (0 <= x + dx * (word_len - 1) < rows) and (0 <= y + dy * (word_len - 1) < cols):
                match = True
                for i in range(word_len):
                    if grid[x + i * dx][y + i * dy] != word[i]:
                        match = False
                        break
                if match:
                    count += 1
    return count


def count_all_occurrences(grid, word):
    """
    Count all occurrences of the word in the grid in all directions.
    """
    directions = [
        (0, 1),   # Right (horizontal)
        (1, 0),   # Down (vertical)
        (1, 1),   # Diagonal Down-Right
        (1, -1),  # Diagonal Down-Left
        (0, -1),  # Left (horizontal, reversed)
        (-1, 0),  # Up (vertical, reversed)
        (-1, -1), # Diagonal Up-Left
        (-1, 1)   # Diagonal Up-Right
    ]
    
    total_count = 0
    for dx, dy in directions:
        total_count += count_word_in_direction(grid, word, dx, dy)
    return total_count


def read_grid_from_file(file_path):
    """
    Read the word search grid from a file.
    """
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]
    return grid


# Example usage
if __name__ == "__main__":
    grid = read_grid_from_file(input_file)
    word_to_find = "XMAS"
    total_occurrences = count_all_occurrences(grid, word_to_find)
    print(f"Total occurrences of '{word_to_find}': {total_occurrences}")
