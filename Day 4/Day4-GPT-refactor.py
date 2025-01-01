import os
# ChatGPT came up with this after being shown a working solution from Reddit
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path
input_file = os.path.join(script_dir, 'input.txt')

# Parse grid into complex coordinates
coords = {x + 1j * y: c for y, r in enumerate(open(input_file)) for x, c in enumerate(r.strip())}
g = lambda c: coords.get(c, "")  # Safely fetch grid characters


def count_xmas_patterns(coords):
    """
    Count occurrences of 'XMAS' in all 8 directions.
    """
    directions = [1, 1j, 1+1j, 1-1j, -1, -1j, -1+1j, -1-1j]
    count = 0

    for c in coords:
        for d in directions:
            if g(c) + g(c + d) + g(c + d * 2) + g(c + d * 3) == "XMAS":
                count += 1

    return count


def count_x_mas_patterns(coords):
    """
    Count occurrences of 'X-MAS' cross-diagonal patterns.
    """
    directions = [1+1j, 1-1j, -1+1j, -1-1j]
    count = 0

    for c in coords:
        for d in directions:
            # Check MAS in one diagonal and MS in the other
            if (
                g(c + d) + g(c) + g(c - d) == "MAS" and
                g(c + d * 1j) + g(c - d * 1j) == "MS"
            ):
                count += 1

    return count


if __name__ == "__main__":
    # Count 'XMAS' patterns
    xmas_count = count_xmas_patterns(coords)
    print(f"Total occurrences of 'XMAS': {xmas_count}")

    # Count 'X-MAS' patterns
    x_mas_count = count_x_mas_patterns(coords)
    print(f"Total occurrences of 'X-MAS': {x_mas_count}")
