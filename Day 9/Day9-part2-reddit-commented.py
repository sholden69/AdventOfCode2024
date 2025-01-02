# code from https://www.reddit.com/user/Ok-Builder-2348/

import os
import heapq
from collections import defaultdict

# Construct the file path
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")


def parse_disk_map(disk_map):
    """
    Parse the disk map into file metadata (filled_grid) and free space metadata (gaps).
    """
    lengths = [int(num) for num in disk_map]  # Parse each digit as an integer
    
    filled_grid = {}  # Tracks file metadata (ID: [start, length])   eg filled_grid = {0: [0, 2], 1: [5, 3], 2: [11, 1]}
    gaps = defaultdict(list)  # Tracks gaps (length: [start positions])  eg gaps = {3: [2], 2: [8]}
    
    cur_pos = 0  # Current position pointer
    
    for i, num in enumerate(lengths):
        if i % 2 == 0: #every other digit is a file block so use even numbers to detect that
            # File block: store ID, start position, and length
            filled_grid[i // 2] = [cur_pos, num]
        else:
            # Free space: store in a heap for efficient access
            if num > 0:
                heapq.heappush(gaps[num], cur_pos)
        cur_pos += num  # Increment position by the block length
    
    return filled_grid, gaps


def move_files(filled_grid, gaps):
    """
    Move files into the leftmost valid gap, starting from the highest file ID.
    """
    for i in sorted(filled_grid.keys(), reverse=True):
        file_start, file_len = filled_grid[i]
       
        # Find all valid gaps
        possible_gaps = sorted([[gaps[gap_len][0], gap_len] for gap_len in gaps if gap_len >= file_len])
       
        if possible_gaps:
            gap_start, gap_len = possible_gaps[0] #pick the leftmost one
            if file_start > gap_start:
                # Move file to the gap
                filled_grid[i] = [gap_start, file_len]
                
                # Update the gap metadata
                remaining_gap_len = gap_len - file_len
                heapq.heappop(gaps[gap_len])
                
                if not gaps[gap_len]:
                    del gaps[gap_len]  # Remove exhausted gap
                
                if remaining_gap_len > 0:
                    heapq.heappush(gaps[remaining_gap_len], gap_start + file_len)


def calculate_checksum(filled_grid):
    """
    Calculate the checksum using file metadata directly.
    """
    return sum(
        num * (start * length + (length * (length - 1)) // 2)
        for num, (start, length) in filled_grid.items()
    )


def main():
    # Read the input
    with open(file_path, 'r') as file:
        disk_map = file.readline().strip()
    
    # Step 1: Parse the disk map
    filled_grid, gaps = parse_disk_map(disk_map)
    
    # Step 2: Move files
    move_files(filled_grid, gaps)
    
    # Step 3: Calculate the checksum
    checksum = calculate_checksum(filled_grid)
    
    print(f"Filesystem checksum: {checksum}")


# Entry Point
if __name__ == "__main__":
    main()
