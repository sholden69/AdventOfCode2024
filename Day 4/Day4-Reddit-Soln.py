from collections import defaultdict
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path
input_file = os.path.join(script_dir, 'input.txt')


# Parse the grid into a dictionary using complex numbers for coordinates
# Each character is mapped to a complex number where:
# - The real part (x) represents the column index.
# - The imaginary part (y) represents the row index.
# This allows intuitive traversal using arithmetic on complex numbers.
coords = {x + 1j * y: c for y, r in enumerate(open(input_file)) for x, c in enumerate(r)}

# With complex number representation moving just becomes arithmetic
# Direction	Complex Number Offset
# Right	+1
# Left	-1
# Down	+1j
# Up	-1j
# Diagonal Down-Right	+1 + 1j
# Diagonal Down-Left	-1 + 1j
# Diagonal Up-Right	+1 - 1j
# Diagonal Up-Left	-1 - 1j

# Function to safely fetch characters from the grid. returns an emptry string if nothing found
g = lambda c: coords.get(c, "")  # Returns the character at a given complex coordinate

# Initialize counters for both patterns
s1 = s2 = 0

# Iterate through all coordinates in the grid
for c in coords:
    # Define 8 possible directions using complex numbers
    # 1 (Right), 1j (Down), 1+1j (Diagonal Down-Right), 1-1j (Diagonal Down-Left)
    # -1 (Left), -1j (Up), -1+1j (Diagonal Up-Right), -1-1j (Diagonal Up-Left)
    for d in [1, 1j, 1 + 1j, 1 - 1j, -1, -1j, -1 + 1j, -1 - 1j]:
        # Check for the word "XMAS" in the current direction
        # This validates sequential letters in a straight line across 4 cells
        s1 += g(c) + g(c + d) + g(c + d * 2) + g(c + d * 3) == "XMAS"
        
        # Check for the X-MAS pattern (diagonal cross pattern)
        # This pattern only applies to diagonal directions (both real and imaginary parts must be non-zero)
        if d.imag and d.real:
            # Check for the first diagonal: MAS
            # Check for the second perpendicular diagonal: MS
            s2 += (
                g(c + d) + g(c) + g(c - d) == "MAS" and  # Validate MAS on one diagonal
                g(c + d * 1j) + g(c - d * 1j) == "MS"    # Validate MS on the perpendicular diagonal
            )

# Print results for both patterns
print("Total occurrences of 'XMAS':", s1)
print("Total occurrences of 'X-MAS':", s2)
